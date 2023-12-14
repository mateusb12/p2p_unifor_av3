def dijkstra():
    return {
        "visited": visit_order, "found": found, "ttl_history": ttl_history, "totalMessages": totalMessages,
        "targetNode": found_node, "functionName": flooding_search.__name__,
        "backtrack": _get_backtracking_list(found_node) if found_node else None
    }