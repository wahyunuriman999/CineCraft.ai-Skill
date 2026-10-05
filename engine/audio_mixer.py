import subprocess
import imageio_ffmpeg

def get_ffmpeg():
    return imageio_ffmpeg.get_ffmpeg_exe()

def duck_and_normalize(
    voice_file: str,
    bgm_file: str,
    output_audio: str,
    bgm_duck_vol: float = 0.20,
    voice_boost_vol: float = 1.35,
    target_lufs: float = -14.0
):
    """
    Blends voiceover with ducked BGM and normalizes loudness to broadcast standard (EBU R128).
    """
    ffmpeg_exe = get_ffmpeg()
    af = (
        f"[1:a]volume={bgm_duck_vol}[bgm];"
        f"[0:a]volume={voice_boost_vol}[voice];"
        f"[voice][bgm]amix=inputs=2:duration=first,"
        f"loudnorm=I={target_lufs}:TP=-1.5:LRA=11[aout]"
    )
    cmd = [
        ffmpeg_exe, "-y",
        "-i", voice_file,
        "-i", bgm_file,
        "-filter_complex", af,
        "-map", "[aout]",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "44100",
        output_audio
    ]
    subprocess.run(cmd, check=True)
