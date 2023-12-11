from json_parsing.json_read import read_and_parse_json
from network_search.flooding_search import flooding_search
from network_search.informed_flooding_search import informed_flooding_search
from network_structure.graph_object import Graph
from network_visualization.visualizations import NetworkGraphVisualizer, generate_network_graph_html
from utils.general_utils import convert_graph_to_networkx


def get_search_result(filename: str, start_node_id: str, desired_resource: str, initial_ttl: int, function):
    json_data = read_and_parse_json(filename)
    if not isinstance(json_data, dict):
        print(json_data)
        return
    custom_graph = Graph(json_data)
    result = function(inputGraph=custom_graph, start_node_id=start_node_id, desiredResource=desired_resource,
                      initial_ttl=initial_ttl)
    result["functionName"] = function.__name__
    result["customGraph"] = custom_graph
    return result


def visualize_search(search_result: dict):
    custom_graph = search_result["customGraph"]
    function = search_result["functionName"]
    graph = convert_graph_to_networkx(custom_graph)
    net_visualizer = NetworkGraphVisualizer(graph)
    net_visualizer.plot_network(result=search_result)
    visited_nodes = search_result["visited"]
    total_messages = search_result["totalMessages"]
    print(f"Algorithm chosen: {function.__name__}")
    print(f"Messages exchanged: {str(total_messages)}")
    print(f"Visited nodes: {str(visited_nodes)}")


def run_batch(visualize: bool = True):
    filename = "json_example.json"
    starting_node = "node_21"
    desired_resource = "celestial_harmony.mp3"
    initial_ttl = 10
    function_pool = [flooding_search, informed_flooding_search]
    chosen_function = flooding_search
    result = get_search_result(filename, starting_node, desired_resource, initial_ttl, chosen_function)
    final_result = {"starting_node": starting_node, "target_resource": desired_resource, "initial_ttl": initial_ttl,
                    "function": str(chosen_function), "nodes_visited": len(result["visited"]),
                    "total_messages": result["totalMessages"]}
    if visualize:
        visualize_search(result)
    return


def __main():
    run_batch()


if __name__ == "__main__":
    __main()
