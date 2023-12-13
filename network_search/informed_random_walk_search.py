from json_parsing.json_read import read_json
from network_structure.graph_object import Graph
import random

search_cache = {}


def update_local_cache(node, resource):
    node.cache[resource] = True


def clear_search_cache():
    search_cache.clear()


def start_informed_random_walk_search(inputGraph: Graph, start_node_id: str, desiredResource: str,
                                      initial_ttl: int = 5) -> dict:
    cache_key = (id(inputGraph), start_node_id, desiredResource, initial_ttl)

    if cache_key in search_cache:
        return search_cache[cache_key]

    visited_nodes = [start_node_id]
    ttl_history = [initial_ttl]
    totalMessages = 0
    backtrack_list = []

    current_node_id = start_node_id
    ttl = initial_ttl

    while ttl > 0:
        current_node = inputGraph.data.get(current_node_id)

        if not current_node:
            break

        neighbors = current_node.neighbors

        if neighbors:
            next_node = random.choice(neighbors)
            totalMessages += 1
            current_node_id = next_node.node_id

            # Verificar o cache local do nó para acelerar a busca
            if desiredResource in current_node.cache and current_node.cache[desiredResource]:
                # Recurso encontrado no cache local
                result = {"visited": visited_nodes, "found": True, "ttl_history": ttl_history,
                          "totalMessages": totalMessages, "backtrack": backtrack_list}

                # Armazenar os resultados no cache
                search_cache[cache_key] = result
                return result
        else:
            break

        visited_nodes.append(current_node_id)
        ttl_history.append(ttl)

        if desiredResource in inputGraph.get_node_resources(current_node_id):
            update_local_cache(current_node, desiredResource)

            result = {"visited": visited_nodes, "found": True, "ttl_history": ttl_history,
                      "totalMessages": totalMessages, "backtrack": backtrack_list}

            search_cache[cache_key] = result
            return result

        ttl -= 1

    result = {"visited": visited_nodes, "found": False, "ttl_history": ttl_history, "totalMessages": totalMessages,
              "backtrack": backtrack_list}

    search_cache[cache_key] = result
    return result


def __informed_search_pipeline():
    json_data = read_json("json_example.json")
    g = Graph(json_data)

    # Testar com cache
    result_with_cache = start_informed_random_walk_search(g, start_node_id="node_1", desiredResource="dancing_moon.mp3")
    print("Result with cache:")
    print_result(result_with_cache)

    clear_search_cache()

    # Testar sem cache
    result_without_cache = start_informed_random_walk_search(g, start_node_id="node_1", desiredResource="dancing_moon.mp3")
    print("Result without cache:")
    print_result(result_without_cache)


def print_result(result):
    print(f"Visited Nodes: {result['visited']}")
    print(f"Found: {result['found']}")
    print(f"TTL History: {result['ttl_history']}")
    print(f"Total Messages: {result['totalMessages']}")
    print(f"Backtrack: {result['backtrack']}")



def __main():
    __informed_search_pipeline()


if __name__ == "__main__":
    __main()
