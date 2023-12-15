import grpc
from concurrent import futures
import streaming_pb2
import streaming_pb2_grpc
import json
import logging


class MusicService(streaming_pb2_grpc.MusicServiceServicer):

    def __init__(self):
        with open('../db/users.json', 'r') as file:
            self.users_data = json.load(file)

        with open('../db/songs.json', 'r') as file:
            self.songs_data = json.load(file)

        with open('../db/playlist.json', 'r') as file:
            self.playlists_data = json.load(file)

    def ListAllUsers(self, request, context):
        logging.info("Received ListAllUsers request")

        users = [streaming_pb2.User(id=user["id"], name=user["name"]) for user in self.users_data]
        for user in users:
            yield user

    def ListAllSongs(self, request, context):
        logging.info("Received ListAllSongs request")

        songs = [streaming_pb2.Song(id=song["id"], name=song["nome"], artist=song["artista"],
                                    category=song["categoria"], release_date=song["data_lancamento"]) for song in
                 self.songs_data]
        for song in songs:
            yield song

    def ListUserPlaylists(self, request, context):
        logging.info("Received ListUserPlaylists request")

        user_id = request.user_id  # Assuming you have user_id in the request
        user_playlists = [playlist["nome"] for playlist in self.playlists_data if playlist["id_usuario"] == user_id]

        for playlist_name in user_playlists:
            yield streaming_pb2.Playlist(name=playlist_name)

    def ListPlaylistSongs(self, request, context):
        logging.info("Received ListPlaylistSongs request")

        playlist_name = request.playlist_name  # Assuming you have playlist_name in the request
        playlist = next((playlist for playlist in self.playlists_data if playlist["nome"] == playlist_name), None)

        if playlist:
            song_ids = playlist.get("songs", [])
            songs = [streaming_pb2.Song(id=song["id"], name=song["nome"], artist=song["artista"],
                                        category=song["categoria"], release_date=song["data_lancamento"]) for song in
                     self.songs_data if song["id"] in song_ids]

            for song in songs:
                yield song

    def ListSongPlaylists(self, request, context):
        logging.info("Received ListSongPlaylists request")

        song_id = request.song_id  # Assuming you have song_id in the request
        song_playlists = [playlist["nome"] for playlist in self.playlists_data if song_id in playlist.get("songs", [])]

        for playlist_name in song_playlists:
            yield streaming_pb2.Playlist(name=playlist_name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    streaming_pb2_grpc.add_MusicServiceServicer_to_server(MusicService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
