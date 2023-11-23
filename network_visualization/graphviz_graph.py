from pyvis.network import Network
import networkx as nx
import community as community_louvain
import webbrowser
from json_files.json_read import read_and_parse_json
from network_structure.network_object import Graph


def visualize_graph():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    nx_graph = convert_to_networkx(g)
    create_pyvis_graph(nx_graph, 'output_graph.html')


def convert_to_networkx(graph):
    G = nx.Graph()
    for node in graph.data.values():
        G.add_node(node.node_id)
        for neighbor in node.neighbors:
            G.add_edge(node.node_id, neighbor.node_id)
    return G


def create_pyvis_graph(nx_graph, output_filename):
    net = Network(notebook=False, width="100%", height="700px", bgcolor="#222222", font_color="white")

    # Set node attributes for size and title
    communities = community_louvain.best_partition(nx_graph)
    node_degree = nx.degree_centrality(nx_graph)
    betweenness = nx.betweenness_centrality(nx_graph)
    closeness = nx.closeness_centrality(nx_graph)

    for node in nx_graph.nodes():
        title = f"Degree: {node_degree[node]:.2f}<br>Betweenness: {betweenness[node]:.2f}<br>Closeness: {closeness[node]:.2f}"
        group = communities[node]
        size = 10 + 20 * node_degree[node]  # Adjust size to be proportional to degree
        net.add_node(node, title=title, group=group, value=size)

    # Add edges
    for edge in nx_graph.edges():
        net.add_edge(edge[0], edge[1])

    # Generate and save the network graph
    net.save_graph(output_filename)
    webbrowser.open_new_tab(output_filename)


def __main():
    visualize_graph()


if __name__ == "__main__":
    __main()
