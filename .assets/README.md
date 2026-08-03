# Ferramental de geração das campanhas

Scripts Python (Pillow + ffmpeg) usados para montar as peças da campanha Green Home, reaproveitáveis para os próximos lançamentos:

- `branding.py` — paleta, tipografia (Playfair Display + Montserrat, em `fonts/`), gradientes, motivo de folhas, recorte/composição da foto da pessoa, marca d'água da Conceitto.
- `build_cards.py` — gera os 5 cards estáticos (`campanha-green-home/imagens/`).
- `build_scenes.py` — gera as 7 cenas do vídeo, incluindo os contadores animados.
- `build_video.py` — monta as cenas com zoom (Ken Burns) + crossfade cronometrado pela locução e mixa o áudio final.

Não versiono aqui a foto de origem da pessoa nem os frames/clipes intermediários (muito volume e sem necessidade — os PNGs/MP4 finais já estão em `campanha-green-home/`). Para reprocessar com uma nova foto, coloque o arquivo em `.assets/source/agente-original.jpg`, rode `pip install rembg onnxruntime` e gere o recorte com `rembg` antes de chamar `build_cards.py`/`build_scenes.py`.
