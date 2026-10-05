# 🎬 CineCraft.ai-Skill

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FFmpeg: 7.0+](https://img.shields.io/badge/FFmpeg-7.0+-green.svg)](https://ffmpeg.org/)
[![Agent: Antigravity | Claude Code | Codex](https://img.shields.io/badge/Agent%20Skill-Antigravity%20%7C%20Claude%20%7C%20Codex-purple.svg)](#installation)

**Autonomous AI Video Production & Virtual Studio Suite for AI Coding Agents**  
*Synthesizes 48 tier-1 open-source repositories into 11 unified production engines.*

[Key Features](#-key-features) • [11-Engine Architecture](#-11-engine-architecture) • [Creator Recipes](#-creator-recipes) • [Quickstart](#-quickstart) • [Skill Installation](#-installation-as-ai-agent-skill)

</div>

---

## 🌟 Overview

**CineCraft.ai-Skill** is an industrial-grade autonomous video production, virtual studio, and animation runtime designed specifically for AI agents (*Google Antigravity, Claude Code, OpenAI Codex*). 

Unlike standard video wrappers, CineCraft combines:
*   **Viral Reel Mimicking** (`reelmimic`): Show it a video you love; get a new video in the exact same pacing and rhythm.
*   **2D Mesh Animated Avatars** (`mesh-avatar-studio` + `AnimeEffects`): Turn a single character illustration into a breathing, blinking talking-head presenter for Reels/Shorts.
*   **AI Skeletal Rigging** (`spine-animation-ai`): Auto-rig 2D characters with bone hierarchies and trigger action gestures.
*   **Cognitive Rhythm Pacing**: Beat-synced snapshot teaser cuts (0.24s–0.28s).
*   **Aesthetic Creator Scrapbooking**: Paper tape headers, grid note overlays, warm cream card outros (`#FAF7F2`) with zero tacky meme clutter.
*   **Lossless Stream Surgery**: 0-second keyframe cuts and visually lossless HEVC slimming.

---

## 🏛 11-Engine Architecture

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

1. **Stream Surgery & Slimming**: Zero-loss instant cutting (`-c copy`) and 70-85% visually lossless compression via CRF 2-pass.
2. **Auto-Reframe & Face Tracking (9:16)**: Automatic speaker face tracking and smooth pan-and-scan for vertical platforms.
3. **Acoustic AI & DAW Mixing**: Silence removal, AI stem separation (`demucs`), neural TTS (`kokoro`), and voice-over ducking with EBU R128 loudness normalization (-14 LUFS).
4. **Declarative & React Rendering**: Programmatic timeline composition via JSON and React (`remotion`, `editly`, `FFCreator`).
5. **Shorts Forge & Beat-Sync Pacing**: Signature human-editor pacing—rapid 0.24s–0.28s snapshot cuts synced to drum transients, ripped paper titles, and clean creator typography.
6. **NLE Bridges & Direct Editor**: Direct manipulation of CapCut/JianYing draft files and Final Cut Pro XML export for Adobe Premiere & DaVinci Resolve.
7. **AI Video Localization**: AI voice cloning, multi-language dubbing (`VideoLingo`), and frame super-resolution (`Real-ESRGAN`).
8. **Social Distribution Matrix**: Autonomous ingestion, trending audio matching, and scheduled multi-platform deployment.
9. **Viral Reel Mimicking & Style Transfer** (`reelmimic`): Decomposes any viral reference video into a reusable timeline recipe and re-creates it with your raw clips.
10. **2D Mesh Avatar Studio** (`mesh-avatar-studio` + `AnimeEffects`): Animates single static portraits into organic talking avatars using sinusoidal Free-Form Deformation (FFD).
11. **AI Skeletal 2D Rigging** (`spine-animation-ai`): Auto-generates Spine 2D skeletal hierarchies and keyframes actions (pointing, nodding, jumping) for dynamic B-Roll characters.

---

## 🎨 Creator Recipes

### 1. Viral Reel Style Mimicking
Replicate the exact shot rhythm and pacing of any reference video you love:
```python
from engine.reel_mimic import ReelMimicEngine

# 1. Analyze reference video and extract pacing slots
blueprint = ReelMimicEngine.generate_blueprint("viral_benchmark.mp4")

# 2. Render new raw footage matching the blueprint
ReelMimicEngine.render_mimicked_reel(
    blueprint=blueprint,
    raw_clips=["clip1.mp4", "clip2.mp4", "clip3.mp4"],
    bgm_file="trending_beat.wav",
    output_file="recreated_reel.mp4"
)
```

### 2. 2D Mesh Animated Avatar (VTuber Presenter Overlay)
Animate an illustration into a breathing talking-head presenter:
```python
from engine.mesh_avatar import MeshAvatarStudio

# Render transparent 2D mesh breathing loop
MeshAvatarStudio.generate_idle_avatar_overlay(
    avatar_image="mascot.png",
    duration=10.0,
    output_file="avatar_loop.webm"
)

# Composite as presenter overlay on video
MeshAvatarStudio.composite_avatar_presenter(
    main_video="background.mp4",
    avatar_clip="avatar_loop.webm",
    position="bottom_right",
    scale_pct=0.35,
    output_file="reel_with_avatar.mp4"
)
```

### 3. AI Skeletal 2D Rigging
Auto-rig character assets to interact with on-screen titles:
```python
from engine.spine_rigging import SpineRiggingAI

# Generate Spine 2D bone structure
skeleton = SpineRiggingAI.build_character_skeleton(character_name="presenter")

# Generate pointing gesture action
action = SpineRiggingAI.generate_pointing_action(duration=3.0)
```

### 4. 8-Beat Snapshot Teaser Montage
Creates an ultra-dynamic teaser hook at 0.28s intervals synced to drum transients:
```python
from engine.beat_sync import generate_teaser_montage

generate_teaser_montage(
    clip_specs=[("shot1.mp4", 0, 0.28), ("shot2.mp4", 2.0, 0.28), ("shot3.mp4", 5.0, 0.28)],
    hook_overlay="assets/01_hook_title.png",
    output_file="teaser.mp4"
)
```

---

## 📦 Installation as AI Agent Skill

### Google Antigravity / Claude Code
Clone or copy this repository into your agent's skills directory:
```bash
git clone https://github.com/wahyunuriman999/CineCraft.ai-Skill.git ~/.gemini/config/skills/cinecraft-ai-skill
```

The agent will automatically recognize `SKILL.md` and acquire autonomous video editing & virtual studio capabilities!

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

Developed with ❤️ by **Wahyu Nur Iman** (@wahyunuriman999)
