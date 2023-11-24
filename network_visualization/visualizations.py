from typing import List

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


def __create_edge_trace(position: dict, input_graph: nx.Graph):
    edge_x = []
    edge_y = []
    for edge in input_graph.edges():
        x0, y0 = position[edge[0]]
        x1, y1 = position[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    return go.Scatter(x=edge_x, y=edge_y, line={"width": 2, "color": "#888"}, hoverinfo='none', mode='lines')


def __get_node_plot_data(position: dict, input_graph: nx.Graph):
    node_x = []
    node_y = []
    node_resources = []
    for node in input_graph.nodes():
        x, y = position[node]
        node_x.append(x)
        node_y.append(y)
        resources_info = '<br>'.join(input_graph.nodes[node]['info'])
        node_resources.append(resources_info)
    return node_x, node_y, node_resources


def __get_text_trace(node_x: List[float], node_y: List[float], input_graph: nx.Graph):
    text_trace_format = [f'•<br>{node}' for node in input_graph.nodes()]
    return go.Scatter(x=node_x, y=node_y, mode='text', text=text_trace_format,
                      hoverinfo='none', textposition="middle center", textfont=dict(color='Black', size=9))


def __get_node_trace(node_x: List[float], node_y: List[float], input_graph: nx.Graph, visited_nodes: List[str]):
    node_trace_format = [f'•<br>{node}' for node in input_graph.nodes()]
    node_colors = ['LightCoral' if node in visited_nodes else 'LightSkyBlue' for node in input_graph.nodes()]
    node_marker_style = dict(showscale=False, size=55, line=dict(width=2, color='Black'))
    return go.Scatter(x=node_x, y=node_y, mode='markers', hoverinfo='text', hovertemplate='%{text}',
                      text=node_trace_format, marker=dict(node_marker_style, color=node_colors))


def __add_sliders(fig, visited_nodes):
    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Visited:",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": []
    }
    for i, node in enumerate(visited_nodes):
        slider_step = {"args": [
            [f"frame{i + 1}"],
            {"frame": {"duration": 1000, "redraw": True},
             "mode": "immediate",
             "transition": {"duration": 300}}
        ],
            "label": node,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)
    fig.update_layout(sliders=[sliders_dict])


def plotly_networkx(graph: nx.Graph, visited_nodes: List[str] = None):
    pos = nx.spring_layout(graph)

    node_x, node_y, node_resources = __get_node_plot_data(pos, graph)
    edge_trace = __create_edge_trace(pos, graph)
    text_trace = __get_text_trace(node_x, node_y, graph)

    node_trace_original = __get_node_trace(node_x, node_y, graph, [])
    node_trace_red = __get_node_trace(node_x, node_y, graph, ['node_4', 'node_6', 'node_5', 'node_7'])

    layout = go.Layout(title='<br>Network graph made with Python', titlefont=dict(size=16),
                       showlegend=False, hovermode='closest', margin=dict(b=20, l=5, r=5, t=40),
                       annotations=[dict(text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                                         showarrow=False, xref="paper", yref="paper", x=0.005, y=-0.002)],
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    fig = go.Figure(data=[edge_trace, node_trace_original, text_trace],
                    layout=layout)

    frames = [
        go.Frame(data=[edge_trace, node_trace_original, text_trace], name='frame1'),
        go.Frame(data=[edge_trace, node_trace_red, text_trace], name='frame2')
    ]

    fig.frames = frames

    __add_sliders(fig, visited_nodes)
    fig.update_layout(updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])])
    pyo.iplot(fig)


def visualize_graph():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    nx_graph = _convert_to_networkx(g)
    nx_graph_edges = list(nx_graph.edges)
    visited_nodes = ['node_1', 'node_2', 'node_3']
    plotly_networkx(nx_graph, visited_nodes)
    # net = pyvisNetwork(notebook=False, width="100%", height="700px", bgcolor="#222222", font_color="white")
    # _create_pyvis_graph(net, nx_graph, g, 'output_graph.html')


def __main():
    visualize_graph()


if __name__ == "__main__":
    __main()
