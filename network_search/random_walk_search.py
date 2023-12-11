from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.graph_object import Graph
import random


def start_random_walk_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visited_nodes = [start_node_id]
    ttl_history = [initial_ttl]
    message_count = 0

    current_node = inputGraph.data.get(start_node_id)

    if current_node is None:
        return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history, "message_amount": message_count}

    ttl = initial_ttl

    while ttl > 0:
        neighbors = current_node.neighbors

        if not neighbors:
            return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history, "message_amount": message_count}

        next_node = random.choice(neighbors)
        current_node = inputGraph.data.get(next_node)

        if current_node is None:
            return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history, "message_amount": message_count}

        ttl -= 1
        visited_nodes.append(next_node)
        ttl_history.append(ttl)
        message_count += 1

        print(f"Current Node: {next_node}, TTL: {ttl}, Visited Nodes: {visited_nodes}")

        if desiredResource in current_node.resources:
            return {"visited": visited_nodes, "found": True, "ttl_history": ttl_history, "message_amount": message_count}

    return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history, "message_amount": message_count}


def __main():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    result = start_random_walk_search(inputGraph=g, start_node_id="node_12", desiredResource="starry_skies.mp3", initial_ttl=5)
    print(result)


if __name__ == "__main__":
    __main()
