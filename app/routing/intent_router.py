from app.models.spark_open import generate_response
from app.models.wonder import generate_deep_response

DEEP_THEOLOGY_TRADITIONS = {"buddhist_theravada", "buddhist_mahayana", "taoist", "hindu"}

DEEP_THEOLOGY_KEYWORDS = [
    "bardo", "rebirth", "reincarnation", "dharma", "karma",
    "sutra", "tao", "moksha", "nirvana", "eschatology",
]


def _needs_wonder(text: str, tradition: str) -> bool:
    text_lower = text.lower()
    return tradition in DEEP_THEOLOGY_TRADITIONS and any(
        kw in text_lower for kw in DEEP_THEOLOGY_KEYWORDS
    )


async def route_query(text: str, tradition: str, passages: list[dict]) -> str:
    if _needs_wonder(text, tradition):
        return await generate_deep_response(text, tradition, passages)
    return await generate_response(text, tradition, passages)
