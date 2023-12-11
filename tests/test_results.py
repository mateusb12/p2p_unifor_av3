from pathlib import Path
import pandas as pd

from network_search.flooding_search import flooding_search
from network_search.informed_flooding_search import informed_flooding_search
from path_references.all_references import get_network_tests_path
from wrapper.main_pipeline import get_search_result

function_table = {"flooding_search": flooding_search, "informed_flooding_search": informed_flooding_search}
TEST_FILENAME = "test_table.csv"


def load_tests() -> pd.DataFrame:
    file_path = Path(get_network_tests_path(), TEST_FILENAME)
    return pd.read_csv(file_path)


def loop_through_tests(input_df: pd.DataFrame):
    for index, row in input_df.iterrows():
        filename = row["filename"]
        starting_node = row["starting_node"]
        desired_resource = row["target_resource"]
        initial_ttl = row["initial_ttl"]
        chosen_function = function_table[row["function"]]
        result = get_search_result(filename, starting_node, desired_resource, initial_ttl, chosen_function)
        nodes_visited = len(result["visited"])
        total_messages = result["totalMessages"]
        row["nodes_visited"] = nodes_visited
        row["total_messages"] = total_messages
    input_df.to_csv(Path(get_network_tests_path(), TEST_FILENAME), index=False)


def __main():
    df = load_tests()
    loop_through_tests(df)
    return


if __name__ == '__main__':
    __main()
