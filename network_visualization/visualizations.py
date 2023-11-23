from pyvis.network import Network as pyvisNetwork
import networkx as nx
from json_files.json_read import read_and_parse_json
from network_structure.network_object import Graph
from network_visualization.deprecated_visualizations import _create_pyvis_graph
import plotly.offline as pyo
import plotly.graph_objs as go


def _convert_to_networkx(input_graph: Graph) -> nx.Graph:
    G = nx.Graph()
    for node in input_graph.data.values():
        G.add_node(node.node_id)
        for neighbor in node.neighbors:
            G.add_edge(node.node_id, neighbor.node_id)
    return G


def plotly_networkx(graph: nx.Graph):
    pos = nx.spring_layout(graph)

    edge_x = []
    edge_y = []
    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='#888'),  # Wider and darker edges for visibility
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,  # Not showing the scale for simplicity
            color='LightSkyBlue',  # Light blue color for nodes
            size=20,  # Larger node size for visibility
            line=dict(width=2, color='RoyalBlue'))  # Blue border for nodes
    )

    # Add text separately to ensure it's on top of the nodes, and improve visibility
    text_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='text',
        text=['node_' + str(node) for node in graph.nodes()],
        hoverinfo='none',
        textposition="top center",
        textfont=dict(
            color='Black',
            size=12  # Adjust text size here
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace, text_trace],
                    layout=go.Layout(
                        title='<br>Network graph made with Python',
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                            showarrow=False, xref="paper", yref="paper",
                            x=0.005, y=-0.002 )],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
                        plot_bgcolor='rgba(0,0,0,0)'  # Transparent background
                    ))

    pyo.iplot(fig)


def visualize_graph():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    nx_graph = _convert_to_networkx(g)
    plotly_networkx(nx_graph)
    # net = pyvisNetwork(notebook=False, width="100%", height="700px", bgcolor="#222222", font_color="white")
    # _create_pyvis_graph(net, nx_graph, g, 'output_graph.html')


def __main():
    visualize_graph()


if __name__ == "__main__":
    __main()
