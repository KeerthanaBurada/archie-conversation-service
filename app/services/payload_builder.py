from app.utils.canvas_cleaner import clean_canvas


def build_ai_payload(session_payload, problem):

    latest_canvas = {}

    snapshots = session_payload["latest_canvas_snapshots"]

    if snapshots:
        latest_canvas = snapshots[-1]["canvas_json"]

    return {
        "session_id": session_payload["session_id"],

        "problem": problem,

        "chat_history": session_payload["latest_history"],

        "canvas_snapshot": clean_canvas(
            latest_canvas
        )
    }