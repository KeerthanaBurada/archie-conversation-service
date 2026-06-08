import requests

from app.config import (
    SESSION_SERVICE_API_KEY,
    SESSION_SERVICE_URL
)

headers = {
    "X-API-Key": SESSION_SERVICE_API_KEY
}


def get_session_payload(session_id: str):

    response = requests.post(
        f"{SESSION_SERVICE_URL}/api/sessions/{session_id}/send",
        headers=headers
    )

    response.raise_for_status()

    return response.json()["payload_sent"]

def get_session_payload(session_id: str):

    print("URL:", f"{SESSION_SERVICE_URL}/api/sessions/{session_id}/send")
    print("HEADERS:", headers)

    response = requests.post(
        f"{SESSION_SERVICE_URL}/api/sessions/{session_id}/send",
        headers=headers
    )

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    response.raise_for_status()

    return response.json()["payload_sent"]