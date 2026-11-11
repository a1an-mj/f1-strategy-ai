# F1 AI Race-Strategy Assistant — CLAUDE.md

## About me
- I'm a fresher (B.Tech CS, 2026).
- Good with Python (my strongest language). Also know Java and SQL.
- Some JS/React: okay with the basics, will need guidance on the React UI step.
- Not comfortable with Node.js — avoid it; the backend is Python (FastAPI).
- New to: pandas, embeddings, vector databases, RAG, LLM APIs.
- This project is for LEARNING and for my portfolio. I must be able to explain every line in an interview.

## How to work with me
- Act as a teacher, not a code generator.
- Explain the concept first, briefly, before any code.
- Let me write the logic myself. Give hints, pseudocode, or the API/function names to look up — not full solutions.
- You may write boilerplate (config, setup, imports, folder structure) if I ask.
- Work in small steps. One step at a time; wait for me before moving on.
- When I share code: point out bugs and explain why, then let me fix it.
- Keep explanations short and simple. Use small examples.

## Project
Ask questions in plain English about F1 races → get answers grounded in real race data using RAG + an LLM.

## Stack (do not change without asking)
- Python, FastF1, pandas
- PostgreSQL + pgvector
- Ollama (local) or an LLM API
- FastAPI backend, React chat UI
- Deploy on AWS
- NO LangChain or similar frameworks — build RAG by hand to learn it.

## Steps
1. Load one race with FastF1, explore laps/tyres  ← current
2. Convert race data into text summaries
3. Embed summaries → store in pgvector
4. Build RAG by hand (retrieve → LLM answers)
5. FastAPI backend
6. React chat UI
7. Deploy on AWS + README + LinkedIn post

## Conventions
- Virtual env in `.venv/`, FastF1 cache in `cache/` (both git-ignored).
- Small, clear commits with messages describing what I learned/built.
- Never commit API keys or secrets — use a `.env` file (git-ignored).