from fastapi import APIRouter
from app.services.session_service import get_session_payload
from app.services.payload_builder import build_ai_payload

router = APIRouter()

@router.get("/test")
def test():
    return {"message": "working"}

@router.get("/prepare-ai-payload/{session_id}")
def prepare_payload(session_id: str):

    raw_data = get_session_payload(session_id)

    ai_payload = build_ai_payload(raw_data)

    return ai_payload