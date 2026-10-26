from openai import AsyncOpenAI
from app.config import MODEL_BASE_URL

_client = AsyncOpenAI(base_url=MODEL_BASE_URL)
WONDER_MODEL = "muse-wonder-1.0"


async def generate_deep_response(text: str, tradition: str, passages: list[dict]) -> str:
    context = "\n\n".join(
        f"[{p.get('corpus', '')}] {p.get('text', '')}" for p in passages
    )
    response = await _client.chat.completions.create(
        model=WONDER_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a deep theological analyst. Provide precise, tradition-specific "
                    "guidance grounded in the provided source passages. "
                    "Distinguish clearly between sub-traditions (e.g. Theravada vs. Mahayana; "
                    "Taoist cosmology vs. Buddhist concepts). Never conflate traditions."
                ),
            },
            {
                "role": "user",
                "content": f"Tradition: {tradition}\n\nSource passages:\n{context}\n\nQuestion: {text}",
            },
        ],
    )
    return response.choices[0].message.content
