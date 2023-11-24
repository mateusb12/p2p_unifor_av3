from json_files.json_read import _read_json
from network_parse.dfs_parse import parse_graph
from network_structure.network_message import NetworkMessage
from network_structure.graph_object import Graph


def start_search(inputGraph: Graph, start_node_id: str, resource: str):
    message = NetworkMessage(resource, start_node_id)
    starting_node = inputGraph.data[start_node_id]
    starting_node.receive_message(message)
    return


def __main():
    json_data = _read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    start_search(inputGraph=g, start_node_id="node_3", resource="sunny_day.mp3")
    return


if __name__ == "__main__":
    __main()
