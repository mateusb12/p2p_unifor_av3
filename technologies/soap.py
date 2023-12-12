from spyne import Application, rpc, ServiceBase, Iterable, ComplexModel, Array, Integer, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


# Defining complex data structures
class Comment(ComplexModel):
    _type_info = {
        'user_id': String,
        'content': String,
        'likes': Integer,
        'replies': Array(String),
        'created_at': String,
    }


class Post(ComplexModel):
    _type_info = {
        'title': String,
        'content': String,
        'comments': Array(Comment),
        'likes': Integer,
        'tags': Array(String),
        'updated_at': String,
    }


class UserActivity(ComplexModel):
    _type_info = {
        'likes': Array(String),
        'comments': Array(String),
    }


class User(ComplexModel):
    _type_info = {
        'name': String,
        'email': String,
        'friends': Array(String),
        'posts': Array(String),
        'activity': UserActivity,
    }


# Adjusted WeatherService to handle the new data structures
class DataService(ServiceBase):
    @rpc(String, _returns=User)
    def getUser(ctx, user_id):
        # Mock data retrieval logic
        user = User(
            name="John Doe",
            email="john@example.com",
            friends=["456", "789"],
            posts=["101", "102"],
            activity=UserActivity(
                likes=["201", "202"],
                comments=["301", "302"]
            )
        )
        return user

    @rpc(String, _returns=Post)
    def getPost(ctx, post_id):
        # Mock data retrieval logic
        post = Post(
            title="My First Post",
            content="Hello World!",
            comments=[Comment(user_id="123", content="Great post!", likes=3, replies=["401"],
                              created_at="2023-12-02T15:30:00Z")],
            likes=10,
            tags=["adventure", "travel"],
            updated_at="2023-12-01T12:00:00Z"
        )
        return post


# Creating a SOAP application
application = Application([DataService],
                          tns='myapp.soap.data',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

# Deploy the application using a WSGI server
if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 8000
    server = make_server(HOST, PORT, WsgiApplication(application))
    print("SOAP service is running...")
    print(f"WSDL is at: http://{HOST}:{PORT}/?wsdl")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
