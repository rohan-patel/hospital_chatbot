from fastapi import APIRouter, Depends
from app.core.security import role_required
from app.services.chatbot_service import handle_query
from app.core.logger import log_query

router = APIRouter()

@router.post("/")
async def chatbot_query(query: str, user = Depends(role_required(["Owner", "Admin", "Doctor", "Staff"]))):
    response = await handle_query(query, user)
    await log_query(user["username"], query)
    return response