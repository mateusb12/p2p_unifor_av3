from json_files.json_read import read_and_parse_json


class Graph:
    def __init__(self, network_data: dict):
        self.data = network_data


def __main():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    return


if __name__ == "__main__":
    __main()
