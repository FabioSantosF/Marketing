# Tríduo e Festa da Sagrada Família 2026: post de agradecimento

Coloca uma foto do evento dentro da moldura do template oficial de agradecimento.

| Arquivo | Conteúdo |
|---|---|
| `saida/post-agradecimento.png` | **Post final** em 3072×2048, com o rodapé original (Diácono Genildo) |
| `saida/post-agradecimento-1536x1024.jpg` | O mesmo post no tamanho original do template |
| `saida/post-agradecimento-rodape-livre.png` | Mesma arte com a área do texto de agradecimento vazia |
| `saida/noite-2-post-agradecimento.png` (+ `-1536x1024.jpg`) | **2ª noite** (Pe. César Dias), template próprio com a faixa "2ª Noite" sobre a foto |
| `saida/noite-2-pascom-leo-moger.png` (+ `-1536x1024.jpg`) | **2ª noite, agradecimento da Pascom a Léo Moger**, com o logo da Pascom no rodapé |
| `saida/festa-template-conego-osmar.png` (+ `-1536x1024.jpg`) | **Dia da Festa (08/11)**: template com moldura vazia, selo "Missa Solene" e agradecimento ao Côn. Osmar Júnior |
| `saida/festa-post-conego-osmar.png` (+ `-1536x1024.jpg`) | **Post final da Festa**: foto dos padres com o Cônego no template enviado pela paróquia |
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
  --saida saida/noite-2-post-agradecimento.png --corte-esquerda 250 --corte-direita 160 --estender base --nitidez 1.4
```
Selos ou faixas do template que ficam dentro da moldura, como "2ª Noite", são detectados e continuam por cima da foto.

`--nitidez` (0 a ~1,5) aplica nitidez clássica só na luminância, igual na foto inteira. Acima de 1,5 surgem halos claros nos contornos.

Versão Pascom (logo à esquerda, filete dourado e texto à direita):
```bash
python3 compor_post.py --template entrada/template-noite-2.png --foto entrada/foto-noite-2-pascom.jpg \
  --saida saida/noite-2-pascom-leo-moger.png --corte-esquerda 200 --corte-direita 160 --estender base \
  --nitidez 1.4 --logo entrada/logo-pascom.jpg --prefixo "A Pascom agradece a " --nome "Léo Moger" \
  --texto "pela generosa colaboração nesta 2ª noite do Tríduo da Sagrada Família. Sua dedicação ajuda nossa comunidade a anunciar a beleza da fé."
```

Dia da Festa: `--selo` troca o texto da faixa vermelha dentro da moldura. Use `--foto ""` para gerar só o template, ou passe a foto para gerar o post pronto:
```bash
python3 compor_post.py --template entrada/template-noite-2.png --foto entrada/FOTO-DA-MISSA.jpg \
  --saida saida/festa-post-conego-osmar.png --selo "Missa Solene" --nome "Côn. Osmar Júnior" --logo entrada/logo-pascom.jpg \
  --texto "por presidir a Missa Solene da Festa da Sagrada Família, conduzindo nossa comunidade no amor, na comunhão e na missão." \
  --nitidez 1.4
```

Post final da Festa (template recomprimido → a área da foto vem do template limpo via `--mascara-de`):
```bash
python3 compor_post.py --template entrada/template-festa-conego-osmar.png --mascara-de entrada/template-noite-2.png \
  --foto entrada/foto-festa-padres-conego.jpg --saida saida/festa-post-conego-osmar.png \
  --corte-esquerda 280 --corte-direita 120 --estender base --nitidez 1.4
```

Use `--limpar-rodape` para gerar sem texto e `--corte-esquerda N` para ajustar o enquadramento.
