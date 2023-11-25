from json_files.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.network_message import NetworkMessage
from network_structure.graph_object import Graph


def start_search(inputGraph: Graph, start_node_id: str, desiredResource: str) -> dict:
    visited_nodes = []
    initial_ttl = 5
    to_be_visited = [(start_node_id, initial_ttl)]
    while to_be_visited:
        current_node_label, current_ttl = to_be_visited.pop(0)
        current_node = inputGraph.data[current_node_label]
        if desiredResource in current_node.resources:
            return {"visited": visited_nodes, "found": True}
        if current_ttl <= 0:
            continue
        if current_node_label not in visited_nodes:
            visited_nodes.append(current_node_label)
            for neighbor in inputGraph.data[current_node_label].neighbors:
                new_ttl = current_ttl - 1
                to_be_visited.append((neighbor.node_id, new_ttl))
    return {"visited": visited_nodes, "found": False}


def search_pipeline():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    # start_search(inputGraph=g, start_node_id="node_3", resource="sunny_day.mp3")
    return start_search(inputGraph=g, start_node_id="node_6", desiredResource="cosmic_journey.mp3")


def __main():
    result = search_pipeline()
    return


if __name__ == "__main__":
    __main()
