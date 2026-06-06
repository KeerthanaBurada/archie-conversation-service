import requests
from app.config import API_KEY, VARSHITHA_BASE_URL

headers = {
    "X-API-Key": API_KEY
}


def get_problem(problem_id: str):

    response = requests.get(
        f"{VARSHITHA_BASE_URL}/api/problems/{problem_id}",
        headers=headers
    )

    response.raise_for_status()

    return response.json()