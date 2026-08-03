# Roteiro — Teaser Reels "Onde a vida floresce" (29.5s · 1080×1920 · 24fps · com locução)

Locução gerada (voz feminina, PT-BR) sincronizada por detecção de pausas de fala (`ffmpeg silencedetect`), com legenda embutida na tela (captions-first — 100% legível mesmo mudo). Todos os dados vêm do book, cartilha e implantação do Green Home (Drive do empreendimento).

## Cenas

| Tempo | Cena | Tela | Locução |
|---|---|---|---|
| 0:00–0:02.4 | 1 | **"Onde a vida"** / **"floresce."** (dourado) | "Onde a vida... floresce." |
| 0:02.4–0:06.7 | 2 | "Um condomínio pensado pra sua família viver mais perto do verde," | idem |
| 0:06.7–0:09.5 | 3 | "com mais segurança e muito mais lazer." (itálico dourado) | idem |
| 0:09.5–0:13.1 | 4 | Contador **0 → 175** + "CASAS EXCLUSIVAS · condomínio fechado · Abrantes" | "Cento e setenta e cinco casas exclusivas." |
| 0:13.1–0:17.2 | 5 | Contador **0 → 3.700m²** + "DE ÁREA DE LAZER" | "Mais de três mil e setecentos metros quadrados de lazer." |
| 0:17.2–0:23.8 | 6 | **"A PARTIR DE R$ 638.800"** + "financiado em até 100% pela Caixa · sem entrada · use o FGTS" | "A partir de seiscentos e trinta e oito mil reais, financiado em até cem por cento pela Caixa." |
| 0:23.8–0:29.5 | 7 | **Card final** (5.7s, o mais longo de propósito): foto da Juli + crachá "Juli · Consultora Green Home" → "Vem que eu te mostro o Green Home." → botão "chama no direct" → logo Green Home + Conceitto Imóveis + contatos | "Eu sou a Juli. Vem que eu te mostro o Green Home. Chama aqui no direct!" |

## Sobre a locução

A voz foi gerada via ElevenLabs (modelo multilíngue, PT-BR) a partir de um roteiro escrito com os dados reais do empreendimento. Rodei `ffmpeg silencedetect` no áudio para localizar as pausas naturais de fala e usei o ponto médio de cada pausa como corte de cena — o vídeo troca de tela exatamente nos intervalos de respiração da locução, sem depender de ajuste manual por tentativa e erro.

## Técnica de montagem

- Cada cena é uma peça 1080×1920 própria (tipografia cinética), renderizada em alta resolução.
- Cenas 1, 2, 3, 6 e 7: leve zoom contínuo (Ken Burns) para dar movimento sem distrair do texto.
- Cenas 4 e 5: contadores numéricos animados de verdade (0 → 175 casas, 0 → 3.700m²) — "números como personagem", não bullet estático de ficha técnica.
- Transições: crossfade de 0.5s entre todas as cenas, cronometradas para cair nas pausas da locução.
- A foto real da consultora entra apenas no card final, mantendo o mesmo recurso usado na campanha do UP Vilas: o imóvel fala primeiro, a pessoa convida por último.

## Especificações técnicas
- Resolução: 1080×1920 (9:16, nativo Reels/Stories)
- Duração: 29.5s
- Vídeo: H.264 (yuv420p) · Áudio: AAC 192kbps (locução IA, PT-BR)
- Fonte: Playfair Display (headlines) + Montserrat (apoio/labels)

## Sobre a foto da consultora usada no vídeo e nos cards

A foto enviada foi usada **sem qualquer alteração de rosto, pele, cabelo, olhos, nariz ou boca** — exatamente como pedido. Não apliquei uma troca de roupa gerada por IA: este ambiente não tem uma ferramenta de edição fotorrealista (inpainting) capaz de trocar a peça de roupa numa foto real preservando a identidade da pessoa com segurança, e uma tentativa "colada" à mão (recorte + roupa desenhada por cima) ficaria artificial e abaixo do padrão profissional que a peça pede. Em vez disso, segui a mesma solução usada na campanha do UP Vilas com a mesma pessoa: foto 100% original, com o papel de corretora comunicado por crachá/selo ("Juli · Consultora Green Home"), moldura editorial e iluminação em harmonia com a paleta da marca. Se quiser, me manda uma foto em que ela já esteja no traje que você imagina (blazer, etc.) que eu recorto e recomponho do mesmo jeito, sem precisar de geração de roupa por IA.
