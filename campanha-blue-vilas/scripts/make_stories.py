# Gera cards de Stories (1080x1920) a partir das fotos brutas selecionadas,
# com color grading, copy sobreposta e a logo da Conceitto como marca d'água.
#
# Como usar:
#   1. pip install pillow
#   2. Baixe as fotos-fonte (ver CARDS abaixo) do Drive da campanha para a
#      pasta apontada em RAW_DIR (por padrão, campanha-blue-vilas/raw/).
#   3. python3 scripts/make_stories.py
#
# Dependências de fonte (ambiente original do Claude Code):
#   - /mnt/skills/examples/canvas-design/canvas-fonts/Outfit-{Bold,Regular}.ttf
#   - /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf
# Em outra máquina, troque FONTS/EMOJI_FONT por caminhos equivalentes
# (ex.: instale a família "Outfit" do Google Fonts e "Noto Color Emoji").
import os, re
from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
CAMPAIGN_DIR = os.path.dirname(HERE)
RAW_DIR = os.path.join(CAMPAIGN_DIR, "raw")
BASE = RAW_DIR
FONTS = "/mnt/skills/examples/canvas-design/canvas-fonts"
EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
OUT = os.path.join(CAMPAIGN_DIR, "stories")
os.makedirs(OUT, exist_ok=True)

W, H = 1080, 1920
GOLD = (214, 168, 92)
WHITE = (255, 255, 255)

f_bold = lambda sz: ImageFont.truetype(f"{FONTS}/Outfit-Bold.ttf", sz)
f_reg = lambda sz: ImageFont.truetype(f"{FONTS}/Outfit-Regular.ttf", sz)

logo = Image.open(os.path.join(CAMPAIGN_DIR, "assets", "logo-conceitto-transparente.png")).convert("RGBA")

_emoji_cache = {}
def emoji_img(ch, target_h):
    key = (ch, target_h)
    if key in _emoji_cache:
        return _emoji_cache[key]
    f = ImageFont.truetype(EMOJI_FONT, 109)
    tmp = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((5, 5), ch, font=f, embedded_color=True)
    bbox = tmp.getbbox()
    if not bbox:
        return None
    tmp = tmp.crop(bbox)
    ratio = target_h / tmp.height
    tmp = tmp.resize((max(1, int(tmp.width * ratio)), target_h), Image.LANCZOS)
    _emoji_cache[key] = tmp
    return tmp

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF]", flags=re.UNICODE
)

def draw_line_with_emoji(canvas, draw, xy, text, font, fill, shadow=(0, 0, 0, 170), offset=3):
    x, y = xy
    parts = EMOJI_RE.split(text)
    emojis = EMOJI_RE.findall(text)
    cx = x
    ascent, descent = font.getmetrics()
    line_h = ascent + descent
    for idx, part in enumerate(parts):
        if part:
            draw.text((cx + offset, y + offset), part, font=font, fill=shadow)
            draw.text((cx, y), part, font=font, fill=fill)
            cx += draw.textlength(part, font=font)
        if idx < len(emojis):
            em = emoji_img(emojis[idx], int(line_h * 0.8))
            if em:
                canvas.alpha_composite(em, (int(cx + 6), int(y + line_h * 0.12)))
                cx += em.width + 10
    return cx

def cover_crop(im, w, h):
    im = ImageOps.exif_transpose(im)
    src_w, src_h = im.size
    src_ratio = src_w / src_h
    dst_ratio = w / h
    if src_ratio > dst_ratio:
        new_h = h
        new_w = int(src_ratio * new_h)
    else:
        new_w = w
        new_h = int(new_w / src_ratio)
    im = im.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    return im.crop((left, top, left + w, top + h))

def grade(im):
    im = im.convert("RGB")
    r, g, b = im.split()
    r = r.point(lambda x: min(255, int(x * 1.06)))
    b = b.point(lambda x: int(x * 0.94))
    im = Image.merge("RGB", (r, g, b))
    im = ImageEnhance.Color(im).enhance(1.18)
    im = ImageEnhance.Contrast(im).enhance(1.07)
    im = ImageEnhance.Brightness(im).enhance(1.04)
    gamma = 1.08
    lut = [min(255, int(255 * ((i / 255) ** (1 / gamma)))) for i in range(256)]
    im = im.point(lut * 3)
    return im

def rounded_rect(draw, box, radius, fill):
    draw.rounded_rectangle(box, radius=radius, fill=fill)

def make_gradient(w, h, top_alpha=0, bottom_alpha=0, top_h=0, bottom_h=0):
    grad = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = grad.load()
    for y in range(h):
        a = 0
        if y < top_h and top_alpha > 0:
            a = int(top_alpha * (1 - y / top_h))
        if y > h - bottom_h and bottom_alpha > 0:
            local = (y - (h - bottom_h)) / bottom_h
            a = max(a, int(bottom_alpha * local))
        if a:
            for x in range(w):
                px[x, y] = (0, 0, 0, a)
    return grad

CARDS = [
    dict(photo="IMG_9036.JPG", kicker="BLUE VILAS", headline="Sua vida dos sonhos\ncomeça aqui.",
         sub="Desliza pra conhecer →", focus="top"),
    dict(photo="IMG_9017.JPG", kicker="PAISAGISMO", headline="O verde que te recebe\nantes da porta de casa. 🌿",
         sub=None, focus="center"),
    dict(photo="IMG_9034.JPG", kicker="NATUREZA", headline="Qualidade de vida é ter\na natureza como vizinha. 🌴",
         sub=None, focus="center"),
    dict(photo="IMG_9061.JPG", kicker="LAZER", headline="Aqui, o dia começa com\no som da água e o mar. 🌊",
         sub=None, focus="center"),
    dict(photo="IMG_8987.JPG", kicker="VEM CONHECER", headline="O sorriso de quem já\nencontrou o lugar certo.",
         sub="Manda um oi no direct 💬", cta="FALE COM A CONCEITTO", focus="top"),
]
N = len(CARDS)

for i, card in enumerate(CARDS):
    im = Image.open(os.path.join(BASE, card["photo"]))
    im = cover_crop(im, W, H)
    im = grade(im)
    canvas = im.convert("RGBA")

    grad = make_gradient(W, H, top_alpha=150, bottom_alpha=215, top_h=260, bottom_h=850)
    canvas.alpha_composite(grad)
    draw = ImageDraw.Draw(canvas)

    margin = 40
    gap = 10
    seg_w = (W - 2 * margin - gap * (N - 1)) / N
    for s in range(N):
        x0 = margin + s * (seg_w + gap)
        x1 = x0 + seg_w
        color = (255, 255, 255, 235) if s <= i else (255, 255, 255, 90)
        rounded_rect(draw, (x0, 54, x1, 60), radius=3, fill=color)

    logo_h = 46
    logo_small = logo.copy()
    ratio = logo_h / logo_small.height
    logo_small = logo_small.resize((int(logo_small.width * ratio), logo_h), Image.LANCZOS)
    canvas.alpha_composite(logo_small, (margin, 84))
    draw.text((margin + logo_small.width + 14, 84), "conceittoimoveis", font=f_bold(30), fill=WHITE)
    draw_line_with_emoji(canvas, draw, (margin + logo_small.width + 14, 122), "📍 Blue Vilas", f_reg(24), (255, 255, 255, 220))

    ky = 1360 if card["focus"] == "top" else 1420
    draw.text((margin, ky), card["kicker"], font=f_bold(28), fill=GOLD)

    hy = ky + 46
    hf = f_bold(64)
    for line in card["headline"].split("\n"):
        draw_line_with_emoji(canvas, draw, (margin, hy), line, hf, WHITE)
        hy += 76

    if card.get("sub"):
        draw_line_with_emoji(canvas, draw, (margin, hy + 14), card["sub"], f_reg(32), (255, 255, 255, 235))
        hy += 60

    if card.get("cta"):
        btn_w, btn_h = 620, 96
        bx0 = (W - btn_w) // 2
        by0 = 1760
        rounded_rect(draw, (bx0, by0, bx0 + btn_w, by0 + btn_h), radius=48, fill=GOLD)
        bbox = draw.textbbox((0, 0), card["cta"], font=f_bold(34))
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((bx0 + (btn_w - tw) / 2, by0 + (btn_h - th) / 2 - bbox[1]), card["cta"], font=f_bold(34), fill=(30, 30, 30))
    else:
        chip_h = 64
        lg = logo.copy()
        r2 = (chip_h - 16) / lg.height
        lg = lg.resize((int(lg.width * r2), chip_h - 16), Image.LANCZOS)
        label = "Conceitto Imóveis"
        lf = f_bold(24)
        tb = draw.textbbox((0, 0), label, font=lf)
        text_w = tb[2] - tb[0]
        pad_l, pad_r, gap2 = 14, 26, 16
        chip_w = pad_l + lg.width + gap2 + text_w + pad_r
        cx0 = W - margin - chip_w
        cy0 = H - 150
        rounded_rect(draw, (cx0, cy0, cx0 + chip_w, cy0 + chip_h), radius=chip_h // 2, fill=(255, 255, 255, 230))
        canvas.alpha_composite(lg, (int(cx0 + pad_l), int(cy0 + 8)))
        draw.text((cx0 + pad_l + lg.width + gap2, cy0 + chip_h / 2), label, font=lf, fill=(40, 90, 60), anchor="lm")

    out_path = os.path.join(OUT, f"story-{i+1}-{os.path.splitext(card['photo'])[0]}.png")
    canvas.convert("RGB").save(out_path, quality=95)
    print("saved", out_path)
