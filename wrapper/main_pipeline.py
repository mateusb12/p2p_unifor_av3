from json_parsing.json_read import read_and_parse_json


def search_through(filename: str):
    json_data = read_and_parse_json("json_example.json")
    if not isinstance(json_data, dict):
        print(json_data)
        return
    return


def __main():
    search_through("json_example.json")


if __name__ == "__main__":
    __main()
