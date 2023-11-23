from graphviz import Digraph

from json_files.json_read import read_and_parse_json
from network_structure.network_object import Graph


def visualize_graph():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    dot = create_graphviz_graph(g)
    dot.render('output_graph.gv', view=True)


def create_graphviz_graph(graph):
    dot = Digraph(comment='The Network')

    # Add nodes
    for node in graph.data.values():
        dot.node(node.node_id, node.node_id)

    # Add edges
    for node in graph.data.values():
        for neighbor in node.neighbors:
            dot.edge(node.node_id, neighbor.node_id)

    return dot


def __main():
    visualize_graph()


if __name__ == "__main__":
    __main()
