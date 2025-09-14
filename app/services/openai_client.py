from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def ask_openai(question: str, context: str) -> str:
    prompt = f"""
    You are an assistant answering based on the provided document.

    Question: {question}

    Relevant Context:
    {context}

    Answer clearly and concisely:
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
