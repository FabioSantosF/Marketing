# Campanha Instagram — Dízimo (Paróquia São João Evangelista)

Carrossel de feed + sequência de stories para a campanha do dízimo da Paróquia São João Evangelista de Vilas do Atlântico (Arquidiocese de São Salvador da Bahia), a partir das fotos reais da paróquia (celebrações, crisma e imagens do altar).

## Conceito

**"Seu dízimo se transforma em vida e missão."** — em vez de pedir a contribuição de forma genérica, cada peça mostra *onde* o dízimo vira ação concreta: liturgia e sacramentos, catequese/crisma, pastoral social, evangelização e missão, e manutenção da paróquia. O fechamento reforça a frase-chave da campanha: **"Com o seu dízimo, fazemos muito mais!"**

## Identidade visual

Mantida a mesma linguagem já usada nas peças anteriores desta conta: fundo preto, tipografia **Playfair Display** (serifada, com itálico dourado para as palavras de destaque) combinada com **Montserrat** (caixa-alta, letter-spacing largo, para rótulos e pills), linha fina dourada como divisor, pills contornadas para os tópicos e um selo/wordmark da paróquia no canto superior esquerdo. Paleta: preto (#0b0b0c), dourado (#c9a24d / #e6c777) e off-white (#f6f1e6).

## O que foi gerado

| Peça | Arquivo | Formato | Uso |
|---|---|---|---|
| Carrossel 1 — Capa | `imagens/feed-01-capa.png` | 1080×1350 (4:5) | Feed (slide 1/5) |
| Carrossel 2 — Liturgia | `imagens/feed-02-liturgia.png` | 1080×1350 | Feed (slide 2/5) |
| Carrossel 3 — Catequese | `imagens/feed-03-catequese.png` | 1080×1350 | Feed (slide 3/5) |
| Carrossel 4 — Comunidade | `imagens/feed-04-comunidade.png` | 1080×1350 | Feed (slide 4/5) |
| Carrossel 5 — CTA | `imagens/feed-05-cta.png` | 1080×1350 | Feed (slide 5/5) |
| Story 1 — Hook | `imagens/story-1-hook.png` | 1080×1920 | Stories (parte 1/3) |
| Story 2 — Benefícios | `imagens/story-2-beneficios.png` | 1080×1920 | Stories (parte 2/3) |
| Story 3 — CTA | `imagens/story-3-cta.png` | 1080×1920 | Stories (parte 3/3) |

Fontes de imagem originais (enviadas pelo usuário): `fotos-base/`
Código-fonte editável de cada card (HTML/CSS) e script de renderização: `html/`

## Como publicar

1. **Feed**: publicar como carrossel único, na ordem `feed-01` → `feed-05`, com a legenda de `copy/legenda-feed.md`.
2. **Stories**: postar em sequência `story-1-hook` → `story-2-beneficios` → `story-3-cta` no mesmo dia ou no dia seguinte ao carrossel, linkando (sticker de link/adesivo "Perguntas" ou "Link") para o contato da secretaria paroquial.

## Como editar/regenerar as peças

As peças são HTML/CSS renderizados via Playwright (Chromium headless) — não são arquivos de design binário, então qualquer texto pode ser editado direto no HTML:

```bash
cd campanha-dizimo/html
# edite os arquivos feed-*.html / story-*.html conforme necessário
NODE_PATH=/opt/node22/lib/node_modules node render.js
```

O script regenera todas as 8 imagens em `imagens/` a partir dos HTMLs em `html/`, usando as fotos de `fotos-base/`.

## Observações

- O nome da paróquia e a localização ("São João Evangelista · Vilas do Atlântico", "Arquidiocese de São Salvador da Bahia") foram identificados a partir da camiseta visível em uma das fotos enviadas — confirme se está correto antes de publicar.
- O CTA usa "Fale com a secretaria paroquial" por não termos um @ ou contato específico informado; se a paróquia tiver Instagram, WhatsApp ou PIX próprios para o dízimo, me diga que eu atualizo os cards com esse dado.
