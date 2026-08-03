import subprocess, os, imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
SCENES = "/home/user/Marketing/.assets/scenes"
TMP = "/home/user/Marketing/.assets/clips"
os.makedirs(TMP, exist_ok=True)
FPS = 24
OVERLAP = 0.5

# desired on-screen durations (seconds), aligned to narration silence gaps
desired = [2.4375, 4.2165, 2.8575, 3.6200, 4.0275, 6.6540, 5.6870]
n = len(desired)
render = [desired[i] + (OVERLAP if i < n - 1 else 0) for i in range(n)]

def run(cmd):
    print("RUN:", " ".join(cmd))
    subprocess.run(cmd, check=True)

# --- Scene 1,2,3,6,7: static image + slow zoom (Ken Burns) ---
static_scenes = {0: "scene1.png", 1: "scene2.png", 2: "scene3.png", 5: "scene6.png", 6: "scene7.png"}
for idx, fname in static_scenes.items():
    dur = render[idx]
    frames = int(round(dur * FPS))
    out = f"{TMP}/clip{idx}.mp4"
    zoom_expr = "min(zoom+0.0012,1.10)" if idx != 6 else "min(zoom+0.0009,1.06)"
    vf = (
        f"scale=1620:2880,"
        f"zoompan=z='{zoom_expr}':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps={FPS},"
        f"format=yuv420p"
    )
    run([FFMPEG, "-y", "-loop", "1", "-i", f"{SCENES}/{fname}", "-t", str(dur),
         "-vf", vf, "-r", str(FPS), "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", out])

# --- Scene 4,5: pre-rendered counting sequences ---
for idx, folder in [(3, "scene4_frames"), (4, "scene5_frames")]:
    out = f"{TMP}/clip{idx}.mp4"
    run([FFMPEG, "-y", "-framerate", str(FPS), "-i", f"{SCENES}/{folder}/f%04d.png",
         "-vf", "format=yuv420p", "-c:v", "libx264", "-pix_fmt", "yuv420p", out])

# --- Chain xfade transitions ---
inputs = []
for i in range(n):
    inputs += ["-i", f"{TMP}/clip{i}.mp4"]

filter_parts = []
prev_label = "0:v"
offset = 0.0
cum = 0.0
for i in range(1, n):
    cum += desired[i-1]
    out_label = f"v{i}"
    filter_parts.append(
        f"[{prev_label}][{i}:v]xfade=transition=fade:duration={OVERLAP}:offset={cum:.3f}[{out_label}]"
    )
    prev_label = out_label

filter_complex = ";".join(filter_parts)

out_video = "/home/user/Marketing/.assets/green-home-teaser-novideo.mp4"
cmd = [FFMPEG, "-y"] + inputs + ["-filter_complex", filter_complex, "-map", f"[{prev_label}]",
       "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", str(FPS), out_video]
run(cmd)

# --- Mux narration audio ---
AUDIO = "/home/user/Marketing/.assets/audio/green-home-locucao.mp3"
FINAL = "/home/user/Marketing/campanha-green-home/video/green-home-teaser-reels.mp4"
run([FFMPEG, "-y", "-i", out_video, "-i", AUDIO,
     "-map", "0:v", "-map", "1:a",
     "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k",
     "-movflags", "+faststart",
     FINAL])

print("VIDEO DONE:", FINAL)
