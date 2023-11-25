from json_files.json_read import read_and_parse_json
from network_structure.graph_object import Graph
from utils.general_utils import convert_graph_to_networkx


def __main():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    graph = convert_graph_to_networkx(g)
    return


if __name__ == "__main__":
    __main()
