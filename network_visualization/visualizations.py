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


def plotly_networkx(graph: nx.Graph, visited_nodes: List[str] = None):
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

    node_blue_marker_style = dict(showscale=False, color='LightSkyBlue', size=55, line=dict(width=2, color='RoyalBlue'))
    node_red_marker_style = dict(showscale=False, color='LightCoral', size=55, line=dict(width=2, color='Crimson'))
    hover_label_style = dict(bgcolor='DarkOrange', font=dict(color='LightYellow', size=13))

    node_trace_original = go.Scatter(x=node_x, y=node_y, mode='markers', hoverinfo='text', hovertemplate='%{text}',
                                     text=node_resources, marker=node_blue_marker_style, hoverlabel=hover_label_style)

    node_trace_red = go.Scatter(x=node_x, y=node_y, mode='markers', hoverinfo='text', hovertemplate='%{text}',
                                text=node_resources, marker=node_red_marker_style, hoverlabel=hover_label_style)

    text_trace_format = [f'•<br>{node}' for node in graph.nodes()]
    text_trace = go.Scatter(x=node_x, y=node_y, mode='text', text=text_trace_format,
                            hoverinfo='none', textposition="middle center", textfont=dict(color='Black', size=9))

    layout = go.Layout(title='<br>Network graph made with Python', titlefont=dict(size=16),
                       showlegend=False, hovermode='closest', margin=dict(b=20, l=5, r=5, t=40),
                       annotations=[dict(text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                                         showarrow=False, xref="paper", yref="paper", x=0.005, y=-0.002)],
                       xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

    fig = go.Figure(data=[edge_trace, node_trace_red, text_trace],
                    layout=layout)

    frames = [
        go.Frame(data=[edge_trace, node_trace_original, text_trace], name='frame1'),
        go.Frame(data=[edge_trace, node_trace_red, text_trace], name='frame2')
    ]

    fig.frames = frames

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
