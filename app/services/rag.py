from openai import OpenAI
import numpy as np
from typing import List
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def embed_texts(texts: List[str]) -> List[List[float]]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_relevant_chunks(question: str, chunks: List[str], k=3) -> List[str]:
    # Embed chunks and query
    chunk_embeddings = embed_texts(chunks)
    query_embedding = embed_texts([question])[0]

    # Rank by similarity
    scores = [cosine_similarity(query_embedding, ce) for ce in chunk_embeddings]
    ranked = sorted(zip(scores, chunks), key=lambda x: x[0], reverse=True)

    return [chunk for _, chunk in ranked[:k]]
