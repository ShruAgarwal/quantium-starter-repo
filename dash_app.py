from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# initialize dash
app = Dash(__name__)

# read the data
df = pd.read_csv('Final_sales_output.csv')


# create the visualization
fig = px.line(df, x="date", y="Sales", title="Pink Morsel Sales")

# define the app layout
app.layout = html.Div(children=[
    html.H1(children='Pink morsels Visualizer'),

    html.Div(children='''
        Answers: Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    '''),

    dcc.Graph(
        id='visualization',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)