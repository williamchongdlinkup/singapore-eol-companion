"""Muse Voice Transcribe — English and Mandarin STT via WebSocket (Meta Model API)."""
# TODO: implement WebSocket stream handler for muse-voice-transcribe-1.0
# Supported: English (en), Mandarin Chinese (zh)
# Not supported: Cantonese (yue), Hokkien (min-nan) — see seamlessm4t.py


async def transcribe(audio_bytes: bytes, language: str = "en") -> str:
    raise NotImplementedError
