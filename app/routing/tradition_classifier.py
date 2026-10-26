from openai import AsyncOpenAI
from app.config import MODEL_BASE_URL, MODEL_ID

_client = AsyncOpenAI(base_url=MODEL_BASE_URL)

TRADITIONS = [
    "buddhist_theravada", "buddhist_mahayana", "taoist",
    "christian", "muslim", "hindu", "sikh", "bahai", "jain", "jewish",
]


async def classify_tradition(text: str) -> str:
    # TODO: swap to Muse Glimmer (open weight, Modal) for cost efficiency
    response = await _client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "system",
                "content": (
                    f"Classify the religious tradition of the following query. "
                    f"Reply with exactly one of: {', '.join(TRADITIONS)}. "
                    f"If unclear, reply 'unknown'."
                ),
            },
            {"role": "user", "content": text},
        ],
        max_tokens=20,
    )
    label = response.choices[0].message.content.strip().lower()
    return label if label in TRADITIONS else "unknown"
