from typing import List
import networkx as nx
from plotly.graph_objs import Scatter, Figure, Frame

from core_search.fundamental_searches import dfs_search, bfs_search
from json_files.json_read import read_and_parse_json
from network_search.flooding_search import search_pipeline
from network_structure.graph_object import Graph
import plotly.offline as pyo
import plotly.graph_objs as go
from utils.general_utils import convert_graph_to_networkx


def _add_sliders(fig: Figure, visited_nodes: List[str]):
    sliders_dict = {"active": 0, "yanchor": "top", "xanchor": "left",
                    "currentvalue": {"font": {"size": 20}, "prefix": "Visited:", "visible": True,
                                     "xanchor": "right"},
                    "transition": {"duration": 300, "easing": "cubic-in-out"}, "pad": {"b": 10, "t": 50},
                    "len": 0.9,
                    "x": 0.01, "y": 0, "steps": []
                    }
    visited_nodes.insert(0, "Start")
    for i, node in enumerate(visited_nodes):
        slider_step = {
            "args": [[f"frame{i + 1}"], {"frame": {"duration": 1000, "redraw": True}, "mode": "immediate",
                                         "transition": {"duration": 300}}], "label": node,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)
    fig.update_layout(sliders=[sliders_dict])


class NetworkGraphVisualizer:
    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.position = nx.spring_layout(graph)

    def __create_edge_trace(self):
        edge_x, edge_y = [], []
        for edge in self.graph.edges():
            x0, y0 = self.position[edge[0]]
            x1, y1 = self.position[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        return Scatter(x=edge_x, y=edge_y, line={"width": 2, "color": "#888"}, hoverinfo='none', mode='lines')

    def __get_node_plot_data(self):
        node_x, node_y, node_resources = [], [], []
        for node in self.graph.nodes():
            x, y = self.position[node]
            node_x.append(x)
            node_y.append(y)
            resources_info = '<br>'.join(self.graph.nodes[node]['info'])
            node_resources.append(resources_info)
        return node_x, node_y, node_resources

    def __get_text_trace(self, node_x: List[float], node_y: List[float]):
        node_labels = self.graph.nodes()
        text_trace_format = [f'•<br>{node}' for node in node_labels]
        return Scatter(x=node_x, y=node_y, mode='text', text=text_trace_format,
                       hoverinfo='none', textposition="middle center", textfont=dict(color='Black', size=9))

    def __get_hover_text_trace(self):
        node_resources = [item[1]['info'] for item in self.graph.nodes(data=True)]
        return ['<br>'.join([f'• {resource}' for resource in resources]) for resources in node_resources]

    def __get_node_trace(self, node_x: List[float], node_y: List[float], visited_nodes: List[str]):
        node_colors = ['LightCoral' if node in visited_nodes else 'LightSkyBlue' for node in self.graph.nodes()]
        node_marker_style = dict(showscale=False, size=55, line=dict(width=2, color='Black'))
        node_trace_format = self.__get_hover_text_trace()
        return Scatter(x=node_x, y=node_y, mode='markers', hoverinfo='text', hovertemplate='%{text}',
                       text=node_trace_format, marker=dict(node_marker_style, color=node_colors))

    def __get_animation_frames(self, node_x: List[float], node_y: List[float], edge_trace: Scatter,
                               text_trace: Scatter, node_trace_original: Scatter, visited_nodes: List[str]):
        frames = [Frame(data=[edge_trace, node_trace_original, text_trace], name='frame1')]
        for i, node in enumerate(visited_nodes):
            nodes_subset = visited_nodes[:i + 1]
            node_trace = self.__get_node_trace(node_x, node_y, nodes_subset)
            frame_name = f'frame{i + 2}'
            frames.append(go.Frame(data=[edge_trace, node_trace, text_trace], name=frame_name))
        return frames

    def plot_network(self, visited_nodes: List[str] = None):
        node_x, node_y, _ = self.__get_node_plot_data()
        edge_trace = self.__create_edge_trace()
        text_trace = self.__get_text_trace(node_x, node_y)
        node_trace_original = self.__get_node_trace(node_x, node_y, [])

        layout = go.Layout(title='<br>Network graph made with Python', titlefont=dict(size=16),
                           showlegend=False, hovermode='closest', margin=dict(b=20, l=5, r=5, t=40),
                           annotations=[dict(text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                                             showarrow=False, xref="paper", yref="paper", x=0.005, y=-0.002)],
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

        fig = Figure(data=[edge_trace, node_trace_original, text_trace], layout=layout)

        frames = self.__get_animation_frames(node_x, node_y, edge_trace, text_trace, node_trace_original, visited_nodes)
        fig.frames = frames

        _add_sliders(fig, visited_nodes)
        fig.update_layout(
            updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])])
        pyo.iplot(fig)


def __main():
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    graph = convert_graph_to_networkx(g)
    visualizer = NetworkGraphVisualizer(graph)
    # visited_nodes = bfs_search(graph)
    visited_nodes = search_pipeline()
    visualizer.plot_network(visited_nodes=visited_nodes)
    return


if __name__ == "__main__":
    __main()
