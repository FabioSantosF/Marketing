# Tríduo e Festa da Sagrada Família 2026: post de agradecimento

Coloca uma foto do evento dentro da moldura do template oficial de agradecimento.

| Arquivo | Conteúdo |
|---|---|
| `saida/post-agradecimento.png` | **Post final** em 3072×2048, com o rodapé original (Diácono Genildo) |
| `saida/post-agradecimento-1536x1024.jpg` | O mesmo post no tamanho original do template |
| `saida/post-agradecimento-rodape-livre.png` | Mesma arte com a área do texto de agradecimento vazia |
| `saida/noite-2-post-agradecimento.png` (+ `-1536x1024.jpg`) | **2ª noite** (Pe. César Dias), template próprio com a faixa "2ª Noite" sobre a foto |
| `saida/exemplo-texto-dinamico.png` | Exemplo do texto gerado pelo script (`--nome` / `--texto`) |

## Como a foto foi encaixada
- A área interna da moldura dourada, com os cantos recortados, é detectada automaticamente. A foto entra por baixo da moldura, e logos, textos, cores e ornamentos do template ficam como estão.
- A foto só foi **redimensionada proporcionalmente** e recebeu uma **gradação de cor global e leve** (tom um pouco mais quente). Não houve retoque, IA nem ajuste local: os rostos e as pessoas estão iguais aos da foto original.
- A moldura (~1,47:1) é mais "alta" que a foto (16:9). Para não cortar o diácono sentado à direita, que encosta na borda da foto, foram removidos 230 px de púlpito à esquerda. A faixa que faltava em cima foi preenchida só com o forro liso do teto.

## Gerar uma nova versão
```bash
pip install pillow numpy scipy opencv-python-headless
python3 compor_post.py --foto entrada/OUTRA_FOTO.jpg --saida saida/novo.png \
  --nome "Padre Fulano" \
  --texto "pela celebração desta noite do Tríduo da Sagrada Família..."
```
Comando usado na 2ª noite:
```bash
python3 compor_post.py --template entrada/template-noite-2.png --foto entrada/foto-noite-2.jpg \
  --saida saida/noite-2-post-agradecimento.png --corte-esquerda 250 --corte-direita 160 --estender base
```
Selos ou faixas do template que ficam dentro da moldura, como "2ª Noite", são detectados e continuam por cima da foto.

Use `--limpar-rodape` para gerar sem texto e `--corte-esquerda N` para ajustar o enquadramento.
