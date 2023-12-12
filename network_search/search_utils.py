from typing import List

from network_structure.node_object import Node


def _get_backtracking_list(target_node: Node) -> List[str]:
    backtrack_list = [target_node.node_id]
    while target_node.previous is not None:
        target_node = target_node.previous
        backtrack_list.append(target_node.node_id)
    return backtrack_list


def _set_ttl(input_node: Node, new_ttl: int):
    if input_node.ttl == float("inf"):
        input_node.ttl = new_ttl


def _check_found_condition(desired_resource: str, current_node: Node, use_cache: bool) -> bool:
    if use_cache:
        if desired_resource in current_node.resources or desired_resource in current_node.cache:
            return True
    else:
        if desired_resource in current_node.resources:
            return True
    return False


def _search_helper(inputGraph, start_node_id, desiredResource, initial_ttl, use_cache):
    visit_order = []
    ttl_history = []
    to_be_visited = [(start_node_id, initial_ttl)]
    found = "None"
    totalMessages = 0
    current_node = None

    while to_be_visited:
        current_node_label, current_ttl = to_be_visited.pop(0)
        current_node = inputGraph.data[current_node_label]
        _set_ttl(input_node=current_node, new_ttl=current_ttl)
        found_condition = _check_found_condition(desired_resource=desiredResource, current_node=current_node,
                                                 use_cache=use_cache)
        if found_condition:
            visit_order.append(current_node_label)
            ttl_history.append(current_ttl)
            found = current_node_label
            continue

        if current_ttl <= 0:
            visit_order.append(current_node_label)
            ttl_history.append(current_ttl)
            continue

        if current_node_label not in visit_order:
            visit_order.append(current_node_label)
            new_ttl = current_ttl - 1
            ttl_history.append(current_ttl)
            for neighbor in current_node.neighbors:
                if neighbor.node_id not in visit_order and new_ttl >= 0:
                    totalMessages += 1
                    to_be_visited.append((neighbor.node_id, new_ttl))
                    inputGraph.data[neighbor.node_id].previous = current_node

    found_node = inputGraph.data[found] if found != "None" else None
    return visit_order, found, ttl_history, totalMessages, found_node
