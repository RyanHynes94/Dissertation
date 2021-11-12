import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px

from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('MessivsRonaldo', external_stylesheets=external_stylesheets)   # replaces dash.Dash

# load data 

df = pd.read_csv('cristiano_vs_messi 2.csv')  #load data
df2 = pd.read_excel('MessiRonaldo.xlsx')

df = df.sort_values('type', ascending=True) # sort datasets
df2 = df2.sort_values('Season', ascending=True)

#drop null values

df.drop(df.index[df['type'] == 'Chest'], inplace=True)
df.drop(df.index[df['type'] == 'Counter attack goal'], inplace=True)
df.drop(df.index[df['type'] == 'Deflected shot on goal'], inplace=True)
df.drop(df.index[df['type'] == 'Penalty rebound'], inplace=True)
df.drop(df.index[df['type'] == 'Solo run'], inplace=True)


# figure 1
figure = px.histogram(df, title='types of goals scored', x='type', color='player', barmode='group',
                      labels={
                          "type": "Type of Goal"
                          
})

figure.update_layout(
    yaxis_title="Goals",
    font=dict(
        family="helvetica",
        size=18
    ))

figure.add_layout_image(
    dict(
        source="https://en.wikipedia.org/wiki/Cristiano_Ronaldo#/media/File:Cristiano_Ronaldo_2018.jpg",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

figure = dcc.Graph(id='graph1', figure=figure)

#figure 2
fig2 = px.line(df2, title='Champions League goals', y='CL_Goals', x='Season', color='Player', markers=True,
              labels={
                  "CL_Goals": "Champions League goals",
              })
fig2.update_xaxes(type='category')

fig2 = dcc.Graph(id='graph2', figure=fig2)

header = html.H2(children='Messi vs Ronaldo - A visual comparison of key statistics')
intro = html.H5(children='Few arguments in football are as contentious as the classic Messi or Ronaldo debate. The numbers for both are staggering but can we through visualisation shine a light on the key differences between these two titans of the beautiful game?')

layout = html.Div(children=[header, intro, figure, fig2], style={"font-family": "helvetica"})

app.layout = layout




