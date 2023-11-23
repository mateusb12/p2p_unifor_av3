from json_files.json_read import read_and_parse_json
from network_structure.node_object import Node
from graphviz import Digraph


class Graph:
    def __init__(self, network_data: dict):
        self.raw_data = network_data
        self.data = self.__initialize_nodes()

    def __initialize_nodes(self) -> dict:
        edges = self.__get_edge_table()
        nodes = self.raw_data.get("resources", {})
        node_pot = {}
        for node_alias, node_resources in nodes.items():
            new_node = Node(node_id=node_alias, resources=node_resources)
            node_pot[node_alias] = new_node
        for node_alias in nodes.keys():
            node_neighbors = edges.get(node_alias, [])
            node = node_pot[node_alias]
            for neighbor in node_neighbors:
                node.add_neighbor(node_pot[neighbor])
        return node_pot

    def __get_edge_table(self) -> dict:
        edges = self.raw_data.get("edges", [])
        edge_table = {}
        for pair in edges:
            _from, _to = pair.get("from"), pair.get("to")
            if _from not in edge_table:
                edge_table[_from] = []
            edge_table[_from].append(_to)
        return edge_table

    # def create_graphviz_graph(self):
    #     dot = Digraph(comment='The Network')
    #
    #     # Add nodes
    #     for node in self.data.values():
    #         dot.node(node.node_id, node.node_id)
    #
    #     # Add edges
    #     for node in self.data.values():
    #         for neighbor in node.neighbors:
    #             dot.edge(node.node_id, neighbor.node_id)
    #
    #     return dot


def __main():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    # dot = g.create_graphviz_graph()
    # dot.render('output_graph.gv', view=True)
    return


if __name__ == "__main__":
    __main()
