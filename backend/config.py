import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    AI_PROVIDER = os.getenv("AI_PROVIDER", "minimax")
    MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY", "")
    MINIMAX_API_URL = os.getenv("MINIMAX_API_URL", "https://api.minimax.chat/v1")
    FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))