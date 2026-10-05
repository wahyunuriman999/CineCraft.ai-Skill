---
name: cineforge-engine
description: Industrial-grade Autonomous AI Video Production & Editing Suite. Synthesizes 44 tier-1 repositories into 8 unified engines covering lossless stream surgery, 9:16 vertical auto-reframing with face tracking, acoustic trigger detection & DAW mixing, Remotion/WASM declarative rendering, viral shorts forge with beat-synced montage pacing, human-creator aesthetic scrapbooking, and multi-platform social distribution.
---

# 🎬 CineForge Engine: Apex Autonomous Video Production Suite

Skill ini mendefinisikan standar operasional prosedur (SOP), arsitektur teknis, formula FFmpeg, serta script automasi terpadu dari **CineForge Engine**. Menggabungkan DNA dari **44 repositori video editing open-source terkemuka di dunia** ke dalam 8 mesin produksi otonom untuk AI Coding Assistants (Google Antigravity, Claude Code, Codex).

---

## 🏛️ ARSITEKTUR 8 MESIN UTAMA (THE 44-REPOSITORY SYNTHESIS MATRIX)

```
                                  ┌────────────────────────────────────────────────────────┐
                                  │                CINEFORGE APEX CORE                     │
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
```

| Engine | Repositori Sumber | Domain & Kapabilitas Utama |
| :--- | :--- | :--- |
| **1. Stream Surgery & Video Slimming** | `mifi/lossless-cut`, `AlguevaraSec/VideoSlim`, `juntaosun/ComeCut`, `walterlow/freecut`, `jub0t/Concat` | Pemotongan stream-copy instan (0 detik tanpa render), CRF target visual-lossless slimming, H.264/H.265/AV1 2-pass compression, keyframe demuxing. |
| **2. Computer Vision & Auto-Reframe (9:16)** | `KazKozDev/auto-vertical-reframe`, `obi19999/smart-video-reframe`, `fralapo/FrameShift`, `innovatrics/smartface`, `getopenscreen/openscreen` | Konversi 16:9 ke 9:16 otomatis dengan pelacakan wajah pembicara aktif, smoothing kamera (Kalman/EMA filter), dynamic pan-and-scan, cursor auto-zoom. |
| **3. Acoustic AI, Audio Separation & Vocal** | `WyattBlue/auto-editor`, `facebookresearch/demucs`, `hexgrad/kokoro`, `mycroftai/mycroft-precise`, `gantasmo/theDAW` | Pembuangan hening/dead-air otomatis (`auto-editor`), pemisahan vokal/musik latar (`demucs`), neural TTS lokal 82M (`kokoro`), sidechain ducking vokal, normalisasi EBU R128 (-14 LUFS). |
| **4. Declarative, React & WASM Rendering** | `remotion-dev/remotion`, `mifi/editly`, `tnfe/FFCreator`, `imgly/video-editor-wasm-react` | Pembuatan video berbasis komponen React (`Remotion`), timeline deklaratif berbasis JSON (`Editly`), WebGL shader transitions 60fps (`FFCreator`), WASM client-side player. |
| **5. AI Shorts Forge & Beat-Sync Pacing** | `mutonby/openshorts`, `gyoridavid/short-video-maker`, `Anil-matcha/AI-Youtube-Shorts-Generator`, `ronak-create/FableCut` | **Signature Human Creator Pacing**: 8-beat intro teaser montage (0.24s - 0.28s cuts), 3-tier multi-cam split, scrapbooking ripped-paper typography, zero tacky meme clutter. |
| **6. NLE Bridges, CapCut & Agent Code Editor** | `Vvv1940905115/Adobe-Premiere-Pro-AutoEdit`, `fralapo/clippyme`, `diffusionstudio/editor`, `0xsline/OpenChatCut` | Interoperabilitas Final Cut Pro XML (.xml) ke Premiere Pro & DaVinci Resolve, manipulasi langsung draft file **CapCut / JianYing** (`clippyme`), code-first editing untuk AI Agent. |
| **7. AI Video Localization & Super-Resolution**| `Huanshere/VideoLingo`, `visomaster/VisoMaster`, `xinntao/Real-ESRGAN`, `TencentARC/GFPGAN` | Translasi & sulih suara AI multibahasa (*AI Dubbing*) kelas Netflix (`VideoLingo`), restorasi wajah buram (`GFPGAN`), dan upscaling frame ke 4K (`Real-ESRGAN`). |
| **8. Social Ingestion & Autonomous Matrix** | `eat-pray-ai/yutu`, `diezo/Ensta`, `ramtinak/InstagramApiSharp` | Scraping tren medsos, upload otomatis YouTube Shorts & Instagram Reels dengan penjadwalan, anti-ban jitter delay, dan metadata SEO generator. |

---

## ⚡ FORMULA & PROTOKOL PRODUKSI

### 1. Zero-Loss Keyframe-Accurate Cut (Stream Surgery)
```bash
ffmpeg -ss 00:01:15.000 -to 00:03:42.500 -i input.mp4 -c copy -avoid_negative_ts make_zero output_segment.mp4
```

### 2. Beat-Synced Teaser Montage (Human Creator Standard)
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

### 3. Multi-Cam 3-Tier Split Screen
```bash
ffmpeg -y \
  -ss 3.0 -t 6.0 -i top_view.mp4 \
  -ss 6.0 -t 6.0 -i mid_view.mp4 \
  -ss 1.0 -t 6.0 -i bot_view.mp4 \
  -filter_complex "\
    [0:v]scale=1080:640:force_original_aspect_ratio=increase,crop=1080:640[vt];\
    [1:v]scale=1080:640:force_original_aspect_ratio=increase,crop=1080:640[vm];\
    [2:v]scale=1080:640:force_original_aspect_ratio=increase,crop=1080:640[vb];\
    [vt][vm][vb]vstack=inputs=3[v]" \
  -map "[v]" -c:v libx264 -crf 18 split_stack.mp4
```

### 4. Acoustic Voice Ducking & EBU R128 Normalization
```bash
ffmpeg -y -i voice.wav -i bgm.wav -filter_complex "\
  [1:a]volume=0.20[ducked_bgm];\
  [0:a]volume=1.35[boost_voice];\
  [boost_voice][ducked_bgm]amix=inputs=2:duration=first,\
  loudnorm=I=-14:TP=-1.5:LRA=11[aout]" \
  -map "[aout]" final_audio.aac
```

### 5. Aesthetic Cream Card Outro (#FAF7F2)
Menempatkan video di jendela rasio 16:9 di atas kanvas warna cream hangat `#FAF7F2` dengan tipografi serif elegan dan cutout teks kertas.
