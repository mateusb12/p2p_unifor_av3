from json_parsing.json_read import read_and_parse_json
from network_search.flooding_search import start_flooding_search
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
    graph = convert_graph_to_networkx(custom_graph)
    result = function(inputGraph=custom_graph, start_node_id=start_node_id, desiredResource=desired_resource,
                      initial_ttl=initial_ttl)
    visited_nodes = result["visited"]
    searchResult = result["found"]
    ttl_history = result["ttl_history"]
    total_messages = result["totalMessages"]
    if visualize:
        net_visualizer = NetworkGraphVisualizer(graph)
        net_visualizer.plot_network(visited_nodes=visited_nodes, found=searchResult, ttl_history=ttl_history)
    print(f"Algorithm chosen: {function.__name__}")
    print(f"Messages exchanged: {str(total_messages)}")
    print(f"Visited nodes: {str(visited_nodes)}")
    return result


def __main():
    filename = "json_example.json"
    starting_node = "node_12"
    desired_resource = "mystic_river.mp3"
    initial_ttl = 3
    function = start_flooding_search
    visualize = True
    result = search_through(filename, starting_node, desired_resource, initial_ttl, function, visualize)
    return


if __name__ == "__main__":
    __main()
