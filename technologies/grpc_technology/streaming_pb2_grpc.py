# streaming_pb2_grpc.py
import grpc

import streaming_pb2 as streaming__pb2


class MusicServiceStub(object):
    """The music service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAllUsers = channel.unary_stream(
            '/streaming.MusicService/ListAllUsers',
            request_serializer=streaming__pb2.ListAllUsers.SerializeToString,
            response_deserializer=streaming__pb2.User.FromString,
        )

        self.ListAllSongs = channel.unary_stream(
            '/streaming.MusicService/ListAllSongs',
            request_serializer=streaming__pb2.ListAllSongs.SerializeToString,
            response_deserializer=streaming__pb2.Song.FromString,
        )

        self.ListUserPlaylists = channel.unary_stream(
            '/streaming.MusicService/ListUserPlaylists',
            request_serializer=streaming__pb2.ListUserPlaylists.SerializeToString,
            response_deserializer=streaming__pb2.Playlist.FromString,
        )

        self.ListPlaylistSongs = channel.unary_stream(
            '/streaming.MusicService/ListPlaylistSongs',
            request_serializer=streaming__pb2.ListPlaylistSongs.SerializeToString,
            response_deserializer=streaming__pb2.Song.FromString,
        )

        self.ListSongPlaylists = channel.unary_stream(
            '/streaming.MusicService/ListSongPlaylists',
            request_serializer=streaming__pb2.ListSongPlaylists.SerializeToString,
            response_deserializer=streaming__pb2.Playlist.FromString,
        )


class MusicServiceServicer(object):
    """The music service definition.
    """

    def ListAllUsers(self, request, context):
        """List all users."""
        # Your implementation here
        pass

    def ListAllSongs(self, request, context):
        """List all songs."""
        # Your implementation here
        pass

    def ListUserPlaylists(self, request, context):
        """List playlists for a user."""
        # Your implementation here
        pass

    def ListPlaylistSongs(self, request, context):
        """List songs in a playlist."""
        # Your implementation here
        pass

    def ListSongPlaylists(self, request, context):
        """List playlists containing a song."""
        # Your implementation here
        pass


def add_MusicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ListAllUsers': grpc.unary_stream_rpc_method_handler(
            servicer.ListAllUsers,
            request_deserializer=streaming__pb2.ListAllUsers.FromString,
            response_serializer=streaming__pb2.User.SerializeToString,
        ),
        'ListAllSongs': grpc.unary_stream_rpc_method_handler(
            servicer.ListAllSongs,
            request_deserializer=streaming__pb2.ListAllSongs.FromString,
            response_serializer=streaming__pb2.Song.SerializeToString,
        ),
        'ListUserPlaylists': grpc.unary_stream_rpc_method_handler(
            servicer.ListUserPlaylists,
            request_deserializer=streaming__pb2.ListUserPlaylists.FromString,
            response_serializer=streaming__pb2.Playlist.SerializeToString,
        ),
        'ListPlaylistSongs': grpc.unary_stream_rpc_method_handler(
            servicer.ListPlaylistSongs,
            request_deserializer=streaming__pb2.ListPlaylistSongs.FromString,
            response_serializer=streaming__pb2.Song.SerializeToString,
        ),
        'ListSongPlaylists': grpc.unary_stream_rpc_method_handler(
            servicer.ListSongPlaylists,
            request_deserializer=streaming__pb2.ListSongPlaylists.FromString,
            response_serializer=streaming__pb2.Playlist.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'streaming.MusicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
