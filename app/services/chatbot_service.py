import openai
from app.core.config import settings
from datetime import datetime
from app.services.hmis_service import get_patient_count_today

openai.api_key = settings.OPENAI_API_KEY

async def handle_query(query: str, user: dict):
    # Basic pattern match
    if "patients visited today" in query.lower():
        count = await get_patient_count_today(user)
        return {"answer": f"{count} patients visited today."}
    # Forward to GPT for basic fallback
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return {"answer": completion["choices"][0]["message"]["content"]}