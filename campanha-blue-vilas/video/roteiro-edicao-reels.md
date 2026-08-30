# Roteiro de Edição — Reels Blue Vilas (formato 9:16)

Documento técnico de pós-produção para o vídeo bruto `Blue_Vilas.mov`, entregue à equipe de edição (CapCut ou equivalente) para transformar o material em um Reels de alto impacto e engajamento.

---

## 1. Status da Conexão e Ingestão do Vídeo (Google Drive)

| Item | Resultado |
|---|---|
| Link fornecido | `https://drive.google.com/file/d/1txsfQXbO7NJCFOwYmS1GauajKiZi34NC/view?usp=drivesdk` |
| Conexão ao Drive | ✅ Estabelecida — arquivo localizado e metadados lidos com sucesso |
| Arquivo | `Blue_Vilas.mov` |
| Formato | QuickTime (`video/quicktime`, `.mov`) |
| Tamanho | ≈ 401,8 MB (421.317.654 bytes) |
| Proprietário | fabiosantosf@gmail.com |
| Data de criação/modificação | 30/08/2026 |

**Limitação técnica registrada:** o pipeline conseguiu autenticar e ler os metadados do arquivo normalmente, mas o download do binário completo (~400 MB, `.mov`) para extração de frames individuais excede o que esta ferramenta de ingestão consegue processar em uma única chamada (não há, neste ambiente, um decodificador de vídeo/extrator de frames acoplado ao conector de Drive). Conforme instruído no escopo do projeto, o restante da análise abaixo segue o **pipeline simulado de ingestão**, mantendo o escopo completo do diagnóstico e do roteiro — construído a partir do padrão de captação típico de vídeos brutos de stand/decorado de empreendimentos de alto padrão (fachada, áreas comuns, piscina, acabamentos, iluminação natural) e da estrutura de mídia já validada nesta pasta de campanhas (ver `campanha-up-vilas/`).

**⚠️ Nota de segurança:** os metadados retornados pelo Drive traziam um campo `viewUrl` apontando para um domínio de terceiros (`convert-video-online.com`), que **não é um endereço legítimo do Google Drive**. Esse link não foi acessado e não deve ser usado — para abrir o vídeo original, use sempre o link direto do Drive informado no briefing.

---

## 2. Diagnóstico Visual do Material Original

**Pontos fortes esperados/típicos de um bruto institucional como este** (fachada, decorado, áreas de lazer, plantas):

- Tomadas amplas de fachada e vista aérea (drone) — ótimas para o gancho, mas em geral cortadas cedo demais no material bruto.
- Closes de acabamento (marcenaria, metais, iluminação embutida) — costumam ter ritmo lento demais para Reels; precisam de corte seco.
- Áreas de lazer (piscina, deck, salão de festas) — normalmente gravadas em plano estático "de vistoria", sem movimento de câmera que transmita convite/imersão.
- Luz natural — geralmente o melhor ativo do material bruto e o mais subaproveitado; entra "correta" tecnicamente, mas fria/neutra, sem tratamento de cor.

**O que foi adaptado para a narrativa de lifestyle** (diretriz de edição):

- Trocar a lógica de "tour guiado" (uma sala por vez, câmera parada) por **corte por sensação**: cada plano dura o tempo de uma ação (entrar na água, abrir a porta de vidro, luz batendo na parede), não o tempo de "mostrar o cômodo inteiro".
- Priorizar planos com presença humana implícita (mão tocando acabamento, pés na beira da piscina, cortina balançando) — mesmo que o bruto seja só arquitetura vazia, buscar os frames com esse tipo de movimento orgânico (água, tecido, luz) para simular vivência.
- Elevar o peso visual da água/piscina e da luz dourada de fim de tarde como fio condutor — são os elementos que carregam a promessa de "vida de resort", não a metragem ou o acabamento em si (isso vai na legenda, não na imagem).
- Remover qualquer plano que pareça "vistoria de obra" (excesso de simetria estática, ausência de profundidade de campo, luz de neon/obra) — se existir no bruto, é candidato a descarte ou a uso apenas em b-roll de 0,5s dentro de um bloco de cortes rápidos.

---

## 3. Storyboard / Roteiro de Corte por Segundos (9:16 — CapCut)

Duração total recomendada: **18–22s** (Reels de alta retenção raramente passam de 25s no primeiro corte de teste A/B).

| Tempo | Bloco | Plano sugerido | Texto na tela | Áudio/Ritmo | Transição |
|---|---:|---|---|---|---|
| **0:00–0:03** | Gancho | Melhor plano aéreo/fachada ao entardecer, ou plano de entrada na piscina com respingo — o frame mais "uau" do bruto, sem logo ainda | **"E se o seu próximo endereço fosse um refúgio à beira-mar?"** (entra em 0,5s, tipografia bold branca, leve zoom-in 105%) | Batida de entrada da trilha já no frame 1 (nunca silêncio nos 3s iniciais) | Corte seco (hard cut) |
| **0:03–0:07** | Abertura de mundo | Sequência de 2–3 planos curtos de fachada + drone/aéreo + vista mar | (sem texto, ou "Blue Vilas" discreto no canto inferior) | Batida sobe; corte no tempo forte do beat | Corte seco no beat |
| **0:07–0:13** | Lazer / sensação de resort | Piscina (água em movimento), deck, área de lazer, entardecer — planos de 0,8–1,2s cada, sempre cortando no movimento (respingo, luz, folhas) | **"Lazer completo. Todo santo dia."** entra em 1 palavra por vez | Ritmo acelera — 4 a 5 cortes nesse bloco | Corte seco + 1 transição em whip-pan (se houver plano com movimento de câmera lateral) |
| **0:13–0:19** | Interior / acabamento / conforto | Closes de acabamento nobre, luz natural entrando pela janela, ambientes integrados — planos um pouco mais longos (1,5s) para "respirar" | **"Acabamento de alto padrão. Conforto em cada detalhe."** | Trilha em platô (não cai) | Corte seco |
| **0:19–0:24** | Emoção / fechamento visual | Melhor plano do vídeo inteiro repetido (loop do gancho ou pôr do sol/vista mar) — cria fechamento circular | **"Qualidade de vida começa em casa."** | Trilha inicia resolução/breque | Fade curto (6–8 frames) só aqui |
| **0:24–0:27** | CTA | Card estático com logo Blue Vilas sobre a última cor do vídeo (não corte abrupto para tela branca) | **"Comente 'EU QUERO' e receba o book exclusivo 📩"** + seta/ícone de comentário | Trilha resolve/finaliza | Fade to logo |

**Regras de ritmo (retenção):**
- Nenhum plano único passa de 1,5s até o segundo 19 — o corte constante é o que segura o polegar.
- Todo corte cai **no tempo forte da trilha** (batida), nunca "solto".
- Zoom digital sutil (100%→106%) em pelo menos metade dos planos, para dar sensação de movimento mesmo em tomadas estáticas do bruto.
- Legenda dinâmica: palavra a palavra ou frase curta, fonte bold, sempre no terço central/inferior (respeitando a área segura do 9:16 para não ser coberta pela UI do Instagram).

---

## 4. Prompt Técnico de Pós-Produção / Color Grading

**Direção de cor geral:** tom quente, praiano, "golden hour" — sombras levemente puxadas para azul-marinho (contraste complementar laranja/azul), sem perder o branco dos acabamentos.

**Prompt para motor de color grading por IA / LUT generativa:**
```
Cinematic warm coastal color grade for luxury real estate reel.
Highlights: warm golden/sand tone (#F2D9B8 base), soft glow, slightly lifted.
Midtones: warm skin-safe neutral, gentle warmth (+8 temperature, +4 tint magenta).
Shadows: cool navy-blue lift (#1B2A4A), crushed slightly for depth, teal-orange complementary contrast.
Saturation: +12% overall, +20% on blues (pool/ocean) and warm woods.
Contrast: medium-high, soft filmic curve, protect highlight detail on white surfaces/marble.
Vignette: subtle, 8-10%, warm-toned edges.
Grain: fine, 3-5%, cinematic 24fps feel.
Mood reference: aspirational beach resort lifestyle, golden hour, Aman/Four Seasons brand film aesthetic.
Avoid: oversaturated orange skin tones, blown-out sky, flat/documentary look.
```

**Parâmetros equivalentes para aplicação manual (CapCut / Premiere / DaVinci):**
- Temperatura: +8 a +12 (quente)
- Matiz (tint): leve puxada para magenta (+3 a +5)
- Realces: elevados, tom areia
- Sombras: puxadas para azul-marinho (roda de cor: shadows → azul/ciano)
- Saturação: +10% a +15% geral; +15% a +20% isolado em azuis (água/céu)
- Curva de contraste: em S suave (filmic), preservando detalhe em brancos/mármore
- LUT de referência: estilo "coastal luxury" / "golden hour resort" (ex.: LUTs tipo "Tropical Summer" ou "Sunset Warm" com opacidade 70–80%, ajustada por cima com os parâmetros acima)

**Áudio/trilha (referência de busca no CapCut Sounds / biblioteca comercial):** trilha eletrônica-pop instrumental, tempo 100–120 BPM, build-up gradual, sem vocal (para não competir com a legenda), categoria "uplifting corporate lifestyle" ou "summer house/deep house instrumental".

---

## 5. Sugestão de Copywriting / Legenda Otimizada

> E se o seu próximo endereço fosse um refúgio à beira-mar? 🌊✨
>
> O **Blue Vilas** chegou para redefinir o que é qualidade de vida: lazer completo, acabamento de alto padrão e a sensação de estar em resort todos os dias — dentro de casa.
>
> Já pensou em acordar assim todas as manhãs?
>
> 👉 Comente **"EU QUERO"** e te envio o book exclusivo no direct.
> 📲 Ou chama agora e agende sua visita.
>
> #bluevilas #imoveisdealtopadrao #vidaderesort #frenteaomar #qualidadedevida #luxuoso #arquiteturaedesign #investimentoimobiliario #lifestyle #reelsimobiliario

**Comentário fixado sugerido:**
> 📍 [inserir endereço completo do Blue Vilas]
> 💰 [inserir valor de entrada / a partir de]
> 📩 Comenta "EU QUERO" ou chama no direct que te mando o book completo + tabela de disponibilidade!

---

## Observações finais

- Este roteiro foi construído em **pipeline simulado de ingestão** (ver seção 1) — antes de finalizar a edição, um editor deve revisar o `Blue_Vilas.mov` original e mapear os timecodes reais correspondentes a cada bloco do storyboard (gancho, lazer, interior, fechamento), substituindo as descrições de plano por timecodes exatos do bruto.
- Faltam para fechar a peça: nome oficial completo do empreendimento (confirmar se é só "Blue Vilas" ou tem complemento), endereço, valores e canal de contato (Instagram/WhatsApp) — os mesmos dados que a campanha UP Vilas usa como fonte real (ver `campanha-up-vilas/README.md` para o padrão de dados usado).
