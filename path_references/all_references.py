from pathlib import Path
import sys


def get_main_folder_path() -> Path:
    """
    Returns the path of the main folder of the project.
    :return: Path
    """
    return Path(__file__).parent.parent


def append_main_folder_to_sys():
    main_folder_path = get_main_folder_path()
    sys.path.append(str(main_folder_path))
    return


def get_json_files_path() -> Path:
    """
    Returns the path of the folder containing the json files.
    :return: Path
    """
    return get_main_folder_path() / "json_parsing/json_files"


def get_network_tests_path() -> Path:
    """
    Returns the path of the folder containing the json files.
    :return: Path
    """
    return get_main_folder_path() / "network_tests"


append_main_folder_to_sys()


def __main():
    path = get_json_files_path()
    return


if __name__ == '__main__':
    __main()
