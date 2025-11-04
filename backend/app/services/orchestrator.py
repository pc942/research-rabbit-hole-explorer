import uuid
from app.agents.scout import run_scout
from app.agents.critic import run_critic
from app.agents.synthesiser import run_synthesiser

async def run_pipeline(seed: str) -> dict:
    run_id = str(uuid.uuid4())
    papers = await run_scout(seed)
    numbered = [(i+1, p["title"], p["url"]) for i, p in enumerate(papers[:10])]
    critic = run_critic(seed, [t for _, t, _ in numbered])
    review_md = run_synthesiser(seed, numbered)
    return {"run_id": run_id, "review_md": review_md, "critic_yaml": critic.get("yaml")}
