import json

from path_references.all_references import get_technology_data_path


def get_user_data() -> dict:
    folder = get_technology_data_path()
    path = folder / "users.json"
    with open(path, 'r') as file:
        return json.load(file)


def get_song_data():
    folder = get_technology_data_path()
    path = folder / "songs.json"
    with open(path, 'r') as file:
        return json.load(file)


def get_playlist_data():
    folder = get_technology_data_path()
    path = folder / "playlists.json"
    with open(path, 'r') as file:
        return json.load(file)
