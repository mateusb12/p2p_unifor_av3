from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_search.search_utils import _get_backtracking_list, _flooding_helper
from network_structure.graph_object import Graph
from network_structure.node_object import Node


def informed_flooding_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visit_order, found, ttl_history, totalMessages, found_node = _flooding_helper(inputGraph, start_node_id,
                                                                                  desiredResource, initial_ttl,
                                                                                  True)
    return {
        "visited": visit_order, "found": found, "ttl_history": ttl_history, "totalMessages": totalMessages,
        "targetNode": found_node, "functionName": informed_flooding_search.__name__,
        "backtrack": _get_backtracking_list(found_node)
    }


def __informed_search_pipeline():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    starting_node = "node_12"
    resource = "winter_chill.mp3"
    return informed_flooding_search(inputGraph=g, start_node_id=starting_node, desiredResource=resource,
                                    initial_ttl=5)


def __main():
    result = __informed_search_pipeline()
    return


if __name__ == "__main__":
    __main()
