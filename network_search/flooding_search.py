from json_files.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.network_message import NetworkMessage
from network_structure.graph_object import Graph


# def start_search(inputGraph: Graph, start_node_id: str, resource: str):
#     message = NetworkMessage(resource, start_node_id)
#     starting_node = inputGraph.data[start_node_id]
#     starting_node.receive_message(message)
#     return

def start_search(inputGraph: Graph):
    visited_nodes = []
    all_nodes = list(inputGraph.data.keys())
    queue = [all_nodes[0]]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)
            for neighbor in inputGraph.data[current_node].neighbors:
                queue.append(neighbor.node_id)
    return visited_nodes


def search_pipeline():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    # start_search(inputGraph=g, start_node_id="node_3", resource="sunny_day.mp3")
    return start_search(inputGraph=g)


def __main():
    search_pipeline()


if __name__ == "__main__":
    __main()
