from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.gates.gate2_crisis import check_crisis
from app.routing.tradition_classifier import classify_tradition
from app.routing.intent_router import route_query
from app.retrieval.corpus_client import retrieve_passages
from app.models.spark_open import generate_response

app = FastAPI(title="Singapore End-of-Life Companion")


class QueryRequest(BaseModel):
    text: str
    language: str = "en"


@app.post("/query")
async def query(req: QueryRequest):
    crisis = check_crisis(req.text)
    if crisis:
        return crisis

    tradition = await classify_tradition(req.text)
    passages = await retrieve_passages(req.text, tradition)
    response = await route_query(req.text, tradition, passages)
    return {"tradition": tradition, "response": response, "passages": passages}


@app.get("/health")
def health():
    return {"status": "ok"}
