from typing import List

import networkx as nx

from json_files.json_read import read_and_parse_json
from network_structure.graph_object import Graph
from utils.general_utils import convert_graph_to_networkx


def dfs_search(inputGraph: nx.Graph) -> List[str]:
    visited_nodes = []
    all_nodes = list(inputGraph.nodes())
    stack = [all_nodes[0]]
    while stack:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            for neighbor in inputGraph[current_node]:
                stack.append(neighbor)
    return visited_nodes


def bfs_search(inputGraph: nx.Graph) -> List[str]:
    visited_nodes = []
    all_nodes = list(inputGraph.nodes())
    queue = [all_nodes[0]]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            for neighbor in inputGraph[current_node]:
                queue.append(neighbor)
    return visited_nodes


def __main():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    graph = convert_graph_to_networkx(g)
    visited_nodes = dfs_search(graph)
    return


if __name__ == "__main__":
    __main()
