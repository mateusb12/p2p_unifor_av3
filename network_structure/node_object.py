from utils.general_utils import generate_random_ip_address


class Node:
    def __init__(self, node_id: str, resources: list):
        self.node_id = node_id
        self.resources = resources
        self.neighbors = []
        self.ip = generate_random_ip_address()

    def add_neighbor(self, neighbor):
        """Add a neighbor to this node."""
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def remove_neighbor(self, neighbor):
        """Remove a neighbor from this node."""
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)

    def has_resource(self, resource: str) -> bool:
        """Check if the node has a specific resource."""
        return resource in self.resources

    def __repr__(self):
        return f"Node({self.node_id}, Resources: {self.resources}, Neighbors: {[n.node_id for n in self.neighbors]})"

    def receive_message(self, inputMessage):
        if inputMessage.is_ttl_expired():
            return
        if self.has_resource(inputMessage.resource):
            self.send_response(inputMessage)
        else:
            inputMessage.ttl -= 1
            inputMessage.add_node_to_path(self.node_id)
            self.forward_message(inputMessage)

    def forward_message(self, inputMessage):
        for neighbor in self.neighbors:
            if neighbor.node_id != inputMessage.path[-1]:  # Avoid sending back to the sender
                neighbor.receive_message(inputMessage)

    def send_response(self, message):
        # Implement the logic to send the response back to the origin
        pass


def __main():
    # Example usage
    node_1 = Node("node_1", ["dancing_moon.mp3", "echoes_of_spring.mp3"])
    node_2 = Node("node_2", ["rainy_night.mp3"])
    node_3 = Node("node_3", ["sunset_boulevard.mp3", "twilight_whispers.mp3"])

    # Add neighbors
    node_1.add_neighbor(node_2)
    node_2.add_neighbor(node_1)
    node_2.add_neighbor(node_3)

    # Print node information
    print(node_1)
    print(node_2)
    print(node_3)


if __name__ == "__main__":
    __main()
