from pathlib import Path


def get_main_folder_path() -> Path:
    """
    Returns the path of the main folder of the project.
    :return: Path
    """
    return Path(__file__).parent.parent


def get_json_files_path() -> Path:
    """
    Returns the path of the folder containing the json files.
    :return: Path
    """
    return get_main_folder_path() / "json_parsing"


def __main():
    path = get_json_files_path()
    return


if __name__ == '__main__':
    __main()
