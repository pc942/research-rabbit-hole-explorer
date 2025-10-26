from fastapi import FastAPI
app = FastAPI(title="RRH API", version="0.0.1")
@app.get("/health")
async def health(): return {"ok": True}
