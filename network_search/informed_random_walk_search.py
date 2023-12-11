from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.graph_object import Graph
from typing import List
import random


def start_informed_random_walk_search(inputGraph: Graph, start_node_id: str, desiredResource: str,
                                      initial_ttl: int = 5) -> dict:
    visited_nodes = []
    ttl_history = []

    current_node_id = start_node_id
    ttl = initial_ttl

    while ttl > 0:
        visited_nodes.append(current_node_id)
        ttl_history.append(ttl)

        if desiredResource in inputGraph.get_node_resources(current_node_id):
            return {"visited": visited_nodes, "found": True, "ttl_history": ttl_history}

        neighbors = [neighbor.node_id for neighbor in inputGraph.data[current_node_id].get_neighbors()]

        if neighbors:
            current_node_id = random.choice(neighbors)
        else:
            break
        ttl -= 1

    return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history}


def __main():
    json_data = read_json("json_example.json")
    g = Graph(json_data)

    print("Available Node IDs:", list(g.data.keys()))

    result = start_informed_random_walk_search(g, start_node_id="node_1", desiredResource="dancing_moon.mp3")
    print(result)

if __name__ == "__main__":
    __main()

