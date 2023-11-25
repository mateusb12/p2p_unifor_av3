from json_files.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.graph_object import Graph


def start_random_walk_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visited_nodes = []
    ttl_history = []

    # TODO: Implement random walk search

    return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history}


def __main():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    return start_random_walk_search(inputGraph=g, start_node_id="node_12", desiredResource="starry_skies.mp3",
                                    initial_ttl=5)


if __name__ == "__main__":
    __main()
