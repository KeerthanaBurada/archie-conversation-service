def clean_canvas(canvas_snapshot):

    nodes = []

    for node in canvas_snapshot.get("nodes", []):

        nodes.append({
            "id": node.get("id"),
            "type": node.get("type", "component"),
            "data": {
                "label": node.get("label", "")
            }
        })

    edges = []

    for edge in canvas_snapshot.get("edges", []):

        edges.append({
            "source": edge.get("from"),
            "target": edge.get("to")
        })

    return {
        "nodes": nodes,
        "edges": edges
    }