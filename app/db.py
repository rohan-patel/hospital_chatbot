from motor.motor_asyncio import AsyncIOMotorClient

mongo_client = None

def get_db():
    return mongo_client["hospital_db"]

async def connect_to_mongo():
    global mongo_client
    mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")