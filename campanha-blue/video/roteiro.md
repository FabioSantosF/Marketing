# Roteiro + Pós-produção — "Blue" (Instagram Reels · 2160×3840 · 60fps · 65,97s)

Análise feita a partir de 5 frames enviados pelo usuário (não do arquivo `.mov` inteiro — o ambiente remoto não tem acesso ao arquivo local de 254MB). Comandos abaixo devem ser rodados na máquina onde está o `Blue_Final.mov` e as coordenadas de marca d'água são estimativas por proporção — conferir no preview antes de renderizar em definitivo.

## ⚠️ Nota de compliance — confirmado pelo usuário

As cenas de interior (sala, varanda gourmet, cozinha, banheiro) são **renderizações/decoração virtual gerada por IA** (marca "CapCut AI"), não fotos reais do imóvel no estado atual. Por isso é **obrigatório** avisar isso na peça, para não configurar publicidade enganosa (CDC / normas CRECI):

- Adicionar texto fixo no canto do vídeo durante as cenas de interior: **"Imagem ilustrativa — decoração virtual"** (fonte pequena, ~14-16px numa base 1080px, opacidade 80%, canto inferior).
- Repetir o aviso na legenda do post (ver sugestão de legenda abaixo).
- Se o corretor for perguntado, deixar claro que o imóvel está em fase de acabamento/entrega e a decoração é sugestão.

## 1. Color grading (padrão Conceitto — litorâneo, quente, "manhã na praia")

O grading já usado na campanha UP Vilas (mesma imobiliária) é claro, quente e com céu/verde saturados — replicar aqui para manter identidade visual entre os vídeos da Conceitto.

**Cena externa (caminhada, coqueiros, escadaria azul):**
- White balance: neutralizar levemente para ~5600K (a imagem atual está com leve véu/haze — reduzir neblina aumentando contraste local +10 a +15)
- Highlights: −15 a −20 (o céu está quase estourando em algumas partes)
- Shadows/Blacks: +10 a +15 (levantar sombra da estrutura de madeira à esquerda, que está muito escura/sem detalhe)
- Saturação global: +8 a +12
- HSL seletivo: verde (coqueiros) +15 saturação / −5 luminância para não "estourar"; azul (céu e escada) +10 saturação
- Vibrance (protege pele): +10, mantendo o tom de pele da pessoa natural — não empurrar magenta/laranja demais
- Contraste: leve S-curve, blacks levantados (~+8), para não achatar a sombra do madeiramento

**Cenas de interior (sala, varanda, cozinha, banheiro):**
- White balance: já estão consistentemente quentes (~3200-3400K, luz de LED/pendente) — manter, mas empurrar +100K global pra unificar com a cena externa e evitar "salto" de temperatura no corte
- Highlights: −25 a −30 nas janelas (estão estourando — sala e varanda mostram céu/rua completamente sem detalhe pela janela)
- Se usar DaVinci Resolve: criar Power Window na área da janela e aplicar exposure −1 a −1.5 EV só ali, preservando o resto do ambiente
- Contraste: leve, os ambientes já têm um look "clean/minimalista" (bom para real estate) — não exagerar, só uma curva suave em S
- Saturação: +5 apenas (ambientes neutros/bege não devem ficar "gritantes")
- Nitidez/Clarity: +10 a +15 — os frames estão um pouco soft/desfocados nos detalhes (textura de tapete, madeira)

**Unificação entre clipes:** aplicar um LUT/preset único por cima de tudo no fim (ex: "Warm Neutral" ou grade equivalente no Premiere/Resolve) pra garantir que o corte entre exterior (mais saturado/luz dura) e interior (mais suave/quente) não pareça dois vídeos diferentes.

**Equivalente em ffmpeg (aproximado, pra quem não usa NLE):**
```bash
ffmpeg -i Blue_Final.mov -vf "eq=contrast=1.08:saturation=1.10:brightness=0.01,curves=preset=medium_contrast,unsharp=5:5:0.6" -c:a copy Blue_graded.mov
```
Isso dá só uma base — o ajuste fino de highlights/shadows por cena (principalmente as janelas estouradas) só é possível numa NLE com scopes (Resolve, Premiere), o `eq` do ffmpeg é global e não vai roubar as janelas com precisão.

## 2. Remoção de marcas d'água

### CapCut AI (canto superior esquerdo, cenas de interior) — fácil
É um selo estático numa área de fundo pouco complexa (parede/teto escuro). Dá pra remover direto com `delogo`:

```bash
# Primeiro, teste com show=1 para conferir se a caixa cobre exatamente o selo
ffmpeg -i Blue_Final.mov -vf "delogo=x=0:y=0:w=320:h=230:show=1" -frames:v 1 preview_capcut.png

# Depois de ajustar x/y/w/h olhando o preview, renderiza sem show
ffmpeg -i Blue_Final.mov -vf "delogo=x=0:y=0:w=320:h=230:show=0" -c:a copy Blue_sem_capcut.mov
```
Coordenadas de partida (estimadas para o frame 2160×3840 — ajustar ±20px olhando o preview): `x=0 y=0 w=320 h=230`.

Se a marca só aparece em parte do vídeo (não do início ao fim), restrinja com `enable`:
```bash
delogo=x=0:y=0:w=320:h=230:show=0:enable='between(t,7,44)'
```
(troque `7,44` pelo intervalo real em segundos onde aparecem as cenas de interior — preciso que você me diga esses tempos, ou eu estimo olhando o vídeo completo se você conseguir enviar os cortes).

### CONCEITTO (parte inferior da cena externa) — mais delicada
Essa marca está sobre uma área com textura (calçada de pedra) e a pessoa caminha perto dela em vários frames — um `delogo` simples vai borrar/manchar visivelmente porque a caixa muda de conteúdo a cada frame (a pessoa passa por cima/perto). Recomendo:

- **DaVinci Resolve** (Fusion → Object Removal / Magic Mask) — rastreia e reconstrói o fundo automaticamente, inclusive com movimento de câmera e do "objeto" (a marca é estática, mas o fundo atrás dela se move).
- **After Effects** (Content-Aware Fill, com um track mask na área do logo) — mesma lógica, boa opção se já usam Adobe.

Coordenada aproximada da área a mascarar (2160×3840): `x: 605–1469px, y: 2918–3494px` (bloco do logo + texto "VENDAS · LOCAÇÃO · ADM").

**Decisão do usuário:** tentar remover; só manter se a remoção comprometer a qualidade da imagem.

Critério prático pra decidir qual caminho seguir, ao testar no Resolve/AE:
- **Removeu limpo** (sem manchas, sem "respiração"/tremor no fundo reconstruído, sem artefato visível quando a pessoa passa perto/sobre a área) → segue removida, vídeo fica sem marca nessa cena.
- **Ficou com artefato visível** (mancha, borrão, fundo "derretendo" quando ela caminha por cima da região) → **não force a remoção**. Faça como no vídeo do UP Vilas (commit `9b9b0cd`, mesmo projeto): não se tenta apagar a marca da filmagem bruta — em vez disso, aplica-se por cima um **logo limpo da Conceitto, recortado com fundo transparente, no canto inferior direito**, longe da pessoa e de qualquer área de textura complexa, como assinatura de marca deliberada (mesmo lugar/tratamento usado nas peças estáticas e no vídeo do UP Vilas). Isso evita tanto o artefato quanto o problema de deixar a marca original malposicionada.

### Nota à parte — artefato de movimento (não é marca d'água)
No frame da caminhada, os braços/vestido da pessoa têm um rastro/"fantasma" (ghosting) — parece efeito de suavização de movimento (motion smoothing/frame interpolation) aplicado no corte, comum em apps como CapCut quando desaceleram um clipe. Isso não se resolve com grading; as opções são: (a) re-exportar esse clipe sem a interpolação/smooth motion ativada, ou (b) trocar por outro take da mesma cena sem o efeito.

## 3. Roteiro falado (pronto para colar no ElevenLabs)

Timing calibrado para os 65,97s do vídeo, no tom já estabelecido pela Conceitto (poético na abertura, direto nos diferenciais, CTA generoso no fechamento — mesmo padrão do roteiro do UP Vilas). Bairro e corretora confirmados pelo usuário: **Vilas do Atlântico, Lauro de Freitas** / **Juli**.

```
[0:00–0:08] (cena externa — caminhada, coqueiros, mar ao fundo)
Tem gente que sonha acordado olhando pro mar.
Aqui, você acorda dentro dele.

[0:08–0:16] (transição para interior — sala)
Bem-vindo ao Blue, em Vilas do Atlântico — onde cada ambiente
foi pensado pra parecer um respiro.

[0:16–0:26] (sala de estar)
Sala ampla, luz natural o dia inteiro,
e uma decoração que combina conforto com sofisticação.

[0:26–0:36] (varanda gourmet)
Na varanda gourmet, seu cantinho pra receber amigos,
com vista pra rua e aquele clima gostoso de fim de tarde.

[0:36–0:46] (cozinha integrada / segunda sala)
Cozinha integrada, acabamento de primeira,
e cada detalhe pensado pra facilitar sua rotina.

[0:46–0:54] (banheiro)
Banheiros amplos, com mármore e uma luz
que faz até o dia mais comum parecer especial.

[0:54–0:66] (CTA / card final)
O Blue é mais que um endereço — é um novo jeito de morar.
Chama a Juli no direct @conceittoimoveis
ou pelo WhatsApp que está na tela, e agenda sua visita.
```

**Contagem:** ~118 palavras / ritmo confortável (~1,8 palavras/s) para caber nos 66s com pausas respiráveis entre blocos.

**Ainda em aberto, se quiser deixar o roteiro mais recheado:**
- Metragem, nº de quartos/suítes e valor (se for divulgar) — dá pra encaixar uma frase extra no bloco 0:16–0:26 sem perder o timing
- Diferenciais extras que apareçam em outras cenas do vídeo completo (só analisei 5 frames enviados; o vídeo tem 66s e pode ter mais ambientes que eu não vi)

## 4. Pipeline de execução — passo a passo (para rodar localmente)

Você decidiu rodar os comandos você mesmo. Sequência recomendada:

### Passo 1 — Mapear os tempos das cenas
Antes de aplicar o `delogo` do CapCut AI com tempo restrito (senão ele borra o canto superior esquerdo da cena externa, que tem coqueiro/estrutura de madeira ali). Gere um frame por segundo com o tempo marcado:
```bash
mkdir -p frames_mapa
ffmpeg -i Blue_Final.mov -vf "fps=1,drawtext=text='%{pts\:hms}':x=10:y=10:fontsize=36:fontcolor=yellow:box=1:boxcolor=black@0.6" frames_mapa/f_%03d.png
```
Abra a pasta `frames_mapa` e anote: (a) em que segundo começa e termina cada cena de interior (onde aparece "CapCut AI"), e (b) em que segundo começa/termina a cena externa (onde aparece "CONCEITTO"). Substitua os placeholders `START_CAPCUT`/`END_CAPCUT` abaixo por esses valores (em segundos, ex: `7.5`).

### Passo 2 — Grading + remoção do CapCut AI + conversão pra H.264 (tudo num comando)
```bash
ffmpeg -i Blue_Final.mov -vf "\
delogo=x=0:y=0:w=320:h=230:show=0:enable='between(t,START_CAPCUT,END_CAPCUT)',\
eq=contrast=1.08:saturation=1.10:brightness=0.01,\
curves=preset=medium_contrast,\
unsharp=5:5:0.6" \
-c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
-c:a aac -b:a 192k \
Blue_etapa1.mp4
```
Confira o resultado antes de seguir — se a caixa do `delogo` estiver deixando um "quadrado" visível ou desalinhado, reajuste `x/y/w/h` e rode de novo (é rápido, o arquivo já está bem menor em H.264).

### Passo 3 — Marca d'água CONCEITTO (cena externa)
Abra `Blue_etapa1.mp4` no DaVinci Resolve (ou After Effects). Aplique o Object Removal/Magic Mask (ou Content-Aware Fill) na área `x: 605–1469px, y: 2918–3494px` só durante a cena externa. Avalie pelo critério já definido na seção 2:
- Ficou limpo → exporte assim.
- Ficou com artefato → **não force**: desfaça a tentativa de remoção e, em vez disso, insira um logo limpo da Conceitto (fundo transparente) no canto inferior direito dessa cena, do mesmo jeito que foi feito no vídeo do UP Vilas. *Observação: não há um arquivo de logo Conceitto isolado neste repositório — a versão usada no UP Vilas foi aplicada direto nos binários (PNG/MP4), então você vai precisar do arquivo de logo original de vocês (ou recortar um trecho limpo de algum material antigo da marca) pra reaproveitar aqui.*

### Passo 4 — Texto de compliance (imagens ilustrativas)
Ainda no Resolve/AE, adicione o texto **"Imagem ilustrativa — decoração virtual"** sobreposto durante as cenas de interior (conforme a nota de compliance no topo deste arquivo).

### Passo 5 — Exportação final
Exporte em H.264, 2160×3840 (ou 1080×1920 se preferir arquivo mais leve — Instagram recomprime de qualquer forma), AAC 192kbps. Confira que o resultado ainda bate com os requisitos de Reels (duração ≤90s, 9:16, ≤4GB) — já validamos isso na análise técnica anterior.

Qualquer travamento nesses passos (comando dando erro, coordenada errada, resultado estranho), me manda o print/print do erro que eu ajusto o comando.

## Especificações técnicas do arquivo de origem
- Resolução: 2160×3840 (9:16, 4K vertical)
- Codec: HEVC (H.265), yuv420p, 60fps — recomendado converter para H.264 antes de publicar (ver análise técnica anterior)
- Duração: 65,97s · Tamanho: ~254MB
- Áudio original: AAC (sem locução — precisa da voz gerada no ElevenLabs)
