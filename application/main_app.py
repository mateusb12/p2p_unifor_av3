# app.py - your Flask application

from flask import Flask, render_template
import plotly.io as pio

app = Flask(__name__)


def generate_plotly_graph_html():
    # ... your code to setup the Plotly figure ...
    fig = ...  # the figure you created with the plot_network function
    return pio.to_html(fig, full_html=False)


@app.route('/')
def index():
    plotly_graph_html = generate_plotly_graph_html()
    return render_template('index.html', plotly_graph_html=plotly_graph_html)


if __name__ == '__main__':
    app.run(debug=True)
