from vector_store import collection, embedding_model


def retrieve(question: str, k: int = 3):

    embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k,
    )

    return {
        "documents": results["ids"][0],
        "context": "\n\n".join(results["documents"][0]),
    }