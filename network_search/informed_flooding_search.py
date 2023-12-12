from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.graph_object import Graph
from network_structure.node_object import Node


def informed_flooding_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visited_nodes = []
    ttl_history = []
    to_be_visited = [(start_node_id, initial_ttl, None)]
    last_visited_info = {}
    found = "None"
    totalMessages = 0
    backtrack_path = []

    while to_be_visited:
        current_node_label, current_ttl, last_visited = to_be_visited.pop(0)
        current_node: Node = inputGraph.data[current_node_label]

        if desiredResource in current_node.resources:
            visited_nodes.append(current_node_label)
            ttl_history.append(current_ttl)
            found = current_node_label
            last_visited_info[current_node_label] = last_visited
            continue

        if desiredResource in current_node.cache:
            visited_nodes.append(current_node_label)
            ttl_history.append(current_ttl)
            found = current_node.cache[desiredResource]["node_id"]
            last_visited_info[current_node_label] = last_visited
            continue

        if current_ttl < 0:
            continue

        if current_node_label not in visited_nodes:
            visited_nodes.append(current_node_label)
            new_ttl = current_ttl - 1
            totalMessages += 1
            ttl_history.append(current_ttl)
            last_visited_info[current_node_label] = last_visited

            for neighbor in inputGraph.data[current_node_label].neighbors:
                to_be_visited.append((neighbor.node_id, new_ttl, current_node_label))

    # Backtracking to find the path
    if found != "None":
        target_node_ip = inputGraph.data[found].ip
        backtrack_node_label = found
        while backtrack_node_label:
            backtrack_path.insert(0, backtrack_node_label)
            back_track_node: Node = inputGraph.data[backtrack_node_label]
            back_track_node.cache[desiredResource] = {"node_id": found, "node_ip": target_node_ip}
            backtrack_node_label = last_visited_info.get(backtrack_node_label)

    backtrack_path = backtrack_path[::-1]

    return {"visited": visited_nodes, "found": found, "ttl_history": ttl_history, "totalMessages": totalMessages,
            "backtrack_path": backtrack_path}


def __informed_search_pipeline():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    starting_node = "node_12"
    resource = "winter_chill.mp3"
    return informed_flooding_search(inputGraph=g, start_node_id=starting_node, desiredResource=resource,
                                    initial_ttl=5)


def __main():
    result = __informed_search_pipeline()
    return


if __name__ == "__main__":
    __main()
