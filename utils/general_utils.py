import random

import networkx as nx


def generate_random_ip_address():
    """
    Generates a random IP address.
    :return: A string representing an IP address.
    """
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))


def convert_graph_to_networkx(input_graph) -> nx.Graph:
    G = nx.Graph()
    for node in input_graph.data.values():
        node_to_be_added = node.node_id
        G.add_node(node_to_be_added, info=node.resources, ttl=node.ttl)
        for neighbor in node.neighbors:
            G.add_edge(node.node_id, neighbor.node_id)
    return G


def __main():
    random_ip = generate_random_ip_address()
    return


if __name__ == "__main__":
    __main()
