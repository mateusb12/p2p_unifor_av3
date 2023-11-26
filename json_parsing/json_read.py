from typing import Tuple

from path_references.all_references import get_json_files_path
import json
from pathlib import Path


def read_json(filename: str) -> dict or None:
    path = get_json_files_path() / filename
    try:
        with open(path, 'r') as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
        return None
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON.")
        return None


def _validate_node_neighborhood(neighbors: list, min_neighbors: int, max_neighbors: int) -> bool:
    return min_neighbors <= len(neighbors) <= max_neighbors


def _parse_json(json_data: dict) -> Tuple[bool, str]:
    if json_data is None:
        return False, "File not found."

    num_nodes = json_data.get("num_nodes")
    min_neighbors = json_data.get("min_neighbors")
    max_neighbors = json_data.get("max_neighbors")
    resources = json_data.get("resources", {})
    edges = json_data.get("edges", [])

    # Verificações básicas
    if not isinstance(num_nodes, int):
        return False, "Invalid data type for num_nodes. It should be integer."

    if not isinstance(min_neighbors, int):
        return False, "Invalid data type for min_neighbors. It should be integer."

    if not isinstance(max_neighbors, int):
        return False, "Invalid data type for max_neighbors. It should be integer."

    if not isinstance(resources, dict):
        return False, "Invalid data type for resources. It should be dict."

    if not isinstance(edges, list):
        return False, "Invalid data type for edges. It should be list."

    # Verifica se o número de nós e vizinhos está dentro dos limites
    if not (0 < num_nodes <= 1000):
        return False, "Invalid number of nodes. It should be between 1 and 1000."

    if not (0 <= min_neighbors <= max_neighbors):
        return False, f"Invalid number of neighbors. min_neighbors should be less than or equal to {max_neighbors}."

    # Constrói um dicionário para contar os vizinhos de cada nó
    neighbor_count = {node: [] for node in resources}
    for edge in edges:
        if edge.get("from") in neighbor_count and edge.get("to") in neighbor_count:
            neighbor_count[edge["from"]].append(edge["to"])
        else:
            return False, f"Invalid node in edge: {edge}"

    # Verifica se todos os nós têm o número correto de vizinhos
    for node, neighbors in neighbor_count.items():
        if not _validate_node_neighborhood(neighbors, min_neighbors, max_neighbors):
            return False, (f"Invalid number of neighbors for node {node}."
                           f" It should be between {min_neighbors} and {max_neighbors}.")

    return True, "Valid JSON"


def read_and_parse_json(filename: str) -> dict or str:
    json_content = read_json(filename)
    json_parse_result, json_parse_explanation = _parse_json(json_content)
    if json_parse_result:
        return json_content
    return json_parse_explanation


def __main():
    json_data = read_and_parse_json("json_files/json_example.json")
    return


if __name__ == '__main__':
    __main()
