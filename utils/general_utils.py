import networkx as nx

from json_parsing.json_read import read_json
from network_structure.graph_object import Graph


def convert_graph_to_networkx(input_graph: Graph) -> nx.Graph:
    G = nx.Graph()
    for node in input_graph.data.values():
        node_alias = node.node_id
        G.add_node(node_alias, info=node.resources, ttl=node.ttl)
        for neighbor in node.neighbors:
            weight = node.weighted_edges[neighbor.node_id]
            G.add_edge(node.node_id, neighbor.node_id, weight=weight)
    return G


def __main():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    nx_graph = convert_graph_to_networkx(g)
    return


if __name__ == "__main__":
    __main()
