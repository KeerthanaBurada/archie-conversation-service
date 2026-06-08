import requests

from app.config import AI_ENGINE_URL


def send_to_ai(payload):

    response = requests.post(
        AI_ENGINE_URL,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    return response.json()