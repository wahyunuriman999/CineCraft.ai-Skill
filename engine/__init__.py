"""
CineCraft.ai-Skill - Autonomous AI Video Production Suite
"""

from .stream_surgery import lossless_cut, video_slim
from .beat_sync import generate_teaser_montage
from .multicam_stack import compose_triple_stack
from .audio_mixer import duck_and_normalize
from .aesthetic_cards import generate_cream_outro
from .reel_mimic import ReelMimicEngine
from .mesh_avatar import MeshAvatarStudio
from .spine_rigging import SpineRiggingAI

__version__ = "1.1.0"
__author__ = "Wahyu Nur Iman"
