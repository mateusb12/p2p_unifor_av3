from typing import List

from json_parsing.json_read import read_json
from network_structure.node_object import Node


class Graph:
    def __init__(self, network_data: dict):
        self.raw_data = network_data
        self.data = self.__initialize_nodes()
        self.message_path = []

    def __initialize_nodes(self) -> dict:
        edges = self.__get_edge_table()
        weighted_edges = self.__get_weighted_edge_table()
        nodes = self.raw_data.get("resources", {})
        node_pot = {}
        for node_alias, node_resources in nodes.items():
            new_node = Node(node_id=node_alias, resources=node_resources, node_network=self)
            node_pot[node_alias] = new_node
        for node_alias in nodes.keys():
            node_neighbors = edges.get(node_alias, [])
            node: Node = node_pot[node_alias]
            for neighbor in node_neighbors:
                if neighbor != node_alias:
                    node.add_neighbor(node_pot[neighbor])
                    node.weighted_edges = {key: value for key, value in weighted_edges[node_alias]}
        return node_pot

    def __get_edge_table(self) -> dict:
        edges = self.raw_data.get("edges", [])
        edge_table = {}
        for pair in edges:
            _from, _to = pair.get("from"), pair.get("to")

            if _from not in edge_table:
                edge_table[_from] = []
            if _to not in edge_table:
                edge_table[_to] = []

            edge_table[_from].append(_to)
            if _from != _to:  # Avoiding adding self-loop twice
                edge_table[_to].append(_from)
        return edge_table

    def __get_weighted_edge_table(self):
        edges = self.raw_data.get("edges", [])
        edge_table = {}
        for pair in edges:
            _from, _to = pair.get("from"), pair.get("to")
            weight = pair.get("weight")
            if _from not in edge_table:
                edge_table[_from] = []
            if _to not in edge_table:
                edge_table[_to] = []
            edge_table[_from].append((_to, weight))
            if _from != _to:
                edge_table[_to].append((_from, weight))
        return edge_table

    def get_node_resources(self, node_id: str) -> List[str]:
        return self.data[node_id].resources


def __main():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    return


if __name__ == "__main__":
    __main()
