---
name: cinecraft-ai-skill
description: Industrial-grade Autonomous AI Video Production & Virtual Studio Suite. Synthesizes 48 tier-1 repositories into 11 unified engines covering lossless stream surgery, 9:16 auto-reframing, acoustic AI mastering, viral shorts beat-sync pacing, NLE/CapCut bridges, viral reel style transfer & mimicking (ReelMimic), 2D animated mesh avatars with FFD deformation (MeshAvatar & AnimeEffects), and AI skeletal character animation & rigging (Spine 2D AI).
---

# 🎬 CineCraft.ai-Skill: Apex Autonomous Video & Virtual Studio Suite

Skill ini mendefinisikan standar operasional prosedur (SOP), arsitektur teknis, formula FFmpeg, serta script automasi terpadu dari **CineCraft.ai-Skill**. Menggabungkan DNA dari **48 repositori open-source terkemuka di dunia** ke dalam **11 Mesin Produksi Terpadu** untuk AI Coding Assistants (Google Antigravity, Claude Code, OpenAI Codex).

---

## 🏛️ ARSITEKTUR 11 MESIN UTAMA (THE 48-REPOSITORY SYNTHESIS MATRIX)

```
                                  ┌────────────────────────────────────────────────────────┐
                                  │             CINECRAFT.AI APEX RUNTIME                  │
                                  └───────────────────────────┬────────────────────────────┘
         ┌──────────────────┬────────────────────┬────────────┼────────────┬───────────────────┬───────────────────┐
         ▼                  ▼                    ▼            ▼            ▼                   ▼                   ▼
┌─────────────────┐┌─────────────────┐┌──────────────────┐┌────────────┐┌──────────────────┐┌─────────────────┐┌─────────────────┐
│ ENGINE 1:       ││ ENGINE 2:       ││ ENGINE 3:        ││ ENGINE 4:  ││ ENGINE 5:        ││ ENGINE 6:       ││ ENGINE 7 & 8:   │
│ Stream Surgery  ││ Auto-Reframe &  ││ Acoustic AI & DAW││ Declarative││ Shorts Forge &   ││ NLE Bridges &   ││ AI Localization │
│ & Slimming      ││ Face Tracking   ││ (Demucs, theDAW, ││ & React    ││ Beat-Sync Pacing ││ Agent Editor     ││ & Social Matrix │
│ (LosslessCut,   ││ (SmartFace,     ││  auto-editor,    ││ (Remotion, ││ (OpenShorts,     ││ (Premiere-XML,  ││ (VideoLingo,    │
│  VideoSlim)     ││  AutoReframe)   ││  Kokoro, Precise)││  FFCreator)││  Capite, Stable) ││  Clippyme, NLE) ││  Yutu, Ensta)   │
└─────────────────┘└─────────────────┘└──────────────────┘└────────────┘└──────────────────┘└─────────────────┘└─────────────────┘
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                 ▼                                 ▼
┌─────────────────────────────────┐┌────────────────────────────────┐┌────────────────────────────────┐
│ ENGINE 9:                       ││ ENGINE 10:                     ││ ENGINE 11:                     │
│ Viral Reel Mimicking            ││ 2D Mesh Avatar Studio          ││ AI Skeletal 2D Rigging         │
│ & Style Transfer                ││ & FFD Deformation              ││ & Character Action AI          │
│ (edenfunf/reelmimic)            ││ (mesh-avatar-studio,           ││ (GenielabsOpenSource/          │
│                                 ││  AnimeEffects)                 ││  spine-animation-ai)           │
└─────────────────────────────────┘└────────────────────────────────┘└────────────────────────────────┘
```

| Engine | Repositori Sumber | Domain & Kapabilitas Utama |
| :--- | :--- | :--- |
| **1. Stream Surgery & Video Slimming** | `mifi/lossless-cut`, `AlguevaraSec/VideoSlim`, `juntaosun/ComeCut`, `walterlow/freecut`, `jub0t/Concat` | Pemotongan stream-copy instan (0 detik tanpa render), CRF target visual-lossless slimming, H.264/H.265/AV1 2-pass compression, keyframe demuxing. |
| **2. Computer Vision & Auto-Reframe (9:16)** | `KazKozDev/auto-vertical-reframe`, `obi19999/smart-video-reframe`, `fralapo/FrameShift`, `innovatrics/smartface` | Konversi 16:9 ke 9:16 otomatis dengan pelacakan wajah pembicara aktif, smoothing kamera (Kalman/EMA filter), dynamic pan-and-scan, cursor auto-zoom. |
| **3. Acoustic AI, Audio Separation & Vocal** | `WyattBlue/auto-editor`, `facebookresearch/demucs`, `hexgrad/kokoro`, `mycroftai/mycroft-precise`, `gantasmo/theDAW` | Pembuangan hening/dead-air otomatis (`auto-editor`), pemisahan vokal/musik latar (`demucs`), neural TTS lokal 82M (`kokoro`), sidechain ducking vokal, normalisasi EBU R128 (-14 LUFS). |
| **4. Declarative, React & WASM Rendering** | `remotion-dev/remotion`, `mifi/editly`, `tnfe/FFCreator`, `imgly/video-editor-wasm-react` | Pembuatan video berbasis komponen React (`Remotion`), timeline deklaratif berbasis JSON (`Editly`), WebGL shader transitions 60fps (`FFCreator`), WASM client-side player. |
| **5. AI Shorts Forge & Beat-Sync Pacing** | `mutonby/openshorts`, `gyoridavid/short-video-maker`, `Anil-matcha/AI-Youtube-Shorts-Generator`, `ronak-create/FableCut` | **Signature Human Creator Pacing**: 8-beat intro teaser montage (0.24s - 0.28s cuts), 3-tier multi-cam split, scrapbooking ripped-paper typography, zero tacky meme clutter. |
| **6. NLE Bridges, CapCut & Agent Code Editor** | `Vvv1940905115/Adobe-Premiere-Pro-AutoEdit`, `fralapo/clippyme`, `diffusionstudio/editor`, `0xsline/OpenChatCut` | Interoperabilitas Final Cut Pro XML (.xml) ke Premiere Pro & DaVinci Resolve, manipulasi langsung draft file **CapCut / JianYing** (`clippyme`), code-first editing untuk AI Agent. |
| **7. AI Video Localization & Super-Resolution**| `Huanshere/VideoLingo`, `visomaster/VisoMaster`, `xinntao/Real-ESRGAN`, `TencentARC/GFPGAN` | Translasi & sulih suara AI multibahasa (*AI Dubbing*) kelas Netflix (`VideoLingo`), restorasi wajah buram (`GFPGAN`), dan upscaling frame ke 4K (`Real-ESRGAN`). |
| **8. Social Ingestion & Autonomous Matrix** | `eat-pray-ai/yutu`, `diezo/Ensta`, `ramtinak/InstagramApiSharp` | Scraping tren medsos, upload otomatis YouTube Shorts & Instagram Reels dengan penjadwalan, anti-ban jitter delay, dan metadata SEO generator. |
| **9. Viral Reel Mimicking & Style Transfer** | `edenfunf/reelmimic` | Menganalisis video referensi viral yang disukai user, mengekstrak blueprint ritme (scene detection, beat map, penempatan teks), dan merender video baru dengan format persis sama. |
| **10. 2D Mesh Avatar Studio & FFD Warping** | `shinshin86/mesh-avatar-studio`, `AnimeEffectsDevs/AnimeEffects` | Mengubah 1 gambar ilustrasi/maskot/foto statis menjadi avatar bergerak (*talking head / VTuber*) dengan kedipan mata, napas sinusoidal (*Free-Form Deformation*), dan lip-sync transparan. |
| **11. AI Skeletal 2D Rigging & Action AI** | `GenielabsOpenSource/spine-animation-ai` | Auto-rigging struktur tulang 2D hierarkis (root, hip, torso, head, limbs) dan pembuatan animasi gerak dinamis (menunjuk judul, melompat, melambaikan tangan) untuk B-Roll karakter. |

---

## ⚡ FORMULA & PROTOKOL PRODUKSI

### 1. Reel Style Mimicking (Tiru Gaya Video Referensi)
```python
from engine.reel_mimic import ReelMimicEngine

# 1. Ekstrak blueprint dari video idaman
blueprint = ReelMimicEngine.generate_blueprint("reference_viral.mp4")

# 2. Render footage mentah user mengikuti ritme video referensi tersebut
ReelMimicEngine.render_mimicked_reel(
    blueprint=blueprint,
    raw_clips=["shotA.mp4", "shotB.mp4", "shotC.mp4"],
    bgm_file="trending_beat.wav",
    output_file="mimicked_reel.mp4"
)
```

### 2. 2D Mesh Animated Avatar (VTuber / Presenter Overlay)
```python
from engine.mesh_avatar import MeshAvatarStudio

# 1. Animasi ilustrasi statis menjadi avatar bernapas & berkedip transparan
MeshAvatarStudio.generate_idle_avatar_overlay(
    avatar_image="mascot.png",
    duration=15.0,
    output_file="avatar_loop.webm"
)

# 2. Tempelkan avatar presenter di pojok kanan bawah video Reels
MeshAvatarStudio.composite_avatar_presenter(
    main_video="reels_background.mp4",
    avatar_clip="avatar_loop.webm",
    position="bottom_right",
    scale_pct=0.35,
    output_file="final_with_avatar.mp4"
)
```

### 3. AI Skeletal 2D Rigging (Karakter Menunjuk Judul)
```python
from engine.spine_rigging import SpineRiggingAI

# Bangun hierarki tulang karakter otomatis
skeleton = SpineRiggingAI.build_character_skeleton(character_name="chef_mascot")
# Hasilkan sekuens animasi menunjuk teks judul
action = SpineRiggingAI.generate_pointing_action(duration=3.0)
```

### 4. Zero-Loss Keyframe-Accurate Cut (Stream Surgery)
```bash
ffmpeg -ss 00:01:15.000 -to 00:03:42.500 -i input.mp4 -c copy -avoid_negative_ts make_zero output_segment.mp4
```

### 5. Beat-Synced Teaser Montage (Human Creator Standard)
Memotong 8 snapshot klip dalam interval 0.24s - 0.28s selaras ketukan drum/perkusi intro untuk retensi puncak Instagram Reels / TikTok:
```bash
ffmpeg -y \
  -ss 2.0 -t 0.28 -i clip1.mp4 \
  -ss 5.0 -t 0.28 -i clip2.mp4 \
  -ss 3.0 -t 0.28 -i clip3.mp4 \
  -ss 1.0 -t 1.84 -i clip_mc.mp4 \
  -loop 1 -t 2.68 -i ripped_paper_title.png \
  -filter_complex "[0:v][1:v][2:v][3:v]concat=n=4:v=1:a=0[bg];[4:v]scale=1080:1920[ov];[bg][ov]overlay=0:0[v]" \
  -map "[v]" -c:v libx264 -crf 18 teaser.mp4
```

### 6. Acoustic Voice Ducking & EBU R128 Normalization
```bash
ffmpeg -y -i voice.wav -i bgm.wav -filter_complex "\
  [1:a]volume=0.20[ducked_bgm];\
  [0:a]volume=1.35[boost_voice];\
  [boost_voice][ducked_bgm]amix=inputs=2:duration=first,\
  loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
  -map "[aout]" final_audio.aac
```
