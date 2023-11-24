import webbrowser

import community as community_louvain
import networkx as nx
from pyvis.network import Network as pyvisNetwork

from network_structure.graph_object import Graph
from network_visualization.network_manipulation import update_edge


def _create_pyvis_graph(net: pyvisNetwork, nx_graph: nx.Graph, graph: Graph, output_filename: str):
    # Configure the physics layout of the network
    net.toggle_physics(True)  # Turn on physics simulation

    # Set node attributes for size and title
    communities = community_louvain.best_partition(nx_graph)
    node_degree = nx.degree_centrality(nx_graph)

    # Ensure the size is adequately scaled
    max_degree = max(node_degree.values())
    min_size = 100
    size_multiplier = 50  # Adjust this as needed to scale the node sizes

    for node in nx_graph.nodes():
        resources = graph.get_node_resources(node)
        size = min_size + size_multiplier * (node_degree[node] / max_degree)
        title = f"Resources: {resources}"
        group = communities[node]
        net.add_node(node, title=title, group=group, value=size)

    # Add edges
    for edge in nx_graph.edges():
        net.add_edge(edge[0], edge[1])
    update_edge(net, 'node_5', 'node_7', color="purple", width=3)

    # Generate and save the network graph
    net.save_graph(output_filename)
    webbrowser.open_new_tab(output_filename)
