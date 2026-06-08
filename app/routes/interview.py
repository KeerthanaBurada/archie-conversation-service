from fastapi import APIRouter
from fastapi import HTTPException

from app.services.session_service import get_session_payload
from app.services.problem_service import get_problem
from app.services.payload_builder import build_ai_payload
from app.services.ai_service import send_to_ai

router = APIRouter()


@router.get("/prepare-ai-payload/{session_id}")
def prepare_ai_payload(session_id: str):

    try:

        print("\n===== STEP 1: SESSION =====")

        session_payload = get_session_payload(
            session_id
        )

        print(session_payload)

        print("\n===== STEP 2: PROBLEM =====")

        problem = get_problem(
            session_payload["problem_id"]
        )

        print(problem)

        print("\n===== STEP 3: BUILD PAYLOAD =====")

        ai_payload = build_ai_payload(
            session_payload,
            problem
        )

        print(ai_payload)

        return ai_payload

    except Exception as e:

        print("\n===== ERROR =====")
        print(type(e))
        print(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/interview/{session_id}")
def interview(session_id: str):

    try:

        print("\n===== STEP 1: SESSION =====")

        session_payload = get_session_payload(
            session_id
        )

        print(session_payload)

        print("\n===== STEP 2: PROBLEM =====")

        problem = get_problem(
            session_payload["problem_id"]
        )

        print(problem)

        print("\n===== STEP 3: BUILD PAYLOAD =====")

        ai_payload = build_ai_payload(
            session_payload,
            problem
        )

        print(ai_payload)

        print("\n===== STEP 4: AI CALL =====")

        ai_response = send_to_ai(
            ai_payload
        )

        print(ai_response)

        return {
            "status": "success",
            "response": ai_response
        }

    except Exception as e:

        print("\n===== ERROR =====")
        print(type(e))
        print(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )