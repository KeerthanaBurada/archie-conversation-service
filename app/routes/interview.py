from fastapi import APIRouter

from app.services.session_service import get_session_payload
from app.services.problem_service import get_problem
from app.services.payload_builder import build_ai_payload

router = APIRouter()


@router.get("/prepare-ai-payload/{session_id}")
def prepare_ai_payload(session_id: str):

    session_payload = get_session_payload(session_id)

    problem = get_problem(
        session_payload["problem_id"]
    )

    ai_payload = build_ai_payload(
        session_payload,
        problem
    )

    return ai_payload