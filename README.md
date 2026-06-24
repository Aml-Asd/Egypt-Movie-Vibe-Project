# 🏛️ AuraEgypt — AI Travel Matching Platform

> **Match your movie mood to an Egyptian destination.**
> Live demo → [project-z8foo.vercel.app](https://project-z8foo.vercel.app)

AuraEgypt is a full-stack AI platform that takes a movie title and your MBTI personality type, extracts an emotional fingerprint from the film, and matches you to real destinations in Upper Egypt and the Red Sea coast using a hybrid scoring pipeline.

---

## ✨ How It Works

```
Movie Title + MBTI
      ↓
TMDB API → plot, genres, poster
      ↓
Emotion Engine (LLM) → core emotions, traveller archetype, atmosphere words
      ↓
Hybrid Scorer:
  • Semantic similarity (Sentence-Transformers + Pinecone)   35%
  • Budget fit                                               25%
  • Persona matching (MBTI)                                  20%
  • CLIP visual scoring                                      20%
      ↓
Social Re-ranker (rural boost, community impact)
      ↓
Cleopatra Narrative (Groq LLM)
      ↓
Trip Builder (flights, hotels, activities, booking links)
```

---

## 🏗️ Architecture

| Module | Description |
|---|---|
| `emotion_engine.py` | LLM-based emotional fingerprinting of movies |
| `matcher.py` | Pinecone vector search + static DB fallback |
| `social_reranker.py` | Boosts rural/community destinations |
| `lore_db.py` | Dynamic social-impact tier database |
| `trip_builder.py` | Budget breakdown, hotel/flight/activity links |
| `cache_manager.py` | Semantic cache (avoids redundant LLM calls) |
| `visual_engine.py` | CLIP-based image–text visual scoring |
| `agent.py` | Cleopatra narrative generation via Groq |
| `scout_agent.py` | Pinecone enrichment agent |
| `main.py` | FastAPI backend — 10+ endpoints |

---

## 🚀 Features

- **Vibe matching** — emotion-driven, not keyword-driven
- **Social impact scoring** — rural destinations get a boost to support local communities
- **Live booking links** — flights (TravelPayouts), hotels, activities, transfers
- **B2B API** — licensed partner endpoint for travel agencies
- **Streamlit ops dashboard** — What-If headway simulation, metadata audit
- **Semantic cache** — identical vibes reuse previous results
- **Egyptian ISP resilience** — SSL bypass, offline HuggingFace mode, retry logic

---

## 🛠️ Tech Stack

**Backend:** Python, FastAPI, Pinecone, HuggingFace Transformers, Sentence-Transformers, CLIP, Groq API, TMDB API, TravelPayouts  
**Frontend:** React, Vite, Tailwind CSS, Vercel  
**Dashboard:** Streamlit  
**ML/AI:** Semantic embeddings, CLIP visual scoring, LLM emotion extraction

---

## ⚙️ Setup

```bash
git clone https://github.com/Aml-Asd/Egypt-Movie-Vibe-Project
cd Egypt-Movie-Vibe-Project/src

pip install -r requirements.txt

# Create .env
GROQ_API_KEY=your_key
TMDB_API_KEY=your_key
PINECONE_API_KEY=your_key

uvicorn main:app --reload --port 8005
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/vibe-match` | Movie → destination matches |
| POST | `/api/build-trip` | Build full trip itinerary |
| POST | `/api/b2b/match` | B2B partner match endpoint |
| GET | `/api/health` | System health + cache stats |
| GET | `/api/lore/tiers` | Social impact tier database |
| GET | `/api/links/verify` | Verify all booking links live |
| GET | `/api/metadata/audit` | Flag locations with missing data |

---

## 👩‍💻 Author

**Aml Abdelrhman Ahmed Mohamed**  
B.Sc. Computer Science — AASTMT Aswan (GPA: 3.67/4.0 — Excellence)

