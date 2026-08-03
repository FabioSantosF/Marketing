# Campanha Instagram — Green Home (Julianne Costa, Consultora)

Material de campanha para a Julianne Costa ("Juli") divulgar o **Green Home** (DENA Realizações) no Instagram — condomínio fechado com 175 casas exclusivas em Abrantes, Lauro de Freitas/BA. Peças produzidas a partir do book, cartilha e implantação do empreendimento (pasta do Drive), usando a foto real dela como fio condutor da campanha, no mesmo padrão visual/editorial da campanha do UP Vilas já publicada neste repositório.

## Conceito criativo: "Onde a vida floresce"

O Green Home já nasce com uma identidade forte de marca (verde + "assinatura de excelência"), então a campanha assume esse território de forma literal: paleta verde-floresta profunda com dourado, um traço orgânico de folhas ao fundo (em vez das linhas retas/urbanas do UP Vilas) e uma narração real guiando o ritmo do vídeo — captions embutidas para quem assiste mudo, locução para quem assiste com som.

Assim como no UP Vilas, a Juli entra só no card final do vídeo: o imóvel fala primeiro (natureza, segurança, números), a corretora aparece por último para fazer o convite pessoal.

## O que foi gerado

| Peça | Arquivo | Formato | Uso |
|---|---|---|---|
| Vídeo teaser (com locução) | `video/green-home-teaser-reels.mp4` | 1080×1920, 29.5s, MP4 (H.264 + AAC) | Reels / Stories |
| Post de feed | `imagens/feed-post.png` | 1080×1350 (4:5) | Feed |
| Capa do Reels | `imagens/reels-cover.png` | 1080×1920 | Capa/thumbnail do Reels |
| Story 1 — Hook | `imagens/story-1-hook.png` | 1080×1920 | Stories (parte 1/3) |
| Story 2 — Benefícios | `imagens/story-2-beneficios.png` | 1080×1920 | Stories (parte 2/3) |
| Story 3 — CTA | `imagens/story-3-cta.png` | 1080×1920 | Stories (parte 3/3, com enquete) |

Legendas e hashtags prontas: `copy/legendas-e-hashtags.md`
Roteiro/storyboard cena a cena do vídeo (com timecodes da locução): `video/roteiro.md`
Locução original (IA, PT-BR): `video/audio-fonte/green-home-locucao.mp3`

## Por que essa direção funciona para o nicho

- **Locução real + legenda embutida** — o vídeo é 100% legível mudo (85% dos Reels são assistidos sem som) e ainda soa como um convite pessoal para quem ouve.
- **Cortes cronometrados pela fala, não no chute** — usei detecção de silêncio no áudio (`ffmpeg silencedetect`) e cravei cada troca de cena exatamente nas pausas de respiração da locução.
- **Números como personagem** — "175 casas" e "3.700m² de lazer" entram como contador animado (0 → valor final), não como bullet de ficha técnica.
- **A consultora aparece por último, não primeiro** — mesmo recurso do UP Vilas: gera curiosidade até o closing e reforça que existe uma pessoa real por trás do empreendimento.
- **Sistema visual consistente com a marca-mãe (DENA)** — mesma tipografia (Playfair Display + Montserrat) e estrutura de campanha do UP Vilas, mas com paleta e motivo gráfico próprios do Green Home (verde/folhas em vez de preto/onda), para não confundir os dois lançamentos no feed.

## Como publicar (ordem sugerida)

1. **Reels** com `green-home-teaser-reels.mp4` + capa `reels-cover.png` definida manualmente no Instagram.
2. **Stories** no dia seguinte: `story-1-hook.png` → `story-2-beneficios.png` → `story-3-cta.png` em sequência. Ativar o sticker de **enquete nativa** do Instagram por cima do quadro "Quer conhecer o Green Home?" no story 3 (espaço já reservado).
3. **Feed** com `feed-post.png`, legenda longa (ver arquivo de legendas) fixando as informações completas + CTA para o direct da Juli.

## Dados reais usados (fonte: Drive do empreendimento)

- Condomínio fechado, **175 casas exclusivas**, em duas etapas de construção
- Casas de 96m² internos + quintal privativo de 86 a 210m², 3 ou 4 suítes
- Infraestrutura para energia solar, split e carregamento de carro elétrico
- **3.700m²** de área de lazer: piscina com raia de 28m, piscina infantil e "prainha", quadra de beach tennis/futevôlei, campo de futebol, pet place, academia, espaço yoga, parque infantil, brinquedoteca, salão de festas com varandão, lounge gourmet, sport bar
- Segurança: portaria 24h, guarita com clausura, vagas para visitantes
- Endereço: Abrantes, ao lado do Colégio Villa Global Education (próximo a Via Metropolitana, Grecos, Linha Verde BA-099, Busca Vida, shopping)
- Valores: a partir de **R$ 638.800**, financiamento em até 100% pela Caixa, sem entrada, uso do FGTS (sujeito a análise de crédito/aprovação CEF)
- Incorporação: DENA Realizações · Alvará de construção nº 375/2025 · Registro em Camaçari sob matrícula nº 63.281

## Sobre a foto da consultora usada no vídeo e nos cards

As peças usam a foto real da Juli de blazer/social que você enviou — **sem qualquer alteração de rosto, pele, cor, cabelo, olhos, nariz ou boca**, e também sem gerar roupa por IA: é a foto original dela mesma, só recortada do fundo e recomposta nas artes. Optei por essa foto (em vez da primeira, de blusa vermelha) por já trazer o visual de corretora de imóveis de alto padrão que você pediu, com qualidade totalmente fotográfica — sem depender de nenhuma edição sintética.

## Suposições que fiz (me avise se algo estiver errado)

- O crachá/assinatura usa o nome completo **Julianne Costa**; o restante das legendas mantém o apelido **"Juli"**, no tom mais pessoal de quem fala direto no Instagram.
- Mantive o contato da **Conceitto Imóveis** (@conceittoimoveis, (71) 98855-1313, conceittoimoveis.imb.br) usado na campanha do UP Vilas neste mesmo repositório — confirmado que é o número certo.
- Não encontrei um arquivo de logo oficial da Conceitto no Drive, então reconstruí a marca (ícone de casa + "CONCEITTO imóveis") a partir do padrão visual usado na campanha anterior. Se você tiver o arquivo de logo oficial, eu troco pela versão exata.

## Próximos passos / limitações a saber

- A locução foi gerada por IA (ElevenLabs, voz feminina PT-BR) a partir de um roteiro com os dados reais do empreendimento — não é uma gravação humana. Se preferir, posso trocar por uma locução enviada por vocês (como foi feito no UP Vilas) ou testar outra voz.
- As imagens/vídeo foram renderizados em alta resolução (1080px de largura), prontos para upload direto no Instagram, sem perda de qualidade.
- Posso gerar variações adicionais: carrossel de plantas (casa de 3 e 4 suítes já estão no book), stories extras por área de lazer, ou uma versão do vídeo com trilha sonora em vez de locução.
