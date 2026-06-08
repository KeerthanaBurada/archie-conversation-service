import requests

from app.config import (
    API_KEY,
    VARSHITHA_BASE_URL
)

headers = {
    "X-API-Key": API_KEY
}


def get_session_payload(session_id: str):

    response = requests.post(
        f"{VARSHITHA_BASE_URL}/api/sessions/{session_id}/send",
        headers=headers
    )

    response.raise_for_status()

    return response.json()["payload_sent"]