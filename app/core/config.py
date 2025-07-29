import os

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    ALGORITHM = "HS256"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-key")

settings = Settings()