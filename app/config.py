import os

SESSION_SERVICE_URL = os.getenv(
    "SESSION_SERVICE_URL",
    "https://sesson-handling.onrender.com"
)

SESSION_SERVICE_API_KEY = os.getenv(
    "SESSION_SERVICE_API_KEY",
    ""
)

AI_ENGINE_URL = os.getenv(
    "AI_ENGINE_URL",
    "http://localhost:8001/chat"
)