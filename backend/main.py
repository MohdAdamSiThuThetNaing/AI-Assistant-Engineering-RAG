import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

load_dotenv()

app = FastAPI(title="Engineering AI Assistant RAG")

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

db = chromadb.PersistentClient(path="./chroma_db")
collection = db.get_or_create_collection("documents")

groq = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


class AnalyzeRequest(BaseModel):
    question: str


@app.on_event("startup")
def startup():
    if collection.count() > 0:
        return

    docs = Path("documents")

    for file in docs.glob("*.txt"):
        text = file.read_text()

        collection.add(
            ids=[file.stem],
            documents=[text],
            embeddings=[embedding_model.encode(text).tolist()],
        )


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/analyze")
def analyze(request: AnalyzeRequest):

    query = embedding_model.encode(request.question).tolist()

    results = collection.query(
        query_embeddings=[query],
        n_results=3,
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
Answer using ONLY this context.

{context}

Question:
{request.question}
"""

    response = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return {
        "documents": results["ids"][0],
        "answer": response.choices[0].message.content,
    }