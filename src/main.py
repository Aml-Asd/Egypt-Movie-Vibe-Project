# backend/main.py  — AuraEgypt API v6.0
"""
Changes from v5.1:
- SSL bypass applied to ALL requests via session (not just some)
- price_per_night passed to build_trip for accurate tier detection
- build_booking_links removed — trip_builder handles it internally now
- budget_warning surfaced in build-trip response
- version bumped to 6.0
"""

import os
import ssl
import urllib3

os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("HF_DATASETS_OFFLINE",  "1")
os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), ".model_cache"))

ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import json, time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from matcher         import AuraMatcher
from agent           import PharaonicAgent
from trip_builder    import build_trip
from cache_manager   import CacheManager
from social_reranker import SocialReranker
from emotion_engine  import emotion_engine
from lore_db         import lore_db
from database        import ASWAN_LOCATIONS

try:
    from visual_engine import visual_engine
    VISUAL_OK = True
except Exception:
    VISUAL_OK = False
    print("[startup] visual_engine unavailable — using default score 60")

def _make_session() -> requests.Session:
    s = requests.Session()
    s.verify = False
    retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    s.mount("https://", adapter)
    s.mount("http://",  adapter)
    return s

session = _make_session()

app = FastAPI(title="AuraEgypt API", version="6.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "*"],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

GROQ_KEY = os.environ.get("GROQ_API_KEY", "")
TMDB_KEY = os.environ.get("TMDB_API_KEY", "")
B2B_KEY  = os.environ.get("B2B_API_KEY",  "aura-demo-key")

matcher  = AuraMatcher()
agent    = PharaonicAgent(GROQ_KEY)
cache    = CacheManager()
reranker = SocialReranker()

GENRE_MAP = {
    28:"Action", 12:"Adventure", 16:"Animation", 35:"Comedy", 80:"Crime",
    99:"Documentary", 18:"Drama", 10751:"Family", 14:"Fantasy", 36:"History",
    27:"Horror", 10402:"Musical", 9648:"Mystery", 10749:"Romance",
    878:"Science Fiction", 53:"Thriller",
}

if __name__ == "__main__":
    import uvicorn
    print("AuraEgypt API v6.0 starting on port 8005...")
    uvicorn.run(app, host="0.0.0.0", port=8005)
