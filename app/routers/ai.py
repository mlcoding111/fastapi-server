from fastapi import APIRouter, UploadFile, Form
from app.services.pdf_parser import extract_text_from_pdf
from app.services.rag import retrieve_relevant_chunks
from app.services.openai_client import ask_openai

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/ask")
async def ask_ai(file: UploadFile, question: str = Form(...)):

    # 1. Parse PDF
    text = extract_text_from_pdf(file.file)

    # 2. Split into chunks (naive split for prototype)
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]

    # 3. Retrieve relevant context
    relevant = retrieve_relevant_chunks(question, chunks)

    # 4. Ask OpenAI
    answer = ask_openai(question, "\n".join(relevant))

    return {"answer": answer}