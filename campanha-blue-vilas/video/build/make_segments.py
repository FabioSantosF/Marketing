#!/usr/bin/env python3
"""Builds each segment of the Blue Vilas Reels from real source photos/clips:
Ken Burns zoom on stills, center-crop on video clips, warm coastal color
grade, dynamic caption, then concatenates everything into the final Reels."""
import subprocess
import os

SRC = "/home/user/Marketing/campanha-blue-vilas/video/bruto"
OUT = "/home/user/Marketing/campanha-blue-vilas/video/build"
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
W, H, FPS = 1080, 1920, 30

GRADE = (
    "eq=contrast=1.08:saturation=1.18:brightness=0.02,"
    "colorbalance=rs=0.05:gs=0.0:bs=-0.06:rm=0.05:gm=0.0:bm=-0.04:rh=0.10:gh=0.02:bh=-0.08,"
    "vignette=PI/6"
)

def text_filter(text, y_expr="h*0.80", fontsize=62, fade=0.35):
    text = text.replace("'", "’").replace(":", "\\:")
    return (
        f"drawtext=fontfile={FONT}:text='{text}':fontcolor=white:fontsize={fontsize}:"
        f"x=(w-text_w)/2:y={y_expr}:box=1:boxcolor=black@0.42:boxborderw=22:"
        f"line_spacing=6:alpha='if(lt(t,{fade}),t/{fade},1)'"
    )

def build_still(name, src_file, duration, text, zoom_in=True, fontsize=62, y_expr="h*0.80"):
    frames = int(duration * FPS)
    z = "min(zoom+0.0009,1.18)" if zoom_in else "if(eq(on,1),1.14,max(zoom-0.0009,1.0))"
    zoompan = (
        f"scale=1500:2667,zoompan=z='{z}':d={frames}:"
        f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}"
    )
    vf = f"{zoompan},{GRADE}"
    if text:
        vf += f",{text_filter(text, y_expr, fontsize)}"
    out_path = f"{OUT}/{name}.mp4"
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", f"{SRC}/{src_file}",
        "-t", str(duration), "-vf", vf,
        "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "18",
        "-an", out_path,
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print("OK", out_path)

def build_clip(name, src_file, text=None, fontsize=58, y_expr="h*0.80"):
    vf = (
        f"crop=ih*9/16:ih,scale={W}:{H},{GRADE}"
    )
    if text:
        vf += f",{text_filter(text, y_expr, fontsize)}"
    out_path = f"{OUT}/{name}.mp4"
    cmd = [
        "ffmpeg", "-y", "-i", f"{SRC}/{src_file}",
        "-vf", vf, "-r", str(FPS), "-pix_fmt", "yuv420p",
        "-c:v", "libx264", "-crf", "18", "-an", out_path,
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print("OK", out_path)

def build_cta(name, duration=3.0):
    text1 = "Blue Vilas"
    text2 = "Comente EU QUERO e receba o book exclusivo"
    vf = (
        f"drawtext=fontfile={FONT}:text='{text1}':fontcolor=0xF2D9B8:fontsize=110:"
        f"x=(w-text_w)/2:y=h*0.42:alpha='if(lt(t,0.4),t/0.4,1)',"
        f"drawtext=fontfile={FONT}:text='{text2}':fontcolor=white:fontsize=50:"
        f"x=(w-text_w)/2:y=h*0.58:box=1:boxcolor=black@0.0:line_spacing=10:"
        f"alpha='if(lt(t,1.0),0,if(lt(t,1.4),(t-1.0)/0.4,1))'"
    )
    out_path = f"{OUT}/{name}.mp4"
    cmd = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=0x1B2A4A:s={W}x{H}:d={duration}:r={FPS}",
        "-vf", vf, "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "18", "-an", out_path,
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print("OK", out_path)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)

    # 1. Gancho — piscina/lazer (0-3s)
    build_still("01_hook", "IMG_9051.jpg", 3.0,
                "E se o seu próximo endereço fosse\num refúgio à beira-mar?",
                zoom_in=True, fontsize=54, y_expr="h*0.72")

    # 2. Fachada + jardim (3-6.5s)
    build_still("02_fachada", "IMG_9045.jpg", 3.5,
                "Blue Vilas", zoom_in=True, fontsize=80, y_expr="h*0.85")

    # 3. Lounge/area social (6.5-9.5s)
    build_still("03_lounge", "IMG_8991.jpg", 3.0,
                "Lazer completo.\nTodo santo dia.", zoom_in=True, fontsize=58)

    # 4. Academia (foto) + clipe real do letreiro Academia
    build_still("04a_academia_foto", "IMG_9013.jpg", 1.8,
                "Estrutura completa.", zoom_in=True, fontsize=58)
    build_clip("04b_academia_clip", "IMG_9002.MOV")

    # 5. Interior vista mar (11.3-14.8s)
    build_still("05_interior", "IMG_8981.jpg", 3.5,
                "Acabamento de alto padrão.\nConforto em cada detalhe.",
                zoom_in=True, fontsize=52)

    # 6. Espaco kids (foto) + clipe do jardim
    build_still("06a_kids", "IMG_8988.jpg", 1.8,
                "Espaço para a família toda.", zoom_in=True, fontsize=50)
    build_clip("06b_jardim_clip", "IMG_9025.MOV")

    # 7. Fechamento emocional — fachada/jardim (18.9-22.4s)
    build_still("07_fechamento", "IMG_9048.jpg", 3.5,
                "Qualidade de vida\ncomeça em casa.", zoom_in=False, fontsize=58)

    # 8. CTA final
    build_cta("08_cta", duration=3.2)

    print("All segments built.")
