from fastapi import FastAPI
from app.api import auth, chatbot, hmis
from app.db import connect_to_mongo

app = FastAPI(title="Hospital Chatbot")

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(hmis.router, prefix="/hmis", tags=["HMIS"])