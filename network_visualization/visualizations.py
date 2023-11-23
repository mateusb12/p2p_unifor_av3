from pyvis.network import Network as pyvisNetwork
import networkx as nx
import community as community_louvain
import webbrowser
from json_files.json_read import read_and_parse_json
from network_structure.network_object import Graph
from network_visualization.network_manipulation import update_edge


def _convert_to_networkx(graph) -> nx.Graph:
    G = nx.Graph()
    for node in graph.data.values():
        G.add_node(node.node_id)
        for neighbor in node.neighbors:
            G.add_edge(node.node_id, neighbor.node_id)
    return G


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


def visualize_graph():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    nx_graph = _convert_to_networkx(g)
    net = pyvisNetwork(notebook=False, width="100%", height="700px", bgcolor="#222222", font_color="white")
    _create_pyvis_graph(net, nx_graph, g, 'output_graph.html')


def __main():
    visualize_graph()


if __name__ == "__main__":
    __main()
