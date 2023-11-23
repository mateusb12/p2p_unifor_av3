from pyvis.network import Network


def update_edge(inputNetwork: Network, source: str, to: str, **options):
    """
    Update the properties of an edge in the network if it exists.

    :param inputNetwork: The Network instance.
    :param source: The 'from' node id of the edge.
    :param to: The 'to' node id of the edge.
    :param options: A dictionary of edge properties to update.
    """
    # Iterate over a copy of the edge list to safely modify the original list
    for edge in inputNetwork.edges[:]:
        if edge['from'] == source and edge['to'] == to:
            # Remove the old edge
            inputNetwork.edges.remove(edge)
            # Add a new edge with the updated properties
            inputNetwork.add_edge(source, to, **options)
            return  # Exit after updating the edge

    # Optionally handle the case where the edge does not exist
    print(f"No edge found from {source} to {to} to update.")
