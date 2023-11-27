from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.network_message import NetworkMessage
from network_structure.graph_object import Graph


def flooding_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visited_nodes = []
    ttl_history = []
    to_be_visited = [(start_node_id, initial_ttl)]
    found = "None"
    totalMessages = 0
    while to_be_visited:
        current_node_label, current_ttl = to_be_visited.pop(0)
        current_node = inputGraph.data[current_node_label]
        if desiredResource in current_node.resources:
            visited_nodes.append(current_node_label)
            ttl_history.append(current_ttl)
            found = current_node_label
            continue
        if current_ttl < 0:
            continue
        if current_node_label not in visited_nodes:
            visited_nodes.append(current_node_label)
            new_ttl = current_ttl - 1
            totalMessages += 1
            ttl_history.append(current_ttl)
            for neighbor in inputGraph.data[current_node_label].neighbors:
                to_be_visited.append((neighbor.node_id, new_ttl))
    return {"visited": visited_nodes, "found": found, "ttl_history": ttl_history, "totalMessages": totalMessages}


def search_pipeline():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    # start_search(inputGraph=g, start_node_id="node_3", resource="sunny_day.mp3")
    return flooding_search(inputGraph=g, start_node_id="node_6", desiredResource="cosmic_journey.mp3",
                           initial_ttl=2)


def __main():
    result = search_pipeline()
    return


if __name__ == "__main__":
    __main()
