"""Sistema visual da campanha Green Home (DENA Realizações / Conceitto Imóveis).
Paleta verde-floresta + dourado, tipografia Playfair Display + Montserrat.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1080, 1920
FEED_W, FEED_H = 1080, 1350

# ---- Paleta ----
BG_TOP = (8, 22, 15)          # verde quase preto
BG_BOTTOM = (3, 8, 6)         # preto
GOLD = (201, 162, 61)         # dourado (assinatura de excelência)
GREEN = (108, 178, 110)       # verde folha (frescor / natureza)
GREEN_DEEP = (30, 74, 45)     # verde profundo p/ formas
CREAM = (245, 241, 231)       # branco quente (texto)
CREAM_DIM = (200, 197, 186)
MUTED = (150, 158, 150)

FONT_DIR = "/home/user/Marketing/.assets/fonts"

_font_cache = {}

def font(weight="Bold", italic=False, size=48):
    key = (weight, italic, size)
    if key in _font_cache:
        return _font_cache[key]
    path = f"{FONT_DIR}/PlayfairDisplay-Italic.ttf" if italic else f"{FONT_DIR}/PlayfairDisplay-Bold.ttf"
    f = ImageFont.truetype(path, size)
    try:
        if not italic:
            f.set_variation_by_name(weight)
    except Exception:
        pass
    _font_cache[key] = f
    return f

def sans(weight="Regular", size=32):
    key = ("sans", weight, size)
    if key in _font_cache:
        return _font_cache[key]
    f = ImageFont.truetype(f"{FONT_DIR}/Montserrat.ttf", size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    _font_cache[key] = f
    return f


def vertical_gradient(size, top, bottom):
    w, h = size
    base = Image.new("RGB", (1, h), 0)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        base.putpixel((0, y), (r, g, b))
    return base.resize((w, h))


def radial_glow(size, center, radius, color, max_alpha=90):
    glow = Image.new("RGBA", size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    steps = 60
    for i in range(steps, 0, -1):
        t = i / steps
        r = int(radius * t)
        a = int(max_alpha * (1 - t) ** 2)
        gd.ellipse(
            [center[0] - r, center[1] - r, center[0] + r, center[1] + r],
            fill=(color[0], color[1], color[2], a),
        )
    return glow


def base_canvas(w=W, h=H, glow_pos=None, glow_color=GOLD, glow_radius=900):
    img = vertical_gradient((w, h), BG_TOP, BG_BOTTOM).convert("RGBA")
    if glow_pos:
        glow = radial_glow((w, h), glow_pos, glow_radius, glow_color, max_alpha=55)
        img = Image.alpha_composite(img, glow)
    noise = Image.effect_noise((w, h), 14).convert("L")
    noise = noise.point(lambda p: p * 0.03)
    img = Image.composite(Image.new("RGBA", (w, h), (255, 255, 255, 255)), img, noise)
    return img


def leaf_motif(size, color=GREEN, alpha=70, seed=7):
    """Traço orgânico de folhas/ramos, sutil, no fundo."""
    w, h = size
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rnd = random.Random(seed)
    cx, cy = w * 0.82, h * 0.20
    ang = -35
    length = h * 0.62
    steps = 26
    x, y = cx, cy
    pts = [(x, y)]
    for i in range(steps):
        ang += rnd.uniform(-9, 9)
        x += math.cos(math.radians(ang)) * (length / steps)
        y += math.sin(math.radians(ang)) * (length / steps) + (length / steps) * 0.9
        pts.append((x, y))
    d.line(pts, fill=(*color, alpha), width=3, joint="curve")
    for i in range(3, len(pts) - 3, 4):
        bx, by = pts[i]
        leaf_w, leaf_h = rnd.uniform(26, 44), rnd.uniform(46, 78)
        rot = rnd.uniform(-60, 60)
        leaf = Image.new("RGBA", (int(leaf_w * 2), int(leaf_h * 2)), (0, 0, 0, 0))
        ld = ImageDraw.Draw(leaf)
        ld.ellipse([0, 0, leaf_w * 2, leaf_h], fill=(*color, alpha))
        leaf = leaf.rotate(rot, expand=True)
        layer.paste(leaf, (int(bx - leaf.width / 2), int(by - leaf.height / 2)), leaf)
    layer = layer.filter(ImageFilter.GaussianBlur(0.6))
    return layer


def tracked_text_size(draw, text, fnt, tracking=0):
    total = 0
    for ch in text:
        bbox = draw.textbbox((0, 0), ch, font=fnt)
        total += (bbox[2] - bbox[0]) + tracking
    return total


def draw_tracked(draw, xy, text, fnt, fill, tracking=0, anchor_center_x=None):
    x, y = xy
    if anchor_center_x is not None:
        w = tracked_text_size(draw, text, fnt, tracking)
        x = anchor_center_x - w / 2
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        bbox = draw.textbbox((0, 0), ch, font=fnt)
        x += (bbox[2] - bbox[0]) + tracking
    return x


def wrap_lines(draw, text, fnt, max_width):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), test, font=fnt)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_rich_lines(img, draw, x, y, spans_lines, line_height, max_width=980):
    """spans_lines: list of lines; each line is list of (text, fnt, color)"""
    cy = y
    for line in spans_lines:
        cx = x
        for text, fnt, color in line:
            draw.text((cx, cy), text, font=fnt, fill=color)
            bbox = draw.textbbox((0, 0), text, font=fnt)
            cx += bbox[2] - bbox[0]
        cy += line_height
    return cy


def house_icon(size=64, color=(224, 122, 42)):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    w = size
    d.polygon([(w*0.5, w*0.06), (w*0.92, w*0.42), (w*0.78, w*0.42), (w*0.5, w*0.20), (w*0.22, w*0.42), (w*0.08, w*0.42)],
              fill=color)
    d.rectangle([w*0.22, w*0.42, w*0.78, w*0.88], fill=color)
    d.rectangle([w*0.42, w*0.60, w*0.58, w*0.88], fill=(8, 22, 15, 255))
    return im


_logo_cache = {}

def _conceitto_logo_img(variant="compact"):
    if variant in _logo_cache:
        return _logo_cache[variant]
    path = f"/home/user/Marketing/.assets/source/conceitto-logo-{variant}.png" if variant != "full" \
        else "/home/user/Marketing/.assets/source/conceitto-logo.png"
    im = Image.open(path).convert("RGBA")
    _logo_cache[variant] = im
    return im


def conceitto_wordmark(draw_target, xy, scale=1.0, target_h=90, variant="compact"):
    """Marca oficial da Conceitto Imóveis (fornecida pelo cliente), usada como marca d'água."""
    x, y = int(xy[0]), int(xy[1])
    logo = _conceitto_logo_img(variant)
    h = max(1, int(target_h * scale))
    w = max(1, int(logo.width * (h / logo.height)))
    logo_r = logo.resize((w, h), Image.LANCZOS)
    draw_target.alpha_composite(logo_r, (x, y))
    return w, h


def green_home_logo(draw_target, xy, center=True, scale=1.0, color=CREAM, accent=GOLD):
    x, y = xy
    d = ImageDraw.Draw(draw_target)
    f_home = sans("SemiBold", int(30 * scale))
    f_green = font("Bold", italic=True, size=int(58 * scale))
    label = "H O M E"
    lw = tracked_text_size(d, label, f_home, tracking=int(10*scale))
    gw = d.textbbox((0, 0), "green", font=f_green)
    gw = gw[2] - gw[0]
    total_w = max(lw, gw)
    cx = x if not center else x
    draw_tracked(d, (cx - lw/2 if center else x, y), label, f_home, color, tracking=int(10*scale))
    d.text((cx - gw/2 if center else x, y + int(30*scale)), "green", font=f_green, fill=accent)
    return


def vignette(img):
    w, h = img.size
    v = Image.new("L", (w, h), 0)
    vd = ImageDraw.Draw(v)
    vd.rectangle([0, 0, w, h], fill=0)
    for i in range(120):
        t = i / 120
        vd.rectangle([i*2, i*2, w-i*2, h-i*2], outline=int(60*(1-t)))
    v = v.filter(ImageFilter.GaussianBlur(80))
    black = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    img.paste(black, (0, 0), v)
    return img


def load_person_cutout():
    return Image.open("/home/user/Marketing/.assets/source/agente-cutout.png").convert("RGBA")


def place_person(canvas, cutout, target_h, bottom_y, center_x, warm_grade=True, shadow=True):
    """Redimensiona o recorte real (sem alterar rosto/corpo) e posiciona no card."""
    ratio = target_h / cutout.height
    new_w = int(cutout.width * ratio)
    person = cutout.resize((new_w, target_h), Image.LANCZOS)

    if warm_grade:
        r, g, b, a = person.split()
        r = r.point(lambda p: min(255, int(p * 1.03)))
        b = b.point(lambda p: int(p * 0.97))
        person = Image.merge("RGBA", (r, g, b, a))

    px = int(center_x - new_w / 2)
    py = int(bottom_y - target_h)

    if shadow:
        shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        alpha = person.split()[3]
        dark = Image.new("RGBA", person.size, (0, 0, 0, 140))
        shadow_layer.paste(dark, (px + 18, py + 26), alpha)
        shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(30))
        canvas.alpha_composite(shadow_layer)

    canvas.alpha_composite(person, (px, py))
    return canvas


def badge(draw_target, xy, avatar_cutout, name_line1, name_line2, scale=1.0):
    x, y = int(xy[0]), int(xy[1])
    d = ImageDraw.Draw(draw_target)
    r = int(34 * scale)
    thumb = avatar_cutout.resize((int(avatar_cutout.width * (2*r)/avatar_cutout.height), 2*r), Image.LANCZOS)
    mask = Image.new("L", (2*r, 2*r), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([0, 0, 2*r, 2*r], fill=255)
    crop_x = max(0, (thumb.width - 2*r)//2)
    thumb_c = thumb.crop((crop_x, 0, crop_x + 2*r, 2*r))
    ring = Image.new("RGBA", (2*r+8, 2*r+8), (0,0,0,0))
    rd = ImageDraw.Draw(ring)
    rd.ellipse([0,0,2*r+8,2*r+8], outline=GOLD, width=3)
    draw_target.paste(ring, (x-4, y-4), ring)
    draw_target.paste(thumb_c, (x, y), mask)
    f1 = sans("Medium", int(20*scale))
    f2 = sans("Bold", int(26*scale))
    d.text((x + 2*r + 18, y - 2), name_line1, font=f1, fill=CREAM_DIM)
    d.text((x + 2*r + 18, y + int(22*scale)), name_line2, font=f2, fill=CREAM)


def save(img, path):
    if img.mode == "RGBA":
        img = img.convert("RGB")
    img.save(path, quality=95)
    print("saved", path)
