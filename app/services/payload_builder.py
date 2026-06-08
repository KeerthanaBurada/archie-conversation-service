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
        latest_canvas = snapshots[-1]["canvas_json"]

    return {
        "session_id": session_payload["session_id"],

        "problem": problem,

        "chat_history": session_payload["latest_history"],

        "canvas_snapshot": latest_canvas
    }