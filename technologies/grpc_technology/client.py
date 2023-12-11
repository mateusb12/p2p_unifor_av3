import grpc
import hello_world_pb2
import hello_world_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_world_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_world_pb2.HelloRequest(name='world'))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
