import subprocess
import imageio_ffmpeg

def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()

def compose_triple_stack(
    top_video: str,
    mid_video: str,
    bottom_video: str,
    duration: float,
    output_file: str,
    banner_overlay: str = None,
    audio_source_idx: int = 0
):
    """
    Stacks three video streams vertically into a 1080x1920 Instagram Reels format.
    """
    ffmpeg_exe = get_ffmpeg()
    cmd = [
        ffmpeg_exe, "-y",
        "-t", str(duration), "-i", top_video,
        "-t", str(duration), "-i", mid_video,
        "-t", str(duration), "-i", bottom_video,
    ]
    
    vf = (
        "[0:v]scale=1080:640:force_original_aspect_ratio=increase,crop=1080:640[vt];"
        "[1:v]scale=1080:640:force_original_aspect_ratio=increase,crop=1080:640[vm];"
        "[2:v]scale=1080:640:force_original_aspect_ratio=increase,crop=1080:640[vb];"
        "[vt][vm][vb]vstack=inputs=3[stack];"
    )
    
    if banner_overlay:
        cmd.extend(["-loop", "1", "-t", str(duration), "-i", banner_overlay])
        vf += "[3:v]scale=1080:1920[ov];[stack][ov]overlay=0:0[v]"
    else:
        vf += "[stack]copy[v]"
        
    cmd.extend([
        "-filter_complex", vf,
        "-map", "[v]",
        "-map", f"{audio_source_idx}:a",
        "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
        "-c:a", "aac", "-b:a", "192k",
        output_file
    ])
    subprocess.run(cmd, check=True)
