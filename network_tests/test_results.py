from pathlib import Path
import pandas as pd

from path_references.all_references import get_network_tests_path


def __main():
    file_path = Path(get_network_tests_path(), "test_table.csv")
    df = pd.read_csv(file_path)
    return


if __name__ == '__main__':
    __main()
