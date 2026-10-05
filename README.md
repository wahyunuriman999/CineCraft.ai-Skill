# 🎬 CineForge Engine

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FFmpeg: 7.0+](https://img.shields.io/badge/FFmpeg-7.0+-green.svg)](https://ffmpeg.org/)
[![Agent: Antigravity | Claude Code | Codex](https://img.shields.io/badge/Agent%20Skill-Antigravity%20%7C%20Claude%20%7C%20Codex-purple.svg)](#installation)

**Autonomous AI Video Production & Editing Suite for AI Coding Agents**  
*Synthesizes 44 tier-1 open-source repositories into 8 unified production engines.*

[Key Features](#-key-features) • [8-Engine Architecture](#-8-engine-architecture) • [Creator Recipes](#-human-creator-recipes) • [Quickstart](#-quickstart) • [Skill Installation](#-installation-as-ai-agent-skill)

</div>

---

## 🌟 Overview

**CineForge Engine** is an industrial-grade autonomous video production and editing runtime designed specifically for AI agents (Google Antigravity, Claude Code, OpenAI Codex). 

Unlike standard FFmpeg wrappers, CineForge combines **cognitive rhythm pacing**, **instant keyframe stream surgery**, **beat-synced montage generation**, **multi-cam split compositing**, and **aesthetic creator scrapbooking** (paper tape overlays, clean serif typography, warm cream card outros) with **zero tacky meme clutter**.

---

## 🏛 8-Engine Architecture

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

1. **Stream Surgery & Slimming**: Zero-loss instant cutting (`-c copy`) and 70-85% visually lossless compression via CRF 2-pass.
2. **Auto-Reframe & Face Tracking (9:16)**: Automatic speaker face tracking and smooth pan-and-scan for vertical platforms.
3. **Acoustic AI & DAW Mixing**: Silence removal, AI stem separation (`demucs`), neural TTS (`kokoro`), and voice-over ducking with EBU R128 loudness normalization (-14 LUFS).
4. **Declarative & React Rendering**: Programmatic timeline composition via JSON and React (`remotion`, `editly`, `FFCreator`).
5. **Shorts Forge & Beat-Sync Pacing**: Signature human-editor pacing—rapid 0.24s–0.28s snapshot cuts synced to drum transients, ripped paper titles, and clean creator typography.
6. **NLE Bridges & Direct Editor**: Direct manipulation of CapCut/JianYing draft files and Final Cut Pro XML export for Adobe Premiere & DaVinci Resolve.
7. **AI Video Localization**: AI voice cloning, multi-language dubbing (`VideoLingo`), and frame super-resolution (`Real-ESRGAN`).
8. **Social Distribution Matrix**: Autonomous ingestion, trending audio matching, and scheduled multi-platform deployment.

---

## 🎨 Human Creator Recipes

### 1. 8-Beat Snapshot Teaser Montage
Creates an ultra-dynamic teaser hook at 0.28s intervals synced to drum transients:
```python
from engine.beat_sync import generate_teaser_montage

generate_teaser_montage(
    clips=["shot1.mp4", "shot2.mp4", "shot3.mp4", "shot4.mp4"],
    interval=0.28,
    hook_overlay="assets/ripped_paper_hook.png",
    output="teaser.mp4"
)
```

### 2. Multi-Cam 3-Tier Split Screen
Stacks top stage action, presenter hype, and live audience reaction:
```python
from engine.multicam_stack import compose_triple_stack

compose_triple_stack(
    top="stage.mp4",
    mid="presenter.mp4",
    bottom="crowd.mp4",
    banner="assets/notebook_strip.png",
    output="split_screen.mp4"
)
```

### 3. Aesthetic Cream Card Outro (`#FAF7F2`)
Renders a warm, high-retention creator outro card with a centered 16:9 window:
```python
from engine.aesthetic_cards import generate_cream_outro

generate_cream_outro(
    video="cheer_group.mp4",
    headline_text="thank you for watching!",
    bg_color="#FAF7F2",
    output="outro.mp4"
)
```

---

## 📦 Installation as AI Agent Skill

### Google Antigravity / Claude Code
Clone or copy this repository into your agent's skills directory:
```bash
git clone https://github.com/wahyunuriman999/CineForge-Engine.git ~/.gemini/config/skills/cineforge-engine
```

The agent will automatically recognize `SKILL.md` and acquire autonomous video editing capabilities!

---

## 🚀 Quickstart (Python)

```bash
pip install -r requirements.txt
```

```python
from engine.stream_surgery import lossless_cut

# Cut 100% losslessly in 0 seconds
lossless_cut("raw_event.mp4", start="00:00:15", duration=5.0, output="cut.mp4")
```

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

Developed with ❤️ by **Wahyu Nur Iman** (@wahyunuriman999)
