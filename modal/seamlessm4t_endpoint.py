import modal

app = modal.App("eol-companion-seamlessm4t")

image = modal.Image.debian_slim().pip_install(
    "transformers>=4.40.0",
    "torch>=2.2.0",
    "torchaudio>=2.2.0",
    "sentencepiece",
)


@app.function(
    image=image,
    gpu="L40S",
    timeout=60,
)
@modal.web_endpoint(method="POST")
async def transcribe(request: modal.Request) -> dict:
    import torchaudio
    from transformers import AutoProcessor, SeamlessM4Tv2Model
    import io

    language = request.headers.get("X-Language", "min-nan")
    audio_bytes = await request.body()

    processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
    model = SeamlessM4Tv2Model.from_pretrained("facebook/seamless-m4t-v2-large")

    audio_array, sample_rate = torchaudio.load(io.BytesIO(audio_bytes))
    inputs = processor(audios=audio_array, src_lang=language, return_tensors="pt")
    output = model.generate(**inputs, tgt_lang="eng")[0]
    text = processor.decode(output, skip_special_tokens=True)

    return {"text": text, "language": language}
