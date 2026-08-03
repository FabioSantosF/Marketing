import sys, os, math
sys.path.insert(0, "/home/user/Marketing/.assets")
from branding import *
from PIL import Image, ImageDraw

SCENES = "/home/user/Marketing/.assets/scenes"
os.makedirs(SCENES, exist_ok=True)
person = load_person_cutout()

FPS = 24

def progress_bar(img, active_idx, total=7):
    d = ImageDraw.Draw(img)
    seg_w = (W - 140 - (total-1)*20) / total
    x = 70
    for i in range(total):
        color = (255,255,255,235) if i <= active_idx else (255,255,255,55)
        d.rounded_rectangle([x, 56, x+seg_w, 62], radius=3, fill=color)
        x += seg_w + 20

def header(img, idx):
    progress_bar(img, idx)
    green_home_logo(img, (W/2, 92), center=True, scale=0.62)

# ---------------------------------------------------------------
# SCENE 1 — HOOK
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.55, H*0.42), glow_color=GREEN, glow_radius=1050)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=65, seed=5))
header(img, 0)
d = ImageDraw.Draw(img)
d.text((W/2, H*0.42), "Onde a vida", font=font("Bold", size=118), fill=CREAM, anchor="mm")
d.text((W/2, H*0.42+120), "floresce.", font=font("Bold", italic=True, size=126), fill=GOLD, anchor="mm")
save(img, f"{SCENES}/scene1.png")

# ---------------------------------------------------------------
# SCENE 2
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.4), glow_color=GREEN, glow_radius=1050)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=60, seed=6))
header(img, 1)
d = ImageDraw.Draw(img)
f = font("Bold", size=80)
lines = wrap_lines(d, "Um condomínio pensado pra sua família viver mais perto do verde,", f, 900)
ty = H/2 - (len(lines)*98)/2
for ln in lines:
    d.text((W/2, ty), ln, font=f, fill=CREAM, anchor="ma")
    ty += 98
save(img, f"{SCENES}/scene2.png")

# ---------------------------------------------------------------
# SCENE 3
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.4), glow_color=GOLD, glow_radius=1000)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=60, seed=8))
header(img, 2)
d = ImageDraw.Draw(img)
f = font("Bold", italic=True, size=88)
lines = wrap_lines(d, "com mais segurança e muito mais lazer.", f, 900)
ty = H/2 - (len(lines)*104)/2
for ln in lines:
    d.text((W/2, ty), ln, font=f, fill=GOLD, anchor="ma")
    ty += 104
save(img, f"{SCENES}/scene3.png")

# ---------------------------------------------------------------
# SCENE 4 — counter frames 0 -> 175 CASAS EXCLUSIVAS
# ---------------------------------------------------------------
os.makedirs(f"{SCENES}/scene4_frames", exist_ok=True)
D4_total_frames = 99
count_frames = 78
target = 175
bg4 = base_canvas(glow_pos=(W*0.5, H*0.42), glow_color=GREEN, glow_radius=1100)
bg4.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=55, seed=12))
for i in range(D4_total_frames):
    t = min(1.0, i / count_frames)
    eased = 1 - (1-t)**3
    val = int(eased * target)
    frame = bg4.copy()
    header(frame, 3)
    d = ImageDraw.Draw(frame)
    d.text((W/2, H*0.42), str(val), font=font("Bold", size=210), fill=GOLD, anchor="mm")
    d.text((W/2, H*0.42+150), "CASAS EXCLUSIVAS", font=sans("SemiBold", 42), fill=CREAM, anchor="mm")
    d.text((W/2, H*0.42+200), "condomínio fechado · Abrantes", font=sans("Regular", 28), fill=MUTED, anchor="mm")
    save(frame, f"{SCENES}/scene4_frames/f{i:04d}.png")

# ---------------------------------------------------------------
# SCENE 5 — counter frames 0 -> 3.700m² DE LAZER
# ---------------------------------------------------------------
os.makedirs(f"{SCENES}/scene5_frames", exist_ok=True)
D5_total_frames = 109
count_frames5 = 86
target5 = 3700
bg5 = base_canvas(glow_pos=(W*0.5, H*0.42), glow_color=GOLD, glow_radius=1100)
bg5.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=55, seed=14))
for i in range(D5_total_frames):
    t = min(1.0, i / count_frames5)
    eased = 1 - (1-t)**3
    val = int(eased * target5)
    frame = bg5.copy()
    header(frame, 4)
    d = ImageDraw.Draw(frame)
    txt = f"{val:,}".replace(",", ".") + "m²"
    d.text((W/2, H*0.42), txt, font=font("Bold", size=150), fill=GOLD, anchor="mm")
    d.text((W/2, H*0.42+130), "DE ÁREA DE LAZER", font=sans("SemiBold", 42), fill=CREAM, anchor="mm")
    d.text((W/2, H*0.42+180), "piscina raia 28m · sport bar · yoga · pet place", font=sans("Regular", 26), fill=MUTED, anchor="mm")
    save(frame, f"{SCENES}/scene5_frames/f{i:04d}.png")

# ---------------------------------------------------------------
# SCENE 6 — Preço + financiamento
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.4), glow_color=GREEN, glow_radius=1050)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=55, seed=18))
header(img, 5)
d = ImageDraw.Draw(img)
d.text((W/2, H*0.34), "A PARTIR DE", font=sans("SemiBold", 34), fill=GOLD, anchor="mm")
d.text((W/2, H*0.34+80), "R$ 638.800", font=font("Bold", size=118), fill=CREAM, anchor="mm")
d.text((W/2, H*0.34+180), "financiado em até 100% pela Caixa", font=sans("Medium", 36), fill=CREAM_DIM, anchor="mm")
d.text((W/2, H*0.34+230), "sem entrada · use o FGTS*", font=sans("Regular", 30), fill=MUTED, anchor="mm")
save(img, f"{SCENES}/scene6.png")

# ---------------------------------------------------------------
# SCENE 7 — CARD FINAL
# ---------------------------------------------------------------
img = base_canvas(glow_pos=(W*0.5, H*0.30), glow_color=GREEN, glow_radius=1050)
img.alpha_composite(leaf_motif((W, H), color=GREEN, alpha=55, seed=21))
header(img, 6)
img = place_person(img, person, target_h=860, bottom_y=1180, center_x=W*0.5)
d = ImageDraw.Draw(img)
badge(img, (W/2-230, 1210), person, "ASSINATURA DE EXCELÊNCIA", "Julianne Costa · Consultora Green Home", scale=1.05)

d.text((W/2, 1360), "Vem que eu te mostro", font=font("Bold", size=62), fill=CREAM, anchor="ma")
d.text((W/2, 1428), "o Green Home.", font=font("Bold", italic=True, size=66), fill=GOLD, anchor="ma")

d.rounded_rectangle([260, 1560, W-260, 1638], radius=38, fill=GOLD)
d.text((W/2, 1580), "chama no direct →", font=sans("Bold", 30), fill=(10,10,10), anchor="ma")

d.line([(140, 1690), (W-140, 1690)], fill=(255,255,255,45), width=2)
conceitto_wordmark(img, (W/2-118, 1720), scale=1.0)
d.text((W/2, 1800), "@conceittoimoveis  ·  (71) 98855-1313  ·  conceittoimoveis.imb.br", font=sans("Medium", 24), fill=CREAM_DIM, anchor="ma")

save(img, f"{SCENES}/scene7.png")

print("ALL SCENES DONE")
