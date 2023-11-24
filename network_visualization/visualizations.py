import networkx as nx
from json_files.json_read import read_and_parse_json
from network_structure.graph_object import Graph
import plotly.offline as pyo
import plotly.graph_objs as go


def _convert_to_networkx(input_graph: Graph) -> nx.Graph:
    G = nx.Graph()
    for node in input_graph.data.values():
        node_to_be_added = node.node_id
        G.add_node(node_to_be_added, info=node.resources)
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

    edge_trace = go.Scatter(x=edge_x, y=edge_y, line={"width": 2, "color": "#888"}, hoverinfo='none', mode='lines')

    node_x = []
    node_y = []
    node_resources = []
    for node in graph.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        resources_info = '<br>'.join(graph.nodes[node]['info'])
        node_resources.append(resources_info)

    node_marker_style = dict(showscale=False, color='LightSkyBlue', size=55, line=dict(width=2, color='RoyalBlue'))
    hover_label_style = dict(bgcolor='DarkOrange', font=dict(color='LightYellow', size=13))

    node_trace = go.Scatter(x=node_x, y=node_y, mode='markers', hoverinfo='text', hovertemplate='%{text}',
                            text=node_resources, marker=node_marker_style, hoverlabel=hover_label_style)

    text_trace_format = [f'•<br>{node}' for node in graph.nodes()]
    text_trace = go.Scatter(x=node_x, y=node_y, mode='text', text=text_trace_format,
                            hoverinfo='none', textposition="middle center", textfont=dict(color='Black', size=9))

    fig = go.Figure(data=[edge_trace, node_trace, text_trace],
                    layout=go.Layout(title='<br>Network graph made with Python', titlefont=dict(size=16),
                                     showlegend=False, hovermode='closest', margin=dict(b=20, l=5, r=5, t=40),
                                     annotations=[dict(text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                                                       showarrow=False, xref="paper", yref="paper", x=0.005, y=-0.002)],
                                     xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                     yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                     paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)'))

    pyo.iplot(fig)


def visualize_graph():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    nx_graph = _convert_to_networkx(g)
    nx_graph_edges = list(nx_graph.edges)
    plotly_networkx(nx_graph)
    # net = pyvisNetwork(notebook=False, width="100%", height="700px", bgcolor="#222222", font_color="white")
    # _create_pyvis_graph(net, nx_graph, g, 'output_graph.html')


def __main():
    visualize_graph()


if __name__ == "__main__":
    __main()
