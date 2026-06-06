def clean_canvas(canvas_snapshot):

    nodes = []

    for node in canvas_snapshot.get("nodes", []):

        nodes.append({
            "id": node.get("id"),
            "label": node.get("label")
        })

    edges = []

    for edge in canvas_snapshot.get("edges", []):

        edges.append({
            "source": edge.get("source"),
            "target": edge.get("target")
        })

    return {
        "nodes": nodes,
        "edges": edges
    }