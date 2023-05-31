from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd



app = Dash(__name__)
server=app.server

app.layout = html.Div([
    html.H1(children='Hola mundo', style={'textAlign':'center'}),
    html.P("Esta es la aplicacion para la PEC3")

])


if __name__ == '__main__':
    app.run_server(debug=True)