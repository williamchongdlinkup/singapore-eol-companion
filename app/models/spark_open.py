from openai import AsyncOpenAI
from app.config import MODEL_BASE_URL, MODEL_ID

_client = AsyncOpenAI(base_url=MODEL_BASE_URL)

SYSTEM_PROMPT = """You are a compassionate spiritual companion supporting patients and families
in an end-of-life care setting in Singapore. You ground every response in authoritative
religious texts — never fabricate scripture. You cite the source passage provided.
You do not offer medical advice. You escalate to human support when the conversation
exceeds your scope."""


async def generate_response(text: str, tradition: str, passages: list[dict]) -> str:
    context = "\n\n".join(
        f"[{p.get('corpus', '')}] {p.get('text', '')}" for p in passages
    )
    response = await _client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Tradition: {tradition}\n\nSource passages:\n{context}\n\nQuestion: {text}",
            },
        ],
        extra_body={"reasoning_effort": "xhigh"},
    )
    return response.choices[0].message.content
