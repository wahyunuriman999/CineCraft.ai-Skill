import subprocess
import imageio_ffmpeg

def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()

def generate_cream_outro(
    video_clip: str,
    output_file: str,
    duration: float = 6.0,
    overlay_png: str = None,
    bg_color: str = "#FAF7F2",
    bgm_file: str = None
):
    """
    Composes a 16:9 centered video window over a warm cream (#FAF7F2) aesthetic card canvas.
    """
    ffmpeg_exe = get_ffmpeg()
    cmd = [
        ffmpeg_exe, "-y",
        "-t", str(duration), "-i", video_clip,
    ]
    
    vf = (
        f"color=c={bg_color}:s=1080x1920:d={duration}[canvas];"
        "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:608:0:650[clip];"
        "[canvas][clip]overlay=0:656[bg];"
    )
    
    if overlay_png:
        cmd.extend(["-loop", "1", "-t", str(duration), "-i", overlay_png])
        vf += "[1:v]scale=1080:1920[ov];[bg][ov]overlay=0:0[v]"
    else:
        vf += "[bg]copy[v]"
        
    cmd.extend(["-filter_complex", vf, "-map", "[v]"])
    
    if bgm_file:
        cmd.extend([
            "-ss", "0", "-t", str(duration), "-i", bgm_file,
            "-filter_complex_threads", "2",
            "-map", "2:a" if overlay_png else "1:a"
        ])
    else:
        cmd.extend(["-map", "0:a?"])
        
    cmd.extend(["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", output_file])
    subprocess.run(cmd, check=True)
