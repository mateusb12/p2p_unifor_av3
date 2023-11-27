from typing import List
import networkx as nx
from plotly.graph_objs import Scatter, Figure, Frame

from core_search.fundamental_searches import dfs_search, bfs_search
from json_parsing.json_read import read_and_parse_json
from network_search.flooding_search import search_pipeline, flooding_search
from network_structure.graph_object import Graph
import plotly.offline as pyo
import plotly.graph_objs as go

from utils.general_utils import convert_graph_to_networkx


def _add_sliders(fig: Figure, visited_nodes: List[str], ttl_history: List[str]):
    sliders_dict = {"active": 0, "yanchor": "top", "xanchor": "left",
                    "currentvalue": {"font": {"size": 20},
                                     "prefix": "TTL:",
                                     "visible": True,
                                     "xanchor": "right"},
                    "transition": {"duration": 300, "easing": "cubic-in-out"}, "pad": {"b": 10, "t": 50},
                    "len": 0.9,
                    "x": 0.01, "y": 0, "steps": []
                    }
    visited_nodes.insert(0, "Start")
    ttl_history.insert(0, str(ttl_history[0]))
    for i, ttl in enumerate(ttl_history):
        slider_step = {
            "args": [[f"frame{i + 1}"], {"frame": {"duration": 1000, "redraw": True}, "mode": "immediate",
                                         "transition": {"duration": 300}}], "label": str(ttl),
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)
    fig.update_layout(sliders=[sliders_dict])


NODE_SIZE = 50
UNVISITED_NODE_COLOR = 'LightSkyBlue'
VISITED_NODE_COLOR = 'LightCoral'
ORIGIN_NODE_COLOR = 'Orange'
TARGET_NODE_COLOR = 'LightGreen'


class NetworkGraphVisualizer:
    def __init__(self, graph: nx.Graph):
        self.graph = graph
        self.position = nx.spring_layout(graph)
        self.node_x: List[float] = []
        self.node_y: List[float] = []
        self.node_resources: List[str] = []

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
        self.node_x = node_x
        self.node_y = node_y
        self.node_resources = node_resources
        return node_x, node_y, node_resources

    def __get_text_trace(self):
        node_labels = self.graph.nodes()
        text_trace_format = [f'•<br>{node}' for node in node_labels]
        return Scatter(x=self.node_x, y=self.node_y, mode='text', text=text_trace_format,
                       hoverinfo='none', textposition="middle center", textfont=dict(color='Black', size=9))

    def __get_hover_text_trace(self):
        node_resources = [item[1]['info'] for item in self.graph.nodes(data=True)]
        return ['<br>'.join([f'• {resource}' for resource in resources]) for resources in node_resources]

    def __get_node_trace(self, visited_nodes: List[str]):
        node_colors = [VISITED_NODE_COLOR if node in visited_nodes else UNVISITED_NODE_COLOR
                       for node in self.graph.nodes()]
        node_marker_style = dict(showscale=False, size=NODE_SIZE, line=dict(width=2, color='Black'))
        node_trace_format = self.__get_hover_text_trace()
        return Scatter(x=self.node_x, y=self.node_y, mode='markers', hoverinfo='text', hovertemplate='%{text}',
                       text=node_trace_format, marker=dict(node_marker_style, color=node_colors))

    def __get_animation_frames(self, edge_trace: Scatter, text_trace: Scatter, node_trace: Scatter,
                               visited_nodes: List[str], found: str = "None"):
        frames = [Frame(data=[edge_trace, node_trace, text_trace], name='frame1')]
        for i, node in enumerate(visited_nodes):
            nodes_subset = visited_nodes[:i + 1]
            node_trace = self.__get_node_trace(nodes_subset)
            frame_name = f'frame{i + 2}'
            frames.append(go.Frame(data=[edge_trace, node_trace, text_trace], name=frame_name))

        if found != "None" and visited_nodes:
            found_node_index = visited_nodes.index(found)
            self.__change_frame_color(frames=frames, visited_nodes=visited_nodes, frame_index=-1,
                                      node_index=found_node_index, color=TARGET_NODE_COLOR)
            self.__change_frame_color(frames=frames, visited_nodes=visited_nodes, frame_index=-1, node_index=0,
                                      color=ORIGIN_NODE_COLOR)
        return frames

    def __change_frame_color(self, frames: List[Frame], visited_nodes: List[str], frame_index: int, node_index: int,
                             color: str):
        desired_frame = frames[frame_index]
        desired_frame_colors = list(desired_frame.data[1].marker.color)
        desired_node = visited_nodes[node_index]
        node_index = list(self.graph.nodes()).index(desired_node)
        desired_frame_colors[node_index] = color
        desired_frame.data[1].marker.color = tuple(desired_frame_colors)

    def plot_network(self, visited_nodes: List[str] = None, found: str = "None", ttl_history: List[str] = None,
                     result=None):
        node_x, node_y, _ = self.__get_node_plot_data()
        edge_trace = self.__create_edge_trace()
        text_trace = self.__get_text_trace()
        node_trace_original = self.__get_node_trace([])

        messageAmount = result["totalMessages"]
        functionName = result["functionName"]
        layout = go.Layout(title=f'Function → {functionName}<br>Message amount → {messageAmount}'
                                 f'<br>Nodes visited → {len(visited_nodes)}',
                           titlefont=dict(size=16),
                           showlegend=False, hovermode='closest', margin=dict(b=20, l=5, r=5, t=40),
                           annotations=[dict(text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                                             showarrow=False, xref="paper", yref="paper", x=0.005, y=-0.002)],
                           xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                           paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

        fig = Figure(data=[edge_trace, node_trace_original, text_trace], layout=layout)

        frames = self.__get_animation_frames(edge_trace=edge_trace, text_trace=text_trace,
                                             node_trace=node_trace_original, visited_nodes=visited_nodes,
                                             found=found)
        fig.frames = frames

        _add_sliders(fig, visited_nodes, ttl_history)
        fig.update_layout(
            updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])])
        pyo.iplot(fig)
        return fig


def generate_network_graph_html(start_node_id, desired_resource, initial_ttl) -> str:
    json_data = read_and_parse_json("json_example.json")
    g = Graph(json_data)
    graph = convert_graph_to_networkx(g)
    visualizer = NetworkGraphVisualizer(graph)
    result = flooding_search(inputGraph=g, start_node_id=start_node_id, desiredResource=desired_resource,
                             initial_ttl=initial_ttl)
    visited_nodes = result["visited"]
    searchResult = result["found"]
    ttl_history = result["ttl_history"]

    fig = visualizer.plot_network(visited_nodes=visited_nodes, found=searchResult, ttl_history=ttl_history)
    graph_html = fig.to_html(fig, full_html=False)
    return graph_html


def __main():
    aux = generate_network_graph_html(start_node_id="node_12", desired_resource="mystic_river.mp3", initial_ttl=4)
    return


if __name__ == "__main__":
    __main()
