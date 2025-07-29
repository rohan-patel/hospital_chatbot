# hospital_chatbot/app/api/hmis.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def hmis_status():
    return {"status": "HMIS connected"}
