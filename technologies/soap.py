from spyne import Application, rpc, ServiceBase, Iterable, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import json


class MusicService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def list_all_users(self):
        with open('../db/users.json', 'r') as file:
            users_data = json.load(file)

        user_names = [user["name"] for user in users_data]
        return user_names

    @rpc(_returns=Iterable(Unicode))
    def list_all_songs(self):
        with open('../db/songs.json', 'r') as file:
            songs_data = json.load(file)

        songs_data = [song["nome"] for song in songs_data]
        return songs_data

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_user_playlists(self, id_usuario):
        with open('../db/user_playlists.json', 'r') as file:
            playlists_data = json.load(file)

        user_playlists = [playlist["nome"] for playlist in playlists_data if playlist["id_usuario"] == int(id_usuario)]
        return user_playlists

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_playlist_songs(self, nome):
        with open('../db/playlists.json', 'r') as file:
            playlists_data = json.load(file)

        playlist = next((playlist for playlist in playlists_data if playlist["nome"] == nome), None)

        if playlist:
            songs_in_playlist = playlist.get("songs", [])
            return songs_in_playlist
        else:
            return []


# Create the Spyne application
application = Application([MusicService], 'music.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    # Wrap the Spyne application with a WsgiApplication
    wsgi_application = WsgiApplication(application)

    # Create a simple WSGI server and run it
    server = make_server('localhost', 8000, wsgi_application)
    print("Listening on http://localhost:8000...")
    server.serve_forever()
