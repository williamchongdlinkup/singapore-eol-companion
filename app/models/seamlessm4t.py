"""SeamlessM4T v2 — Cantonese (yue) and Hokkien (min-nan) STT/TTS via Modal."""
import httpx
from app.config import MODAL_ENDPOINT_URL

SUPPORTED_LANGUAGES = {"yue", "min-nan"}


async def transcribe(audio_bytes: bytes, language: str) -> str:
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Language {language!r} not supported by SeamlessM4T endpoint")
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            f"{MODAL_ENDPOINT_URL}/transcribe",
            content=audio_bytes,
            headers={"X-Language": language},
        )
        response.raise_for_status()
        return response.json()["text"]
