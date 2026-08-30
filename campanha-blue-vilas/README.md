# Campanha Instagram — Blue Vilas

Reels de divulgação do **Blue Vilas** (empreendimento de luxo, lazer, conforto e qualidade de vida) montado a partir do material real do empreendimento (fotos e clipes do Drive do projeto).

## O que tem aqui

| Peça | Arquivo | Descrição |
|---|---|---|
| **Vídeo final do Reels** | `video/blue-vilas-reels.mp4` | 1080×1920 · ~25,5s · H.264 + AAC (áudio silencioso, pronto para receber trilha) |
| Roteiro de edição | `video/roteiro-edicao-reels.md` | Diagnóstico do material, storyboard segundo a segundo, prompt de color grading e copy |
| Script de montagem | `video/build/make_segments.py` | Script Python/ffmpeg que gera cada cena (Ken Burns, color grade, legendas) e monta o vídeo final — reprodutível/ajustável |

## Como foi montado

O `.mov` bruto original (`Blue_Vilas.mov`, ~400 MB) não pôde ser baixado por inteiro — o conector de Drive disponível tem limite de 10 MB por arquivo. Em vez de simular a edição, localizei na mesma pasta do Drive os **clipes e fotos individuais do making-of do empreendimento** (dezenas de `.MOV`/`.DNG` do book oficial) e baixei os que estavam dentro do limite: 2 vídeos curtos + 13 fotos em altíssima resolução (4536×8064, nativas 9:16).

A partir desse material real, montei o Reels com ffmpeg: seleção dos melhores enquadramentos (piscina, fachada/jardim, área social, academia, interior com vista mar, espaço kids), efeito Ken Burns (zoom/pan lento) nas fotos, color grading quente/praiano (realces em tom areia, sombras puxadas para azul-marinho), legendas dinâmicas e card final de CTA — seguindo o storyboard de `video/roteiro-edicao-reels.md`.

**Áudio:** o vídeo sai com trilha silenciosa (sem música) — não há como licenciar uma trilha comercial por aqui. Recomendo adicionar um áudio em alta no próprio editor de Reels do Instagram antes de publicar.

## Pendências antes de publicar

- Adicionar trilha sonora no Instagram (Reels Audio).
- Confirmar endereço, valores e canal de contato reais para o comentário fixado (legenda e hashtags sugeridas já estão na seção 5 de `video/roteiro-edicao-reels.md`).
- Se quiser, posso gerar variações (cortes mais curtos, outra ordem de cenas, ou incorporar mais fotos do Drive que ainda não baixei).
