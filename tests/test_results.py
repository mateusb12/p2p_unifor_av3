from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from network_search.flooding_search import flooding_search
from network_search.informed_flooding_search import informed_flooding_search
from network_search.random_walk_search import start_random_walk_search
from network_search.informed_random_walk_search import start_informed_random_walk_search
from path_references.all_references import get_network_tests_path
from wrapper.main_pipeline import get_search_result

function_table = {
    "flooding_search": flooding_search,
    "informed_flooding_search": informed_flooding_search,
    "random_walk_search": start_random_walk_search,
    "informed_random_walk_search": start_informed_random_walk_search
}
TEST_FILENAME = "test_table.csv"


def load_tests() -> pd.DataFrame:
    file_path = Path(get_network_tests_path(), TEST_FILENAME)
    return pd.read_csv(file_path)


def run_test(filename: str, starting_node: str, desired_resource: str, initial_ttl: int, chosen_function):
    result = get_search_result(filename, starting_node, desired_resource, initial_ttl, chosen_function)
    nodes_visited = len(result["visited"])

    # Verifica se a chave "message_amount" está presente no resultado
    total_messages = result.get("message_amount", result.get("totalMessages", 0))

    return nodes_visited, total_messages


def loop_through_tests(input_df: pd.DataFrame):
    methods = list(function_table.keys())
    for method in methods:
        input_df[method + "_nodes_visited"] = 0
        input_df[method + "_message_amount"] = 0

    for index, row in input_df.iterrows():
        filename = row["filename"]
        starting_node = row["starting_node"]
        desired_resource = row["target_resource"]
        initial_ttl = row["initial_ttl"]

        for method, function in function_table.items():
            nodes_visited, total_messages = run_test(filename, starting_node, desired_resource, initial_ttl, function)
            input_df.at[index, method + "_nodes_visited"] = nodes_visited
            input_df.at[index, method + "_message_amount"] = total_messages

    input_df.to_csv(Path(get_network_tests_path(), TEST_FILENAME), index=False)

    # Generate and save comparative plots
    generate_comparison_plots(input_df, methods)


def generate_comparison_plots(df: pd.DataFrame, methods: list):
    bar_width = 0.2
    index = np.arange(len(df))

    for metric in ["nodes_visited", "message_amount"]:
        plt.figure(figsize=(12, 8))

        for i, method in enumerate(methods):
            plt.bar(index + i * bar_width, df[method + f"_{metric}"], bar_width, label=f"{method}", alpha=0.7)

        plt.xlabel('Test Filename')
        plt.ylabel(metric.replace('_', ' ').title())
        plt.title(f'Comparison of {metric.replace("_", " ").title()} in Tests')
        plt.xticks(index + bar_width * (len(methods) - 1) / 2, df["filename"], rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        # plt.savefig(Path(get_network_tests_path(), f'{metric}_comparison_plot.png'))
        plt.show()


def __main():
    df = load_tests()
    loop_through_tests(df)
    generate_comparison_plots(df, list(function_table.keys()))


if __name__ == '__main__':
    __main()
