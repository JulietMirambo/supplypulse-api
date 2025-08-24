from fastapi import FastAPI
import os
from dotenv import load_dotenv
import redis

load_dotenv()

app = FastAPI(title="SupplyPulse API", version="0.1.0")

REDIS_URL = os.getenv("REDIS_URL", "")
r = redis.from_url(REDIS_URL) if REDIS_URL else None

@app.get("/health")
def health():
    return {"ok": True}
