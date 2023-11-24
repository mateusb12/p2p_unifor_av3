import random

from json_files.json_read import _read_json
from network_structure.graph_object import Graph
from network_structure.node_object import Node


def parse_graph(inputGraph: Graph, graphRestraints: dict):
    nodes = list(inputGraph.data.values())
    min_neighbors = graphRestraints.get("min_neighbors")
    max_neighbors = graphRestraints.get("max_neighbors")
    visited = []

    def dfs(inputNode: Node):
        visited.append(inputNode.node_id)
        if not inputNode.resources:
            return {"result": "Graph should not have nodes without resources.", "path": visited}
        if not (min_neighbors <= len(inputNode.neighbors) <= max_neighbors):
            return {"result": "Graph should not have nodes with invalid number of neighbors.", "path": visited}
        if inputNode in inputNode.neighbors:
            return {"result": "Graph should not have self-referencing nodes.", "path": visited}
        neighbors = inputNode.neighbors
        for neighbor in neighbors:
            if neighbor.node_id not in visited:
                dfs(neighbor)

    starting_node = random.choice(nodes)
    dfs(starting_node)
    connected_result = len(visited) == len(nodes)
    connected_label = {True: "The graph is connected.",
                       False: "The graph is disconnected. There are unreachable nodes."}
    return {"result": connected_label[connected_result], "path": visited}


def __main():
    json_data = _read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    return


if __name__ == "__main__":
    __main()
