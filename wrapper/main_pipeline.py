from json_parsing.json_read import read_and_parse_json
from network_search.flooding_search import flooding_search
from network_search.informed_flooding_search import informed_flooding_search
from network_structure.graph_object import Graph
from network_visualization.visualizations import NetworkGraphVisualizer, generate_network_graph_html
from utils.general_utils import convert_graph_to_networkx


def search_through(filename: str, start_node_id: str, desired_resource: str, initial_ttl: int, function,
                   visualize: bool):
    json_data = read_and_parse_json(filename)
    if not isinstance(json_data, dict):
        print(json_data)
        return
    custom_graph = Graph(json_data)
    result = function(inputGraph=custom_graph, start_node_id=start_node_id, desiredResource=desired_resource,
                      initial_ttl=initial_ttl)
    graph = convert_graph_to_networkx(custom_graph)
    result["functionName"] = function.__name__
    if visualize:
        net_visualizer = NetworkGraphVisualizer(graph)
        net_visualizer.plot_network(result=result)
    visited_nodes = result["visited"]
    total_messages = result["totalMessages"]
    print(f"Algorithm chosen: {function.__name__}")
    print(f"Messages exchanged: {str(total_messages)}")
    print(f"Visited nodes: {str(visited_nodes)}")


def __main():
    filename = "small_example.json"
    starting_node = "node_12"
    desired_resource = "sunny_day.mp3"
    initial_ttl = 4
    function_pool = [flooding_search, informed_flooding_search]
    chosen_function = flooding_search
    visualize = True
    search_through(filename, starting_node, desired_resource, initial_ttl, chosen_function, visualize)
    return


if __name__ == "__main__":
    __main()
