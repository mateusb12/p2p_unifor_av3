from flask import Flask, render_template

from network_visualization.visualizations import generate_network_graph_html

app = Flask(__name__)


@app.route('/')
def index():
    graph_html = generate_network_graph_html("node_12", "mystic_river.mp3", 4)
    return render_template('html_visualization.html', plotly_graph_html=graph_html)


if __name__ == '__main__':
    app.run(debug=True)
