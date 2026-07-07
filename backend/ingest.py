from pathlib import Path

import chromadb
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("documents")

docs_path = Path("documents")


def read_pdf(path: Path) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


for file in docs_path.iterdir():
    if file.suffix.lower() == ".txt":
        text = file.read_text(encoding="utf-8")

    elif file.suffix.lower() == ".pdf":
        text = read_pdf(file)

    else:
        continue

    collection.add(
        ids=[file.stem],
        documents=[text],
        embeddings=[embedding_model.encode(text).tolist()],
    )

print(f"Indexed {collection.count()} documents.")