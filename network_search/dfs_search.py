import random

from json_files.json_read import _read_json
from network_structure.network_object import Graph
from network_structure.node_object import Node


def is_connected(inputGraph: Graph):
    nodes = list(inputGraph.data.values())
    visited = []

    def dfs(inputNode: Node):
        visited.append(inputNode.node_id)
        neighbors = inputNode.neighbors
        for neighbor in neighbors:
            if neighbor.node_id not in visited:
                dfs(neighbor)

    starting_node = random.choice(nodes)
    dfs(starting_node)
    return {"result": len(visited) == len(nodes), "path": visited}


def __main():
    json_data = _read_json("json_example.json")
    g = Graph(json_data)
    res = is_connected(g)
    return


if __name__ == "__main__":
    __main()
