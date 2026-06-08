import requests

from app.config import (
    SESSION_SERVICE_API_KEY,
    SESSION_SERVICE_URL
)

headers = {
    "X-API-Key": SESSION_SERVICE_API_KEY
}


def get_problem(problem_id: str):

    response = requests.get(
        f"{SESSION_SERVICE_URL}/api/problems/{problem_id}",
        headers=headers
    )

    response.raise_for_status()

    return response.json()