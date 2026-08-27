# Roteiro + Pós-produção — "Blue" (Instagram Reels · 2160×3840 · 60fps · 65,97s)

Análise feita a partir de 5 frames enviados pelo usuário (não do arquivo `.mov` inteiro — o ambiente remoto não tem acesso ao arquivo local de 254MB). Comandos abaixo devem ser rodados na máquina onde está o `Blue_Final.mov` e as coordenadas de marca d'água são estimativas por proporção — conferir no preview antes de renderizar em definitivo.

## ⚠️ Nota de compliance — confirmado pelo usuário

As cenas de interior (sala, varanda gourmet, cozinha, banheiro) são **renderizações/decoração virtual gerada por IA** (marca "CapCut AI"), não fotos reais do imóvel no estado atual. Confirmado pelo mapeamento do `contact_sheet.png`: o bloco de interiores (~22s–63s) intercala essas cenas mobiliadas/render com cenas do imóvel **em obra/estado bruto** (concreto aparente, sem mobília) — ou seja, o próprio vídeo mostra lado a lado "como está hoje" e "como pode ficar decorado", o que reforça a obrigatoriedade do aviso. Por isso é **obrigatório** avisar isso na peça, para não configurar publicidade enganosa (CDC / normas CRECI):

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

**Mapeamento real das cenas (feito a partir do `contact_sheet.png`, grade de 2s por célula):**
- 0s–~20s: sequência externa (praia/coqueiros/restaurante) — marca **CONCEITTO**
- ~20s–22s: transição
- ~22s–63s: interiores — mistura de cenas **mobiliadas/render (marca CapCut AI)** com cenas **em obra/estado bruto (sem marca)**
- ~64s+: card final com logo CONCEITTO (intencional, não mexer — ver seção 2.2)

Restrinja o `delogo` do CapCut AI só ao bloco de interiores (aplicar num intervalo maior que o necessário não é problema aqui — nos trechos "em obra" sem marca, a caixa cai sobre parede/concreto liso, então o `delogo` não vai gerar artefato visível mesmo passando por cima):
```bash
delogo=x=0:y=0:w=320:h=230:show=0:enable='between(t,21,63)'
```

### CONCEITTO (parte inferior da cena externa) — mais delicada
Essa marca está sobre uma área com textura (calçada de pedra) e a pessoa caminha perto dela em vários frames — um `delogo` simples vai borrar/manchar visivelmente porque a caixa muda de conteúdo a cada frame (a pessoa passa por cima/perto). Recomendo:

- **DaVinci Resolve** (Fusion → Object Removal / Magic Mask) — rastreia e reconstrói o fundo automaticamente, inclusive com movimento de câmera e do "objeto" (a marca é estática, mas o fundo atrás dela se move).
- **After Effects** (Content-Aware Fill, com um track mask na área do logo) — mesma lógica, boa opção se já usam Adobe.

Coordenada testada (2160×3840): `x=605 y=2918 w=864 h=576` (bloco do logo + texto "VENDAS · LOCAÇÃO · ADM"), sobre a mesa de madeira/mármore da cena do restaurante de praia (~t=5s).

### ✅ Decisão final: marca CONCEITTO **mantida** na cena externa

Sem DaVinci Resolve/After Effects disponíveis, e sem um arquivo isolado do logo da Conceitto (fundo transparente) neste repositório pra reaplicar em outro canto, testamos a remoção via `ffmpeg delogo` diretamente (preview com `show=1` em `t=5s`, superfície lisa da mesa). Resultado: reconstrução com listras/borrão bem visível — não passa no critério de qualidade definido.

**Conclusão (usuário validou o preview):** não forçar a remoção. A marca CONCEITTO permanece como está na cena externa (0–20s), do mesmo jeito que fica visível do início ao fim no vídeo do UP Vilas — funciona como assinatura de marca da imobiliária, e não como "erro" a ser corrigido.

Com isso, **não há mais processamento pendente na cena externa** nem no card final — o `Blue_etapa1.mp4` já reflete o estado definitivo de watermark.

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

Você decidiu rodar os comandos você mesmo. **Passo 1 (mapear os tempos) já foi concluído** via `contact_sheet.png` — o mapeamento está na seção 2 acima (externa 0–20s / transição 20–22s / interiores 22–63s / card final 64s+). Segue a partir do Passo 2:

### Passo 2 — ✅ Concluído (`Blue_etapa1.mp4`)
Grading aplicado, marca "CapCut AI" removida no bloco 21–63s, arquivo já convertido pra H.264. Conferido via `contact_sheet_v2.png`: cena externa e card final intactos, sem resíduo visível do delogo nos frames de baixa resolução — recomendado checar de perto em player (~24s, ~30s, ~48s, ~54s) antes de considerar definitivo.

Comando usado:
```bash
ffmpeg -i Blue_Final.mov -vf "\
delogo=x=4:y=4:w=316:h=226:show=0:enable='between(t,21,63)',\
eq=contrast=1.08:saturation=1.10:brightness=0.01,\
curves=preset=medium_contrast,\
unsharp=5:5:0.6" \
-c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
-c:a aac -b:a 192k \
Blue_etapa1.mp4
```
Confira o resultado antes de seguir — se a caixa do `delogo` estiver deixando um "quadrado" visível ou desalinhado, reajuste `x/y/w/h` e rode de novo (é rápido, o arquivo já está bem menor em H.264).

### Passo 3 — ✅ Concluído (marca CONCEITTO mantida)
Sem Resolve/AE instalados e sem logo isolado da Conceitto disponível, testamos remoção via `ffmpeg delogo` (preview `show=1` em t=5s, área `x=605 y=2918 w=864 h=576`). Resultado: reconstrução visivelmente borrada/com listras sobre a mesa lisa — não passou no critério de qualidade. **Decisão final: marca mantida como está** na cena externa (0–20s), mesma convenção do UP Vilas (assinatura de marca visível). Ver detalhes na seção 2.

### Passo 4 — Texto de compliance (imagens ilustrativas) — a cargo do usuário
Inserir o texto **"Imagem ilustrativa — decoração virtual"** sobreposto durante o bloco de interiores (22–63s). Fica por conta do usuário adicionar (ferramenta de sua escolha).

### Passo 5 — Exportação final
`Blue_etapa1.mp4` já está em H.264, 2160×3840, AAC 192kbps — dentro dos requisitos de Reels (duração ≤90s, 9:16, ≤4GB) validados na análise técnica anterior. Depois de inserir o texto de compliance (Passo 4), o vídeo está pronto para publicar.

Qualquer travamento nesses passos (comando dando erro, coordenada errada, resultado estranho), me manda o print/print do erro que eu ajusto o comando.

## Especificações técnicas do arquivo de origem
- Resolução: 2160×3840 (9:16, 4K vertical)
- Codec: HEVC (H.265), yuv420p, 60fps — recomendado converter para H.264 antes de publicar (ver análise técnica anterior)
- Duração: 65,97s · Tamanho: ~254MB
- Áudio original: AAC (sem locução — precisa da voz gerada no ElevenLabs)
