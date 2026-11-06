#!/usr/bin/env python3
"""Insere uma foto do evento dentro da moldura do template de agradecimento do Tríduo.

- Detecta automaticamente a área interna da moldura dourada (cantos recortados inclusos).
- Recorta/redimensiona a foto proporcionalmente (sem distorcer, sem retoque nas pessoas).
- Aplica apenas uma gradação de cor global e sutil (tom mais quente) para harmonizar.
- Opcional: limpa o texto do rodapé e/ou escreve uma nova mensagem de agradecimento.

Uso:
  python3 compor_post.py                                 # mantém o rodapé original
  python3 compor_post.py --limpar-rodape                 # deixa o rodapé livre
  python3 compor_post.py --nome "Padre Fulano" \\
      --texto "pela celebração desta noite do Tríduo..."  # novo agradecimento
"""
import argparse
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd

AQUI = Path(__file__).resolve().parent
ESCALA = 2  # saída em 3072x2048 (2x o template original)

FONTE_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
FONTE_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"
AZUL = (24, 38, 120)
VERMELHO = (150, 18, 28)

# Área do texto do rodapé (coordenadas do template 1536x1024), abaixo do selo "Agradecimento".
RODAPE = (600, 774, 1436, 946)


def mascara_moldura(tpl):
    """Região interna da moldura: área clara/neutra conectada ao centro do quadro."""
    a = tpl.astype(int)
    sat = a.max(2) - a.min(2)
    lab, _ = nd.label(sat < 22)
    m = lab == lab[380, 1000]
    # preenche só furos pequenos (ruído); furos grandes são selos/faixas do template
    # que ficam POR CIMA da foto (ex.: "2ª Noite")
    furos = nd.binary_fill_holes(m) & ~m
    fl, n = nd.label(furos)
    if n:
        tam = nd.sum(furos, fl, range(1, n + 1))
        m |= np.isin(fl, 1 + np.where(tam < 3000)[0])
    m = nd.binary_dilation(m, iterations=1)  # cobre o pixel de antialias junto ao filete dourado
    return m


def preparar_foto(foto, larg, alt, x0_corte, x1_corte=0, estender="topo"):
    """Corta as laterais e, se faltar altura, estende uma faixa estreita a partir da borda
    (topo: teto liso; base: continuação vertical do altar). Nenhuma pessoa é gerada/alterada."""
    f = foto[:, x0_corte:foto.shape[1] - x1_corte]
    h, w = f.shape[:2]
    alt_nec = int(round(w * alt / larg))
    if alt_nec > h:
        ext = alt_nec - h
        borda = f[0:3] if estender == "topo" else f[-3:]
        faixa = borda.astype(np.float32).mean(0)
        faixa = cv2.GaussianBlur(faixa[None], (0, 0), sigmaX=6)[0]
        bloco = np.repeat(faixa[None], ext, 0)
        grad = np.linspace(0.90, 1.0, ext, dtype=np.float32)[:, None, None]
        if estender != "topo":
            grad = grad[::-1]
        bloco = bloco * grad + np.random.default_rng(7).normal(0, 1.6, bloco.shape)
        bloco = np.clip(bloco, 0, 255).astype(np.uint8)
        f = np.vstack([bloco, f] if estender == "topo" else [f, bloco])
    elif alt_nec < h:
        corte = h - alt_nec
        f = f[corte:]  # corta só parede no alto
    return cv2.resize(f, (larg, alt), interpolation=cv2.INTER_AREA)


def gradacao(img):
    """Gradação global sutil: aquece levemente e assenta os brancos no tom pergaminho."""
    x = img.astype(np.float32) / 255.0
    ganho = np.array([1.025, 1.0, 0.955], np.float32)
    x = x * ganho
    x = x + 0.012 * (1 - x)  # leve lift de sombras
    return np.clip(x * 255, 0, 255).astype(np.uint8)


def nitidez(img, forca):
    """Nitidez clássica (unsharp mask) só na luminância, aplicada igualmente na foto toda.
    Realça bordas já existentes; não recria nem altera traços. Limiar evita realçar ruído."""
    if forca <= 0:
        return img
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB).astype(np.float32)
    L = lab[..., 0]
    # detalhe fino (contornos, óculos, tecido)
    det = L - cv2.GaussianBlur(L, (0, 0), 1.1)
    det = np.sign(det) * np.maximum(np.abs(det) - 1.0, 0)  # limiar anti-ruído
    # micro-contraste suave ("clarity") para tirar o aspecto lavado
    cla = L - cv2.GaussianBlur(L, (0, 0), 10)
    L2 = L + forca * (0.9 * det + 0.18 * cla)
    lab[..., 0] = np.clip(L2, 0, 255)
    return cv2.cvtColor(lab.astype(np.uint8), cv2.COLOR_LAB2RGB)


def _preencher(reg, valido, sigma):
    num = cv2.GaussianBlur(reg * valido[..., None], (0, 0), sigma)
    den = cv2.GaussianBlur(valido, (0, 0), sigma)[..., None]
    return num / np.maximum(den, 1e-4)


def limpar_rodape(tpl):
    """Remove letras + brilho do rodapé e reconstrói o pergaminho por pixel."""
    x0, y0, x1, y1 = RODAPE
    reg = tpl[y0:y1, x0:x1].astype(np.float32)
    lum = reg.mean(2)
    sat = reg.max(2) - reg.min(2)
    # 1) estimativa robusta do fundo (mediana grande ignora as letras)
    med = cv2.medianBlur(tpl[y0:y1, x0:x1], 41).astype(np.float32)
    # 2) texto = escuro/saturado; brilho (glow) = mais claro que o fundo local
    dif = lum - med.mean(2)
    texto = (lum < 215) | (sat > 70) | (np.abs(dif) > 14)
    texto = nd.binary_dilation(texto, iterations=5)
    valido = (~texto).astype(np.float32)
    fundo = _preencher(reg, valido, 10)
    fundo = np.where(den_baixo(valido, 10)[..., None], _preencher(reg, valido, 35), fundo)
    fundo += np.random.default_rng(3).normal(0, 1.0, fundo.shape)
    alfa = cv2.GaussianBlur(texto.astype(np.float32), (0, 0), 2)[..., None]
    out = tpl.copy()
    out[y0:y1, x0:x1] = np.clip(fundo * alfa + reg * (1 - alfa), 0, 255).astype(np.uint8)
    return out


def den_baixo(valido, sigma):
    return cv2.GaussianBlur(valido, (0, 0), sigma) < 0.08


def escrever_rodape(img, nome, texto, s):
    """Primeira linha: 'Agradecemos ao' + nome em destaque; depois o texto quebrado em linhas."""
    d = ImageDraw.Draw(img)
    cx = 1010 * s
    f_reg = ImageFont.truetype(FONTE_REG, 34 * s)
    f_nome = ImageFont.truetype(FONTE_BOLD, 40 * s)

    pre = "Agradecemos ao "
    w1 = d.textlength(pre, font=f_reg)
    w2 = d.textlength(nome, font=f_nome)
    x = cx - (w1 + w2) / 2
    y = 800 * s
    d.text((x, y + 6 * s), pre, font=f_reg, fill=AZUL)
    d.text((x + w1, y), nome, font=f_nome, fill=VERMELHO)

    larg_max = 760 * s
    for tam in range(30, 19, -1):  # reduz a fonte até caber em 3 linhas
        f_txt = ImageFont.truetype(FONTE_REG, tam * s)
        linhas, atual = [], ""
        for p in texto.split():
            t = (atual + " " + p).strip()
            if d.textlength(t, font=f_txt) <= larg_max:
                atual = t
            else:
                linhas.append(atual)
                atual = p
        linhas.append(atual)
        if len(linhas) <= 3:
            break
    y = 852 * s
    for ln in linhas[:3]:
        w = d.textlength(ln, font=f_txt)
        d.text((cx - w / 2, y), ln, font=f_txt, fill=AZUL)
        y += int(tam * 1.25) * s
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default=AQUI / "entrada/template-agradecimento.png")
    ap.add_argument("--foto", default=AQUI / "entrada/foto-pregacao.jpg")
    ap.add_argument("--saida", default=AQUI / "saida/post-agradecimento.png")
    ap.add_argument("--corte-esquerda", type=int, default=230,
                    help="pixels removidos da esquerda da foto original")
    ap.add_argument("--nitidez", type=float, default=0.0,
                    help="força da nitidez (0 = desligada; 1 = recomendada; 1.5 = forte)")
    ap.add_argument("--corte-direita", type=int, default=0)
    ap.add_argument("--estender", choices=["topo", "base"], default="topo",
                    help="lado completado se a foto for mais baixa que a moldura")
    ap.add_argument("--limpar-rodape", action="store_true")
    ap.add_argument("--nome", help="nome em destaque no agradecimento")
    ap.add_argument("--texto", help="restante da mensagem de agradecimento")
    a = ap.parse_args()

    tpl = np.array(Image.open(a.template).convert("RGB"))
    foto = np.array(Image.open(a.foto).convert("RGB"))

    if a.limpar_rodape or a.texto:
        tpl = limpar_rodape(tpl)

    m = mascara_moldura(tpl)
    ys, xs = np.where(m)
    bx0, bx1, by0, by1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1

    s = ESCALA
    H, W = tpl.shape[0] * s, tpl.shape[1] * s
    base = cv2.resize(tpl, (W, H), interpolation=cv2.INTER_LANCZOS4)
    alfa = cv2.resize(m.astype(np.float32), (W, H), interpolation=cv2.INTER_LINEAR)
    alfa = cv2.GaussianBlur(alfa, (0, 0), 0.7)[..., None]

    larg, alt = (bx1 - bx0) * s, (by1 - by0) * s
    f = nitidez(gradacao(preparar_foto(foto, larg, alt, a.corte_esquerda, a.corte_direita, a.estender)), a.nitidez)
    camada = np.zeros_like(base)
    camada[by0 * s:by1 * s, bx0 * s:bx1 * s] = f

    out = (camada * alfa + base * (1 - alfa)).astype(np.uint8)
    img = Image.fromarray(out)
    if a.texto:
        img = escrever_rodape(img, a.nome or "", a.texto, s)

    Path(a.saida).parent.mkdir(parents=True, exist_ok=True)
    img.save(a.saida, optimize=True)
    img.resize((tpl.shape[1], tpl.shape[0]), Image.LANCZOS).save(
        str(a.saida).replace(".png", "-1536x1024.jpg"), quality=95)
    print("ok:", a.saida, img.size)


if __name__ == "__main__":
    main()
