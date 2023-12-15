from flask import Flask, jsonify

from path_references.load_references import get_user_data, get_song_data, get_playlist_data

app = Flask(__name__)
alL_users = get_user_data()
all_songs = get_song_data()
all_playlists = get_playlist_data()


@app.route('/get_all_users/', methods=['GET'])
def get_all_users():
    return jsonify(alL_users)


@app.route('/get_all_songs/', methods=['GET'])
def get_all_songs():
    return jsonify(all_songs)


@app.route('/get_playlists_by_user_id/<user_id>', methods=['GET'])
def get_playlists_by_user_id(user_id):
    user_playlists = [playlist for playlist in all_playlists if playlist["id_usuario"] == int(user_id)]
    return jsonify(user_playlists)


@app.route('/get_songs_by_playlist/<playlist_id>', methods=['GET'])
def get_songs_by_playlist(playlist_id):
    true_id = int(playlist_id)
    all_playlists = get_playlist_data()
    all_songs = get_song_data()
    playlist = next((playlist for playlist in all_playlists if playlist["id"] == int(playlist_id)), None)

    if playlist:
        songs_in_playlist = playlist.get("songs", [])
        return jsonify(songs_in_playlist)
    else:
        return jsonify([])


if __name__ == '__main__':
    PORT = 8000
    app.run(debug=True, port=PORT)
