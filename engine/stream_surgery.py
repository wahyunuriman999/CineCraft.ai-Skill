import subprocess
import imageio_ffmpeg

def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()

def lossless_cut(input_file: str, start: str, duration: float, output_file: str):
    """
    Performs keyframe-accurate lossless stream-copy without re-encoding (0 sec render).
    """
    cmd = [
        get_ffmpeg(), "-y",
        "-ss", str(start),
        "-t", str(duration),
        "-i", input_file,
        "-c", "copy",
        "-avoid_negative_ts", "make_zero",
        output_file
    ]
    subprocess.run(cmd, check=True)

def video_slim(input_file: str, output_file: str, crf: int = 24):
    """
    Compresses video with visual losslessness using H.265 / HEVC.
    """
    cmd = [
        get_ffmpeg(), "-y",
        "-i", input_file,
        "-c:v", "libx265",
        "-crf", str(crf),
        "-preset", "slow",
        "-tag:v", "hvc1",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        output_file
    ]
    subprocess.run(cmd, check=True)
