from json_parsing.json_read import read_json
from network_parse.dfs_parse import parse_graph
from network_structure.graph_object import Graph


def start_informed_random_walk_search(inputGraph: Graph, start_node_id: str, desiredResource: str,
                                      initial_ttl: int = 5) -> dict:
    visited_nodes = [start_node_id]
    ttl_history = [initial_ttl]

    current_node = start_node_id
    ttl = initial_ttl

    while ttl > 0:
        neighbors = inputGraph.get_neighbors(current_node)

        neighbors_with_resource = [neighbor for neighbor in neighbors
                                   if desiredResource in inputGraph.get_node_resources(neighbor)]

        if not neighbors_with_resource:
            return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history}

        next_node = random.choice(neighbors_with_resource)

        current_node = next_node
        ttl -= 1

        visited_nodes.append(current_node)
        ttl_history.append(ttl)

        if desiredResource in inputGraph.get_node_resources(current_node):
            return {"visited": visited_nodes, "found": True, "ttl_history": ttl_history}

    return {"visited": visited_nodes, "found": False, "ttl_history": ttl_history}


def __main():
    json_data = read_json("json_example.json")
    g = Graph(json_data)
    res = parse_graph(inputGraph=g, graphRestraints=json_data)
    return start_informed_random_walk_search(inputGraph=g, start_node_id="node_12", desiredResource="starry_skies.mp3",
                                             initial_ttl=5)


if __name__ == "__main__":
    __main()
