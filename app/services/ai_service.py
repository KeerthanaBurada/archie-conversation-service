import requests

from app.config import SHUBH_AI_URL


def send_to_ai(payload):

    response = requests.post(
        SHUBH_AI_URL,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    return response.json()