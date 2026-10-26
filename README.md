# Singapore End-of-Life Companion

Voice-enabled spiritual companion for dying patients and their families in Singapore. Nine religious traditions, four languages (English, Mandarin, Cantonese, Hokkien), retrieval-grounded responses with source citation and four compliance gates.

Built for the Meta Global AI Developer Hackathon 2026.

## Architecture

### Model pipeline

| Model | Role |
|---|---|
| **Muse Glimmer** | Tradition classification and intent routing |
| **Muse Spark Open** (`meta-models/muse-spark-open-1026` via Baseten) | Primary pastoral dialogue, `reasoning_effort: xhigh` |
| **Muse Wonder 1.0** | Deep theological analysis for complex multi-tradition queries |
| **Muse Voice Transcribe** | English and Mandarin STT via WebSocket |
| **SeamlessM4T v2** (Modal) | Cantonese (yue) and Hokkien (min-nan) STT/TTS |

### Compliance gates

1. **Gate 1 — PII screening**: NRIC and phone number redaction before logging
2. **Gate 2 — Crisis escalation**: Keyword detection with compassionate handoff to SOS Singapore (1800-221-4444)
3. **Gate 3 — Interfaith harmony**: Prevents responses that demean other traditions (Singapore MRHA context)
4. **Gate 4 — Hallucination grounding**: Every response cites its source passage from the retrieval corpus

### Retrieval

Passage retrieval is powered by [SourceTruth](https://sourcetruth.io) — a canonical text API across 30 corpora of religious, philosophical, and classical texts. The EOL Companion calls SourceTruth as an external service; the ingestion pipeline and corpus data are not part of this repository.

## Setup

```bash
cp config.example.env .env
# Fill in your API keys
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment variables

See `config.example.env`. Key variables:

- `MODEL_BASE_URL` / `MODEL_ID`: default to Meta Model API / `muse-spark-1.3`. Swap to Baseten for `meta-models/muse-spark-open-1026` (Best Open Weight Build bonus).
- `SOURCETRUTH_API_KEY`: retrieval layer access
- `MODAL_ENDPOINT_URL`: SeamlessM4T v2 endpoint for Hokkien/Cantonese

## Traditions covered

Buddhist (Theravada), Buddhist (Mahayana), Taoist, Christian, Muslim, Hindu, Sikh, Bahai, Jain, Jewish
