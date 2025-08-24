from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import redis

load_dotenv()

app = FastAPI(title="SupplyPulse API", version="0.1.0")

# allow your dev frontends
origins = ["http://localhost:3002", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REDIS_URL = os.getenv("REDIS_URL", "")
r = redis.from_url(REDIS_URL) if REDIS_URL else None

@app.get("/health")
def health():
    return {"ok": True}
