import httpx
from app.config import SOURCETRUTH_API_KEY, SOURCETRUTH_API_URL


async def retrieve_passages(query: str, tradition: str, k: int = 3) -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SOURCETRUTH_API_URL}/search",
            headers={"Authorization": f"Bearer {SOURCETRUTH_API_KEY}"},
            json={"query": query, "tradition": tradition, "k": k},
        )
        response.raise_for_status()
        return response.json()["results"]
