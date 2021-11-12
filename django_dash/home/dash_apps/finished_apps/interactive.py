import plotly.express as px
from dash import dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from django_plotly_dash import DjangoDash

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('interactive', external_stylesheets=external_stylesheets) 

df = pd.read_csv('Prem_team_stats19-20.csv')

teams = df.team_name.unique()

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in teams],
        value=teams[0],
        clearable=True,
        searchable=True,
        style={'width':"100%", 'font-family': 'helvetica' },
    ),
    dcc.Graph(id="bar-chart"),
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(team):
    mask = df["team_name"] == team
    fig = px.bar(df[mask], x="common_name", y=["draws", "losses", "wins"], barmode="group",
                labels={
                    "common_name": "Team",
                    "variable": "Results"
                })
    
    return fig