# Portfólio Editorial de Lifestyle — Blue Vilas (DENA Realizações)

Tratamento de imagem e estratégia de conteúdo para transformar o book bruto da visita técnica do dia **29/08/2026** em uma campanha de Instagram (Reels/Stories/Feed) com estética de **estilo de vida e qualidade de vida** — nunca de classificado imobiliário.

Fonte: pasta do Google Drive `29082026` (dentro de `Imóveis/Blue`) — [link original](https://drive.google.com/drive/folders/1oAO5lId36fTZ0zgGfVCcgOzUrnFTcPz8).
Empreendimento: [Blue Vilas — DENA Realizações](https://www.denarealizacoes.com/bluevilas).

> **Nota de acesso:** a página oficial do empreendimento está bloqueada para leitura automática neste ambiente (proxy de rede). As metragens por tipologia foram confirmadas diretamente pelas plantas oficiais enviadas pelo gestor (seção 9) — mas **valores de venda e nº total de unidades ainda não foram confirmados** e seguem fora da copy para não inventar números. Antes de publicar, confirme esses dados restantes com o cliente, como foi feito na campanha UP Vilas (ver `campanha-up-vilas/README.md`).

---

## 1. Auditoria do lote (Varredura)

A pasta contém **64 arquivos**, todos gerados na mesma visita, sem subpastas:

| Tipo | Qtd. | Natureza | Uso recomendado |
|---|---|---|---|
| `.DNG` (RAW) | 30 | Fotos de câmera profissional — fachada, jardim, piscina | Fonte principal do tratamento de imagem/feed |
| `.JPG` | 12 | Fotos rápidas (celular) — piscina em ângulos baixos e 2 retratos de pessoa | Boas candidatas a "hero shot" por já terem enquadramento espontâneo |
| `.MOV` | 22 | Vídeos brutos (clipes de poucos segundos) | B-roll para um teaser/Reels futuro — **não tratado neste documento**, é outra frente de trabalho |

**Diagnóstico geral, antes de qualquer tratamento:**
- Todas as fotos foram batidas em **luz dura de meio-dia** (sombras fechadas, céu estourado em algumas), o que precisa ser corrigido no grading.
- O lote cobre bem **jardim/paisagismo** e **piscina/área comum**, e tem **2 fotos de pessoa** (boas para "persona" da campanha).
- **Não há**, nesta leva, nenhuma foto de **vista para o mar**, **interior decorado** ou **fachada frontal completa do prédio** — o material de hoje é essencialmente "área de lazer + jardim + retrato". Alerta ao gestor: se a campanha quer explorar "vista mar" e "sofisticação de interiores" como prometido no posicionamento, **é necessário agendar uma nova captura** (idealmente no fim de tarde, para o pôr do sol) só com isso — nenhuma imagem deste lote deveria ser forçada a simular uma vista que não existe.
- Ainda há elementos de "obra recém-entregue" recorrentes: tela de proteção verde em volta das mudas, placa de aviso regulamentar azul junto à piscina, fiação/postes ao fundo em quase todos os externos, grama com manchas irregulares.

---

## 2. Look & Feel unificado — "Blue Vilas"

Paleta e regras aplicadas em **todos** os prompts abaixo, para garantir coesão de campanha:

- **Paleta:** Ouro Acolhedor (highlights e pele) + Azul Praiano/Turquesa (água e céu) + Branco Puro (fachada e acabamentos).
- **Temperatura:** leve viés quente (+150 a +300K sobre o original), nunca frio/acinzentado.
- **Contraste:** mid-contraste suave, sombras abertas (evitar "preto chapado" de foto de obra).
- **Saturação seletiva:** verde da vegetação e azul-turquesa da água puxados para cima; branco da fachada mantido limpo, sem puxar para amarelo.
- **Remoção padrão:** fiação elétrica, telas de proteção de mudas, placas regulamentares, sujeira/poeira de obra, carros/entulho quando aparecerem.
- **Enquadramento:** recorte 4:5 vertical, regra dos terços, sempre reservando espaço negativo (céu, água ou parede lisa) para a copy entrar por cima.
- **Estilo fotográfico de referência:** editorial de revista de arquitetura/lifestyle costeiro, luz de golden hour, profundidade de campo rasa em still-lifes.

---

## 3. Seleção tratada

### 🌿 IMG_9017.JPG (RAW: IMG_9017.DNG equivalente)
**Diagnóstico de Lifestyle:** boa moldura natural de palmeiras + fachada, mas sol de meio-dia cria sombras duras e a tela verde de proteção das mudas (canto esquerdo) e a grama com manchas amarelas denunciam "obra recém-entregue". Falta um elemento de convite (não há pessoa nem objeto de uso).
**Prompt Técnico:**
```
Editorial real estate lifestyle photography, ground-floor garden of a modern beachside residential building, tall areca palms and ornamental grass beds in soft golden-hour side light, warm inviting tones with lush uniform emerald lawn, clean white and taupe facade with dark wood slat accent walls, remove any green plastic tree-guard netting and construction mesh, even out patchy yellow grass to a uniform manicured lawn, subtle shallow depth of field, warm color grade (gold + turquoise + pure white palette), no visible power lines, vertical 4:5 composition with negative space in the upper third for text overlay, shot on 35mm full-frame, natural light, high-end architecture magazine style --ar 4:5
```
**Copy:** "O verde que te recebe antes mesmo da porta de casa. 🌿"

---

### 🌊 IMG_9061.JPG — *hero shot de piscina*
**Diagnóstico de Lifestyle:** o ângulo baixo e o céu azul saturado já são o ponto alto do lote — só precisa de "humanização". A placa de aviso regulamentar quebra a imersão e a água, embora limpa, está sem nenhum elemento de uso (toalha, copo, pessoa).
**Prompt Técnico:**
```
Cinematic lifestyle photography, ultra-low ground-level angle at the edge of a condominium pool, rippling turquoise water filling the bottom third of the frame, sun loungers and a wood-clad pool bar pavilion softly out of focus in the background, deep saturated blue sky with a single soft cloud, warm golden light grading, remove or blur out the regulatory signage board, add a folded white towel or a chilled glass of water resting on the pool edge for a lived-in feel, vertical 4:5 aspect ratio, generous negative space in the sky for a headline, architectural-digest poolside editorial style --ar 4:5
```
**Copy:** "Aqui, o dia começa com o som da água e o cheiro do mar. 🌊"

---

### 🌴 IMG_9034.JPG
**Diagnóstico de Lifestyle:** já tem a melhor profundidade de campo do lote (folhagem nítida, piscina desfocada ao fundo) — só precisa de saturação e limpeza da parede, que tem leve sujeira de obra.
**Prompt Técnico:**
```
Close-up lifestyle detail shot, lush green tropical palm frond and trailing ivy in sharp focus in the foreground, a sparkling turquoise swimming pool and glass balustrade softly blurred in the background (bokeh), warm natural daylight, boost foliage saturation to vibrant emerald green, clean the rendered wall of any construction dust or staining, dreamy shallow depth of field, vertical 4:5 crop, soft airy highlights, botanical-meets-coastal-architecture editorial mood --ar 4:5
```
**Copy:** "Qualidade de vida é ter a natureza como vizinha. 🌴"

---

### ✨ IMG_8987.JPG (celular)
**Diagnóstico de Lifestyle:** expressão espontânea e luz suave de varanda coberta já entregam o "aspiracional" — mas há um letreiro cortado ilegível ("…ALÃO") ao fundo, que precisa sumir, e o ambiente ainda tem cara de condomínio recém-entregue e vazio.
**Prompt Técnico:**
```
Editorial lifestyle portrait, warm candid smile, soft natural window light on a covered veranda of a modern coastal residential building, remove or replace the incomplete signage text visible in the background with a softly blurred ornamental plant, warm golden-hour color grade with soft natural skin tones, glass-and-steel railing with a tropical plant out of focus, vertical 4:5 composition, negative space to the side for a short caption, aspirational real-estate lifestyle magazine photography --ar 4:5
```
**Copy:** "O sorriso de quem já sabe: encontrou o lugar certo pra viver. ✨"

---

### 🏆 IMG_9036.JPG — *hero shot da campanha*
**Diagnóstico de Lifestyle:** o melhor enquadramento espontâneo do lote inteiro — perfil, riso genuíno, luz de fim de manhã, palmeiras emolduram o prédio e a piscina aparece desfocada ao fundo. Only problem: fiação/poste elétrico atrás e um muro amarelo de terreno vizinho quebram a composição premium.
**Prompt Técnico:**
```
Aspirational lifestyle portrait, woman in profile laughing warmly outdoors, soft natural daylight, tropical palm fronds framing a modern white residential tower with a glimpse of a turquoise pool softly blurred in the background, retouch out overhead power lines and utility poles, replace the plain neighboring wall with soft green foliage bokeh, warm golden color grade (gold + turquoise + white palette), vertical 4:5 crop with negative space on the left for a headline, shallow depth of field, shot like a high-end coastal real-estate campaign --ar 4:5
```
**Copy:** "Sua vida dos sonhos começa aqui. Bem-vindo(a) ao Blue Vilas."

---

## 4. Duplicatas — uso racional (evitar feed repetitivo)

`IMG_9059.JPG`, `IMG_9060.JPG`, `IMG_9062.JPG` e `IMG_9063.JPG` são **variações do mesmo tripé/ângulo** que gerou o hero shot `IMG_9061.JPG` (mesma piscina, mesmo pilar, mesma luz). Publicar as cinco no feed cansaria o algoritmo e o público.

**Recomendação:**
- Manter só `IMG_9061.JPG` no Feed/Reels cover.
- `IMG_9059.JPG` pode virar o 2º card de um carrossel (ângulo ligeiramente mais aberto, mostra a curva branca do prédio) — mesmo prompt/paleta do item acima.
- `IMG_9060.JPG`, `IMG_9062.JPG` e `IMG_9063.JPG` → arquivar como bastidores/Stories de "making of", não usar em peças principais.

---

## 5. Alerta anti-sycophancy — imagem descartada

### ❌ IMG_9030.JPG
**Motivo do descarte:** a paleta desta foto (parede em tom vinho/bordô e bege quente) **destoa de toda a paleta branco/turquesa** do restante do lote — sugere ser um ângulo de fachada de serviço, área técnica ou prédio vizinho, não a fachada principal do Blue Vilas. A composição também é central e sem profundidade, com o fundo estourado de luz. **Não deve entrar na campanha de lifestyle** sem confirmação do gestor sobre a origem da imagem.

**Prompt sintético de substituição** (para gerar um equivalente que mantenha a mesma função narrativa — "detalhe de palmeira ornamental" — sem herdar o problema de cor):
```
Generate a synthetic botanical detail shot in the campaign's editorial style: a single elegant Phoenix roebelenii palm in a clean white planter box, set against a softly blurred modern white coastal building facade, warm golden-hour light, a sliver of turquoise pool visible in soft bokeh behind it, vertical 4:5 crop, lush green fronds in sharp focus, gold + turquoise + white palette, botanical lifestyle editorial photography --ar 4:5
```

---

## 6. Material não tratado nesta rodada

- **22 vídeos `.MOV`** da mesma visita são um ótimo B-roll bruto para um teaser de Reels (mesma lógica de tratamento de cor deve ser aplicada em edição de vídeo depois) — recomendo tratar como uma segunda frente, nos moldes do que foi feito em `campanha-up-vilas/video/`.
- **25 arquivos `.DNG`** não abertos nesta rodada (o lote tem 30 ao todo) — mostraram, pela amostra revisada, o mesmo padrão de jardim/fachada/piscina em ângulos semelhantes. Se o gestor quiser o tratamento completo do lote (e não só a curadoria das melhores), aplico a mesma metodologia acima em lote completo.

---

## 7. Sequência de publicação sugerida

1. **Feed:** `IMG_9036.JPG` (retrato) como carrossel de abertura + `IMG_9061.JPG` (piscina) como 2º card + `IMG_9017.JPG` (jardim) como 3º card. Legenda longa com o posicionamento de "qualidade de vida".
2. **Reels cover:** `IMG_9061.JPG` tratado, com título curto sobreposto no espaço negativo do céu.
3. **Stories:** `IMG_8987.JPG` (retrato varanda) → `IMG_9034.JPG` (detalhe folhagem) → `IMG_9059.JPG` (piscina, variação) em sequência, fechando com CTA para o direct.

## 8. Próximos passos

- Confirmar com o gestor se **IMG_9030.JPG** é do Blue Vilas antes de descartá-la definitivamente.
- Agendar captura de **vista mar / pôr do sol / interior decorado** — ausentes neste lote e centrais ao posicionamento "à beira-mar".
- Se aprovado o direcionamento, os prompts acima estão prontos para uso em Midjourney/DALL·E ou em ferramentas de retoque (Photoshop generative fill) — posso também gerar as versões renderizadas de 1–2 destas imagens como prova de conceito antes do lote completo, caso queira validar o estilo primeiro.

---

## 9. Plantas e metragens confirmadas

O gestor enviou as plantas oficiais das 3 tipologias do empreendimento (salvas em `plantas/`). O material já vem com a identidade visual da marca (faixa azul + abas douradas), então a base gráfica pode ser reaproveitada como está — só precisa de higienização de composição para virar peça de carrossel de Feed, e não "print de corretora".

> **Divergência a confirmar:** a mensagem que acompanhou os arquivos citava "TIPO GARDEN II", mas as 3 imagens recebidas mostram as mesmas 3 abas — **TIPO GARDEN I, TIPO I e TIPO II** — sem nenhuma tela de "Garden II". Se existir de fato uma 4ª tipologia, falta o arquivo dela.

| Tipologia | Suíte Master | Suíte II | Sala Integrada | Varanda Gourmet | Lavabo | Banheiros (Master / Suíte II) | Área Técnica | Jardim privativo |
|---|---|---|---|---|---|---|---|---|
| **Garden I** (térreo, com jardim) | 16,1 m² | 9,1 m² | 23,8 m² | 13,0 m² | 1,5 m² | 3,3 m² / 3,3 m² | 1,1 m² | **48,06 m²** (deck + gramado + espreguiçadeiras) |
| **Tipo I** (andar-tipo, sem jardim) | 16,1 m² | 9,1 m² | 23,8 m² | 13,0 m² | 1,5 m² | 3,3 m² / 3,3 m² | 1,1 m² | — |
| **Tipo II** (planta alternativa) | 14,0 m² | 9,4 m² | **29,8 m²** | 13,7 m² | 1,5 m² | 3,2 m² / 3,2 m² | 1,7 m² | — |

Leitura rápida para a copy: **Garden I** é a tipologia "casa com quintal" (jardim privativo de 48 m², melhor para família/pet); **Tipo I** é o mesmo layout em andar alto (melhor para quem quer varanda com vista); **Tipo II** troca metragem de quarto por uma sala 25% maior (23,8 → 29,8 m²) — ótimo ângulo para "vida social em casa".

**Prompt Técnico (tratamento das 3 peças de planta, mesmo grid para as três):**
```
Clean up this architectural floor plan graphic for a premium real-estate Instagram carousel: keep the existing brand navy-blue header band and gold/blue pill tabs exactly as designed, sharpen the top-down furniture render lines, unify the wood, marble and fabric textures to warmer tones matching a gold + turquoise + white brand palette, add soft drop-shadow depth so the plan reads as a premium 3D isometric render rather than a flat blueprint, keep all room labels and square-meter callouts fully legible, crop to a clean 4:5 vertical card with even white margin, no watermark clutter --ar 4:5
```

**Sugestões de copy para o carrossel de plantas:**
- Garden I: "Sua casa, seu quintal. 48 m² de jardim só seus. 🌿"
- Tipo I: "Mesmo conforto, com a cidade e o mar aos seus pés."
- Tipo II: "Uma sala de 29,8 m² pensada pra reunir quem você ama."

---

## 10. Cards prontos para Stories (com marca d'água Conceitto)

A partir da seleção da seção 3, gerei cards finais em `stories/` (1080×1920, formato Stories/Reels), já com color grading aplicado, copy sobreposta e a logo da **Conceitto Imóveis** como marca d'água — prontos para postar em sequência. O lote 1 (5 cards) já estava aprovado; o lote 2 (6 cards) veio da auditoria completa do restante das fotos da visita (seção 11).

**Sem nenhuma UI falsa do Instagram**: a primeira versão simulava a barra de progresso, o `@conceittoimoveis` e a localização no topo, mas isso é exatamente o que o próprio app já desenha por cima ao publicar (foto de perfil, nome da conta, stickers) — então duplicava e ficava por cima da interface real. Os cards atuais só têm a foto tratada, a copy e a marca d'água — o resto o Instagram cuida sozinho.

| Arquivo | Cena | Papel na sequência |
|---|---|---|
| `story-1-hook.jpg` | Retrato (IMG_9036) | **Hook** — abre a sequência, prende o olhar |
| `story-2-paisagismo.jpg` | Jardim (IMG_9017) | Diferencial 1 — paisagismo |
| `story-3-natureza.jpg` | Folhagem + piscina (IMG_9034) | Diferencial 2 — natureza |
| `story-4-lazer.jpg` | Piscina (IMG_9061) | Diferencial 3 — lazer |
| `story-5-cta.jpg` | Retrato varanda (IMG_8987) | **CTA** — fecha com convite direto |
| `story-6-chegada.jpg` | Pessoa + fachada + piscina (IMG_9048) | Establishing shot — "chegada" ao condomínio |
| `story-7-vista-mar.jpg` | Vista do mar entre coqueiros (IMG_8965) | Diferencial 4 — vista mar (não existia no lote 1) |
| `story-8-varanda.jpg` | Vista da varanda (IMG_8955) | Diferencial 5 — varanda ⚠️ ver nota na seção 11 |
| `story-9-espaco-comum.jpg` | Lounge/coworking (IMG_8991) | Diferencial 6 — espaço comum |
| `story-10-academia.jpg` | Academia equipada (IMG_9015) | Diferencial 7 — academia |
| `story-11-lazer-cta.jpg` | Piscina + espreguiçadeira (IMG_9051) | **CTA 2** — fecha o lote 2 ⚠️ ver nota na seção 11 |

**Técnicas de engajamento aplicadas em cada card:**
- **Kicker curto em caixa alta** (ex.: "LAZER", "NATUREZA") antes da frase — cria hierarquia de leitura rápida, essencial num formato que some em segundos.
- **Frase de no máx. 2 linhas curtas** — Stories têm ~3-5s de atenção; textos longos derrubam a taxa de conclusão.
- **Gradiente escuro só na base** — preserva a foto quase inteira visível (o que vende o imóvel) e garante contraste de leitura sem tarja sólida.
- **Botão de CTA falso no último card** ("FALE COM A CONCEITTO") — deixa claro o próximo passo antes mesmo de a corretora colar o link/sticker de verdade por cima no app.
- **Marca d'água em chip translúcido**, não em tarja opaca — mantém a logo sempre legível em qualquer foto sem tampar a cena.

**Ao postar, use os recursos nativos do Instagram** (o card estático não faz isso sozinho):
- Adicionar o **sticker de link** ("Fale com a gente") ou o **sticker de enquete/pergunta** por cima do card 5 — aumenta drasticamente o alcance por engajamento direto.
- Adicionar o **sticker de localização** nativo "Blue Vilas" — só ele conta para o algoritmo de local (não dá pra simular isso no card).
- Publicar os 5 em sequência direta, sem intercalar com outros stories, para funcionar como uma narrativa contínua.

Script de geração: `scripts/make_stories.py` (Pillow).

---

## 11. Auditoria completa do lote (as 43 fotos)

A pedido do gestor, abri e avaliei individualmente **todas as 43 fotos** da pasta (31 RAW + 12 JPG — os 22 vídeos `.MOV` continuam fora de escopo, ver seção 6). Resultado:

### Entraram como cards novos (lote 2, seção 10)
- **IMG_9048.DNG** — a melhor "establishing shot" do lote inteiro: pessoa + fachada completa + piscina + jardim no mesmo quadro (exatamente o "pessoa contemplando a vista" pedido no briefing original). Havia 4 variações quase idênticas dela (IMG_9047, 9049, 9050) — usei só a melhor pose para não repetir.
- **IMG_8965.DNG** — a vista do mar que **não existia** no lote 1 (eu tinha sinalizado essa ausência na seção 1). Encontrada numa foto tirada de andar alto, coqueiros emoldurando a faixa de mar ao fundo.
- **IMG_8955.DNG** — vista da própria varanda para o quintal/rua.
- **IMG_8991.DNG** — espaço comum tipo lounge/coworking, já mobiliado (mesas, poltronas, TV) — o único ambiente interno do lote já pronto para foto sem precisar de mobília virtual.
- **IMG_9015.DNG** — academia já equipada (esteira, aparelhos, anilhas).
- **IMG_9051.DNG** — variação de piscina com espreguiçadeira em primeiro plano e as "vilas" (casas brancas) do entorno ao fundo — reforça o nome do empreendimento.

### ⚠️ Entraram, mas com uma limitação a saber
- **story-8 (varanda, IMG_8955)** e **story-11 (piscina, IMG_9051)**: ambas têm um **poste de fiação elétrica bem visível** no meio do quadro. O tratamento automático (Pillow) faz recorte, cor e texto, mas não remove objetos da cena — isso exige uma ferramenta de "generative fill" (Photoshop) ou geração por IA. Prompt pronto pra quem for finalizar:
  ```
  Remove the utility pole and overhead power lines from this photo, seamlessly filling the area with the matching sky/tree background, keep everything else in the frame unchanged, photorealistic result
  ```

### Fotos boas, mas que exigem mais que recorte/cor (não viraram card ainda)
- **IMG_8945.DNG** — a única foto de **fachada completa** do prédio (frontal, rua inteira) — mas com 2 carros estacionados ocupando todo o primeiro plano e fiação aérea cruzando o céu. Vale mais a pena uma geração por IA do que recorte, pra não "cortar" o prédio:
  ```
  Photorealistic real estate exterior photo: clean street view of this same white modern residential building facade, empty street with no parked cars, no overhead power lines, warm late-afternoon light, well-manicured landscaping at the entrance gate, vertical 4:5 crop --ar 4:5
  ```
- **IMG_8981.DNG / IMG_8982.DNG** — cobertura duplex já com piso e esquadrias prontos (não é "obra crua"), com vista da janela — mas totalmente **sem mobília**. Precisa de home staging virtual, não só color grading:
  ```
  Virtually stage this empty duplex penthouse living room: add a light neutral sofa, a round wood coffee table, a sheer curtain by the glass doors, and a floor lamp near the staircase, keep the existing marble floor, staircase, ceiling and window view exactly as is, warm natural light, photorealistic interior design magazine style
  ```

### Descartadas desta rodada (e por quê)
- **Grupo "piscina baixo ângulo" duplicado**: IMG_9059/9060/9062/9063/9064 (JPG) — 5 variações do mesmo tripé já coberto por `story-4` e pelo card extra `story-11`; mais uma delas só cansaria o feed (ver seção 4).
- **IMG_9042 / IMG_9043.DNG** — duas pessoas admirando o prédio de baixo, ângulo bem interessante, mas distorção de "olho de peixe" forte + poste de fiação cruzando o rosto das pessoas — pediria o mesmo retoque de remoção de poste acima **e** correção de perspectiva; fica como "banco" para uma próxima rodada se o gestor topar o retoque extra.
- **Áreas comuns ainda em obra** — sala de festas/kids (IMG_8990, 8998, 8999, 9001) e 2 unidades vazias com piso ainda em contrapiso bruto (IMG_8957, 8958): sem mobília e, nos dois últimos casos, sem acabamento — mais próximas de "canteiro de obra" do que de "desejo", não dá pra salvar só com color grading.
- **Fotos de equipamento de academia em close** (IMG_9011, 9012, 9013, 9014) — repetem `story-10` de ângulos mais fechados, com efeito "catálogo de produto" que o briefing pediu pra evitar.
- **Escada de serviço** (IMG_9004) — área puramente funcional, sem apelo de lifestyle.

Vídeos (`.MOV`) seguem fora desta rodada — ver seção 6.
