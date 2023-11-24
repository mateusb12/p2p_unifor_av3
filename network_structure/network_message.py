class NetworkMessage:
    def __init__(self, resource, origin, ttl=5):
        self.id = id(self)
        self.resource = resource
        self.origin = origin
        self.ttl = ttl
        self.path = []

    def add_node_to_path(self, node_id):
        self.path.append(node_id)

    def is_ttl_expired(self):
        return self.ttl <= 0


def __main():
    m = NetworkMessage("dancing_moon.mp3", "node_1")
    return


if __name__ == "__main__":
    __main()
