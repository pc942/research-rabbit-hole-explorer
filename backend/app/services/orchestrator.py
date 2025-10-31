from app.agents.scout import run_scout
async def run_pipeline(seed: str) -> dict:
    papers = await run_scout(seed)
    return {"run_id": "dev", "papers": papers}
