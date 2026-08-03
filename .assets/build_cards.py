import sys
sys.path.insert(0, "/home/user/Marketing/.assets")
from branding import *
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/user/Marketing/campanha-green-home/imagens"
person = load_person_cutout()

# ---------------------------------------------------------------
# 1) CAPA DO REELS (1080x1920)
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.7, H*0.35), glow_color=GREEN, glow_radius=1000)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=55, seed=3))
d = ImageDraw.Draw(img)

green_home_logo(img, (90, 70), center=False, scale=0.85)

d.text((90, 560), "O TEASER", font=sans("SemiBold", 26), fill=GOLD)
f_h1 = font("Bold", size=100)
f_h2 = font("Bold", italic=True, size=104)
d.text((84, 610), "Onde a vida", font=f_h1, fill=CREAM)
d.text((84, 730), "floresce.", font=f_h2, fill=GOLD)

img = place_person(img, person, target_h=1180, bottom_y=1870, center_x=W*0.62)

d = ImageDraw.Draw(img)
d.line([(90, 1730), (990, 1730)], fill=(255, 255, 255, 40), width=2)
badge(img, (90, 1760), person, "ASSINATURA DE EXCELÊNCIA", "Green Home · Abrantes", scale=1.0)
conceitto_wordmark(img, (W - 260, 1750), scale=0.95)

save(img, f"{OUT}/reels-cover.png")

# ---------------------------------------------------------------
# 2) POST DE FEED (1080x1350)
# ---------------------------------------------------------------
img = base_canvas(w=FEED_W, h=FEED_H, glow_pos=(FEED_W*0.25, FEED_H*0.15), glow_color=GOLD, glow_radius=800)
img.alpha_composite(leaf_motif((FEED_W, FEED_H), color=GREEN, alpha=60, seed=11))
d = ImageDraw.Draw(img)

green_home_logo(img, (70, 56), center=False, scale=0.62)

f_h1 = font("Bold", size=66)
f_h2 = font("Bold", italic=True, size=70)
d.text((70, 150), "Uma vida em família", font=f_h1, fill=CREAM)
d.text((70, 222), "que floresce no verde.", font=f_h2, fill=GOLD)

bullets = [
    "175 casas exclusivas em condomínio fechado",
    "96m² internos + quintal privativo de 86 a 210m²",
    "3.700m² de área de lazer completa",
    "Portaria 24h com guarita e clausura",
    "Ponto para carregar carro elétrico",
]
f_b = sans("Medium", 30)
by = 330
for b in bullets:
    d.ellipse([70, by+8, 86, by+24], fill=GREEN)
    d.text((104, by), b, font=f_b, fill=CREAM_DIM)
    by += 52

f_price_label = sans("SemiBold", 26)
f_price = font("Bold", size=58)
d.text((70, by+28), "A PARTIR DE", font=f_price_label, fill=GOLD)
d.text((70, by+62), "R$ 638.800", font=f_price, fill=CREAM)
d.text((70, by+134), "Financie até 100% pela Caixa · use o FGTS*", font=sans("Regular", 24), fill=MUTED)
d.text((70, by+184), "Abrantes, ao lado do", font=sans("Medium", 20), fill=MUTED)
d.text((70, by+210), "Villa Global Education", font=sans("SemiBold", 22), fill=CREAM_DIM)

img = place_person(img, person, target_h=740, bottom_y=FEED_H+30, center_x=FEED_W*0.86)

d = ImageDraw.Draw(img)
d.line([(70, FEED_H-96), (FEED_W-70, FEED_H-96)], fill=(255,255,255,40), width=2)
conceitto_wordmark(img, (70, FEED_H-80), scale=0.75)

save(img, f"{OUT}/feed-post.png")

# ---------------------------------------------------------------
# 3) STORY 1 — HOOK
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.4), glow_color=GREEN, glow_radius=1100)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=70, seed=21))
d = ImageDraw.Draw(img)

for i, w in enumerate([340, 340, 340]):
    xoff = 70 + i*350
    d.rounded_rectangle([xoff, 60, xoff+330, 66], radius=3, fill=(255,255,255,70))
green_home_logo(img, (W/2, 100), center=True, scale=0.7)

f_hook = font("Bold", size=88)
lines = wrap_lines(d, "Já imaginou sua família vivendo cercada de verde, com todo o luxo e segurança de um condomínio fechado?", f_hook, 900)
ty = 620
for i, ln in enumerate(lines):
    color = GOLD if i == len(lines)-1 else CREAM
    bbox = d.textbbox((0,0), ln, font=f_hook)
    d.text(((W-(bbox[2]-bbox[0]))/2, ty), ln, font=f_hook, fill=color)
    ty += 104

d.text((W/2, 1780), "arraste pra cima  ↑", font=sans("Medium", 28), fill=CREAM_DIM, anchor="ma")
save(img, f"{OUT}/story-1-hook.png")

# ---------------------------------------------------------------
# 4) STORY 2 — BENEFÍCIOS
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.12), glow_color=GOLD, glow_radius=900)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=55, seed=33))
d = ImageDraw.Draw(img)
for i in range(3):
    xoff = 70 + i*350
    d.rounded_rectangle([xoff, 60, xoff+330, 66], radius=3, fill=(255,255,255,70) if i!=1 else (255,255,255,230))
green_home_logo(img, (W/2, 100), center=True, scale=0.7)

d.text((W/2, 220), "Diferenciais exclusivos", font=font("Bold", size=56), fill=CREAM, anchor="ma")

items = [
    ("175", "casas exclusivas"),
    ("3.700m²", "de área de lazer"),
    ("28m", "piscina com raia"),
    ("24h", "portaria + guarita com clausura"),
    ("4", "suítes disponíveis por casa"),
]
f_num = font("Bold", size=64)
f_lab = sans("Medium", 30)
gy = 400
for num, lab in items:
    d.text((100, gy), num, font=f_num, fill=GOLD)
    bbox = d.textbbox((0,0), num, font=f_num)
    d.text((100 + (bbox[2]-bbox[0]) + 26, gy+14), lab, font=f_lab, fill=CREAM_DIM)
    gy += 130

d.text((100, gy+20), "Sport bar · Lounge gourmet · Espaço yoga · Pet place", font=sans("Regular", 26), fill=MUTED)
d.text((100, gy+60), "Brinquedoteca · Quadra beach tennis · Campo de futebol", font=sans("Regular", 26), fill=MUTED)

save(img, f"{OUT}/story-2-beneficios.png")

# ---------------------------------------------------------------
# 5) STORY 3 — CTA (com espaço para enquete)
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.35), glow_color=GREEN, glow_radius=1000)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=60, seed=44))
d = ImageDraw.Draw(img)
for i in range(3):
    xoff = 70 + i*350
    d.rounded_rectangle([xoff, 60, xoff+330, 66], radius=3, fill=(255,255,255,230))
green_home_logo(img, (W/2, 100), center=True, scale=0.7)

img = place_person(img, person, target_h=980, bottom_y=1330, center_x=W*0.5)
d = ImageDraw.Draw(img)

d.text((W/2, 1360), "Quer morar rodeado de verde,", font=font("Bold", size=52), fill=CREAM, anchor="ma")
d.text((W/2, 1424), "sem abrir mão do luxo?", font=font("Bold", italic=True, size=54), fill=GOLD, anchor="ma")

d.rounded_rectangle([190, 1520, W-190, 1660], radius=24, outline=(255,255,255,90), width=2)
d.text((W/2, 1548), "Quer conhecer o Green Home?", font=sans("SemiBold", 26), fill=CREAM_DIM, anchor="ma")
d.text((W/2, 1590), "Sim  /  Sim, com certeza", font=sans("Bold", 30), fill=GOLD, anchor="ma")
d.text((W/2, 1500), "[ espaço reservado para sticker de enquete nativo ]", font=sans("Regular", 18), fill=MUTED, anchor="ma")

d.rounded_rectangle([260, 1700, W-260, 1770], radius=30, fill=GOLD)
d.text((W/2, 1718), "chama no direct →", font=sans("Bold", 28), fill=(10,10,10), anchor="ma")

conceitto_wordmark(img, (W/2-120, 1820), scale=0.85)

save(img, f"{OUT}/story-3-cta.png")

print("ALL CARDS DONE")
