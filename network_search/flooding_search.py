import copy

from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.network_message import NetworkMessage
from network_structure.graph_object import Graph
from network_structure.node_object import Node


def __set_ttl(input_node: Node, new_ttl: int):
    if input_node.ttl == float("inf"):
        input_node.ttl = new_ttl


def flooding_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visit_order = []
    ttl_history = []
    to_be_visited = [(start_node_id, initial_ttl)]
    found = "None"
    totalMessages = 0
    while to_be_visited:
        current_node_label, current_ttl = to_be_visited.pop(0)
        current_node: Node = inputGraph.data[current_node_label]
        __set_ttl(input_node=current_node, new_ttl=current_ttl)
        if desiredResource in current_node.resources:
            visit_order.append(current_node_label)
            ttl_history.append(current_ttl)
            found = current_node_label
            continue
        if current_ttl <= 0:
            visit_order.append(current_node_label)
            continue
        if current_node_label not in visit_order:
            visit_order.append(current_node_label)
            new_ttl = current_ttl - 1
            ttl_history.append(current_ttl)
            for neighbor in inputGraph.data[current_node_label].neighbors:
                if neighbor not in visit_order and new_ttl >= 0:
                    totalMessages += 1
                    to_be_visited.append((neighbor.node_id, new_ttl))
    found_node = inputGraph.data[found] if found != "None" else None
    return {"visited": visit_order, "found": found, "ttl_history": ttl_history, "totalMessages": totalMessages,
            "targetNode": found_node, "functionName": flooding_search.__name__}


def search_pipeline():
    json_data = read_json("small_example.json")
    g = Graph(json_data)
    parse_res = parse_graph(inputGraph=g, graphRestraints=json_data)
    res = flooding_search(inputGraph=g, start_node_id="node_12", desiredResource="summer_samba.mp3",
                          initial_ttl=4)
    return


def __main():
    search_pipeline()
    return


if __name__ == "__main__":
    __main()
