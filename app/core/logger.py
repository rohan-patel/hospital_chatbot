from datetime import datetime
from app.db import get_db

async def log_query(user_id, query):
    db = get_db()
    await db["audit_logs"].insert_one({
        "user": user_id,
        "query": query,
        "timestamp": datetime.utcnow()
    })