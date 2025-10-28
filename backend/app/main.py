from fastapi import FastAPI
import asyncio
from app.retrieval.semantic_scholar import search_semantic_scholar
from app.retrieval.arxiv import search_arxiv

app = FastAPI(title="RRH API", version="0.0.2")

@app.get("/health")
async def health(): return {"ok": True}

@app.get("/ping-retrieval")
async def ping(q: str = "transformers"):
    ss, ax = await asyncio.gather(search_semantic_scholar(q, 3), search_arxiv(q, 2))
    return {"semantic_scholar": [p.model_dump() for p in ss], "arxiv": [p.model_dump() for p in ax]}
