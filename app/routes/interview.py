from fastapi import APIRouter
from fastapi import HTTPException

from app.services.session_service import (
    get_session_payload
)

from app.services.problem_service import (
    get_problem
)

from app.services.payload_builder import (
    build_ai_payload
)

from app.services.ai_service import (
    send_to_ai
)

router = APIRouter()


@router.get("/prepare-ai-payload/{session_id}")
def prepare_ai_payload(session_id: str):

    session_payload = get_session_payload(
        session_id
    )

    problem = get_problem(
        session_payload["problem_id"]
    )

    ai_payload = build_ai_payload(
        session_payload,
        problem
    )

    return ai_payload


@router.post("/interview/{session_id}")
def interview(session_id: str):

    try:

        session_payload = get_session_payload(
            session_id
        )

        problem = get_problem(
            session_payload["problem_id"]
        )

        ai_payload = build_ai_payload(
            session_payload,
            problem
        )

        ai_response = send_to_ai(
            ai_payload
        )

        return {
            "status": "success",
            "response": ai_response
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )