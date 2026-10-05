import subprocess
from typing import List, Tuple
import imageio_ffmpeg

def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()

def generate_teaser_montage(
    clip_specs: List[Tuple[str, float, float]], # List of (filepath, start_sec, duration_sec)
    hook_overlay: str,
    output_file: str,
    bgm_file: str = None
):
    """
    Assembles rapid beat-synced snapshot cuts (0.24s - 0.28s) under an aesthetic hook title overlay.
    """
    ffmpeg_exe = get_ffmpeg()
    cmd = [ffmpeg_exe, "-y"]
    
    # Add input clips
    filter_parts = []
    for idx, (path, ss, dur) in enumerate(clip_specs):
        cmd.extend(["-ss", str(ss), "-t", str(dur), "-i", path])
        filter_parts.append(f"[{idx}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v{idx}];")
        
    n_clips = len(clip_specs)
    concat_inputs = "".join(f"[v{i}]" for i in range(n_clips))
    filter_parts.append(f"{concat_inputs}concat=n={n_clips}:v=1:a=0[bg];")
    
    # Overlay hook
    cmd.extend(["-loop", "1", "-i", hook_overlay])
    filter_parts.append(f"[{n_clips}:v]scale=1080:1920[ov];[bg][ov]overlay=0:0[v]")
    
    total_dur = sum(dur for _, _, dur in clip_specs)
    cmd.extend(["-t", str(total_dur)])
    
    if bgm_file:
        cmd.extend(["-ss", "0", "-t", str(total_dur), "-i", bgm_file])
        cmd.extend(["-filter_complex", "".join(filter_parts)])
        cmd.extend(["-map", "[v]", "-map", f"{n_clips + 1}:a"])
    else:
        cmd.extend(["-filter_complex", "".join(filter_parts)])
        cmd.extend(["-map", "[v]"])
        
    cmd.extend(["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", output_file])
    subprocess.run(cmd, check=True)
