from app.utils.canvas_cleaner import clean_canvas


def build_ai_payload(
    session_payload,
    problem
):

    latest_canvas = {
        "nodes": [],
        "edges": []
    }

    snapshots = session_payload.get(
        "latest_canvas_snapshots",
        []
    )

    if snapshots:

        latest_canvas = clean_canvas(
            snapshots[-1]["canvas_json"]
        )

    history = session_payload.get(
        "latest_history",
        []
    )

    latest_message = ""

    for msg in reversed(history):

        if msg.get("role") == "user":

            latest_message = msg.get(
                "content",
                ""
            )

            break

    return {
        "session_id": session_payload["session_id"],

        "problem": problem,

        "chat_history": history,

        "message": latest_message,

        "canvas_snapshot": latest_canvas
    }