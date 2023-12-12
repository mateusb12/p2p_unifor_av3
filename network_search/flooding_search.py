from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_search.search_utils import _get_backtracking_list, _flooding_helper
from network_structure.graph_object import Graph


def flooding_search(inputGraph: Graph, start_node_id: str, desiredResource: str, initial_ttl: int = 5) -> dict:
    visit_order, found, ttl_history, totalMessages, found_node = _flooding_helper(inputGraph, start_node_id,
                                                                                  desiredResource, initial_ttl,
                                                                                  False)
    return {
        "visited": visit_order, "found": found, "ttl_history": ttl_history, "totalMessages": totalMessages,
        "targetNode": found_node, "functionName": flooding_search.__name__,
        "backtrack": _get_backtracking_list(found_node)
    }


def search_pipeline():
    json_data = read_json("small_example.json")
    g = Graph(json_data)
    parse_res = parse_graph(inputGraph=g, graphRestraints=json_data)
    res = flooding_search(inputGraph=g, start_node_id="node_12", desiredResource="sunny_day.mp3",
                          initial_ttl=4)
    return


def __main():
    search_pipeline()
    return


if __name__ == "__main__":
    __main()
