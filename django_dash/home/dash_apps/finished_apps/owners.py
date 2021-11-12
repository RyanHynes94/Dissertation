import dash
import plotly.express as px
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('owners', external_stylesheets=external_stylesheets)

values = [430, 20, 19.4, 13.5, 13, 12.4, 10, 8.7, 8, 7.6] 
labels = ["Newcastle United", "Man City, Melbourne City, New York City", "Red Bull Salzburg, New York Red Bulls, RB Leipzig", "Juventus", "Hoffenheim", "Chelsea", "LA Galaxy", "Arsenal, Colorado Rapids", "Paris Saint Germain", "Inter"]
parents = ["", "", "", "", "", "", "", "", "", ""]
hovertext = ["Public Investment Fund", "Sheikh Mansour", "Dietrich Mateschitz", "Andrea Agnelli (and family)", "Dietmar Hopp", "Roman Abramovich", "Philip Anschutz", "Stan Kroenke", "Nasser Al-Khelaifi", "Zhang Jindong"]


figure = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    hovertext=hovertext,
    textinfo = "label+value",
    marker_colors = ["black", "lightblue", "red", "lightgrey", 
                     "royalblue", "cyan", "silver", "maroon", "darkblue", "skyblue",]
))

figure.update_layout(
    margin = dict(t=50, l=25, r=25, b=25),
    uniformtext=dict(minsize=30))

figure = dcc.Graph(id='graph1', figure=figure)

header = html.H2(children='The Wealth of Football Owners 2021')

intro = html.P(children='This Treemap graphic shows the wealth disparity of football club owners and some of them might surprise you!  values are in (billions)')
layout = html.Div(children=[header, intro, figure], style={"font-family": "helvetica"})

app.layout = layout