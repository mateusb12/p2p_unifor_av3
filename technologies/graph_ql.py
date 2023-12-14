from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import graphene
from graphql import graphql
import uvicorn
from flask import Flask, jsonify, request
from flask_graphql import GraphQLView
from graphene import ObjectType, Schema, List, String, Int
import json


app = Flask(__name__)

# Your existing data loading code
with open('../db/users.json', 'r') as file:
    users_data = json.load(file)

with open('../db/songs.json', 'r') as file:
    songs_data = json.load(file)

with open('../db/playlist.json', 'r') as file:
    playlists_data = json.load(file)

# Define GraphQL types for your data
class UserType(ObjectType):
    id = Int()
    name = String()
    idade = Int()
    sexo = String()
    email = String()
    cep = String()

class SongType(ObjectType):
    id = Int()
    nome = String()
    artista = String()
    categoria = String()
    data_lancamento = String()

class PlaylistType(ObjectType):
    id_usuario = Int()
    nome = String()
    songs = List(SongType)

# Define GraphQL queries
class Query(ObjectType):
    list_all_users = List(UserType)
    list_all_songs = List(SongType)
    list_all_playlists = List(PlaylistType)

    def resolve_list_all_users(self, info):
        return users_data

    def resolve_list_all_songs(self, info):
        return songs_data

    def resolve_list_all_playlists(self, info):
        return playlist_data

# Create a GraphQL schema
schema = Schema(query=Query)

# Define the GraphQL route
@app.route('/graphql', methods=['POST'])
def graphql_handler():
    data = request.get_json()
    success, result = graphql(schema, data['query'])
    status_code = 200 if success else 400
    return JSONResponse(content=result, status_code=status_code)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
