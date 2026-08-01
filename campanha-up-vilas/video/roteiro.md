# Roteiro — Teaser Reels "Mude de perspectiva" (20.5s · 1080×1920 · 24fps · com áudio)

Vídeo com a locução `audio-fonte/up-vilas-locucao.mp3` sincronizada, legenda embutida na tela (captions-first, então continua 100% legível mesmo mudo). Todos os textos usam frases originais do book do UP Vilas. Ritmo calibrado para dar tempo confortável de leitura em cada cena.

## Sobre a sincronização de áudio

A locução enviada tem 20,506s — muito próxima da v2 do vídeo (21s). Rodei uma detecção de silêncio (`ffmpeg silencedetect`) no áudio para localizar as pausas de fala e recalibrei a duração de cada cena proporcionalmente para que o vídeo comece e termine exatamente junto com o áudio, mantendo o ritmo de leitura já validado. Não temos uma transcrição palavra-por-palavra da locução neste ambiente, então o encaixe é "por proporção + pausas maiores detectadas", não lip-sync exato — se algum corte específico não bater com a fala ao assistir, me diga o timestamp que eu ajusto manualmente aquele trecho.

| Tempo | Cena | Tela | Observação |
|---|---|---|---|
| 0:00–2:36 | 1 | Fundo preto, tipografia branca entra palavra a palavra: **"Não se trata de ir além."** (última palavra em dourado) | Hook — corta o padrão de "vídeo de imóvel" tradicional |
| 2:36–5:12 | 2 | **"Trata-se de estar exatamente onde deveria."** (destaque em dourado) | Reforça a segunda parte da frase-manifesto da marca |
| 5:12–8:00 | 3 | **"Entre o horizonte e a cidade,"** / **"um novo ponto de vista."** (itálico dourado) + onda dourada animada + pin **"Miragem · Lauro de Freitas"** | Introduz localização de forma poética, não burocrática |
| 8:00–10:12 | 4 | Contador **0 → 39** + **"UNIDADES · TORRE ÚNICA"** | Número como personagem visual |
| 10:12–12:24 | 5 | Contador **0% → 100%** + **"APARTAMENTOS NASCENTES / luz da manhã, todo dia."** | Reforça diferencial técnico real (todos nascentes) |
| 12:24–15:60 | 6 | Foto da Juli entra em zoom sutil, balão **"Deixa eu te mostrar."**, crachá **"Juli · Corretora de imóveis"** | Vira o vídeo de "sobre o imóvel" para "sobre a pessoa que atende" |
| 15:60–21:00 | 7 | **Card final** (5.4s, o mais longo de propósito): logo **UP Vilas** + **"Assinatura de excelência."** → linha divisória → **logo da Conceitto Imóveis em destaque** → canais de contato revelados um a um: **@conceittoimoveis** (Instagram), **+55 71 98855-1313** (WhatsApp), **conceittoimoveis.imb.br** (site) | Encerramento/CTA — tempo generoso para o espectador anotar ou printar o contato |

Marca d'água da Conceitto (canto inferior direito) presente do início ao fim do vídeo, além de aparecer em destaque, ampliada, no card final.

## Especificações técnicas
- Resolução: 1080×1920 (9:16, nativo Reels/Stories)
- Duração: 20.5s
- Vídeo: H.264 (yuv420p) · Áudio: AAC 192kbps (locução fornecida)
- Fonte: Playfair Display (headlines) + Montserrat (apoio/labels)

## Próximo ajuste fino (se necessário)
Se ao assistir algum corte de cena não bater exatamente com a locução, me passe o timestamp aproximado (ex: "aos 8s a cena devia mudar meio segundo antes") que eu recalibro só aquele trecho — o restante do vídeo já está pronto e não precisa ser re-renderizado inteiro.
