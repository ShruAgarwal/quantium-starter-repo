from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# initialize dash
app = Dash(__name__)

colors = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#581845"
    # 'background': '#111111',
    # 'text': '#7FDBFF'
}

# read the data
df = pd.read_csv('Final_sales_output.csv')

# create the visualization
def generate_fig(chart_data):
    line_chart = px.line(chart_data, x="date", y="Sales", color="region", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=colors['secondary'],
        paper_bgcolor=colors['primary'],
        font_color=colors['font']
    )
    return line_chart

visualization = dcc.Graph(
    id="visualization",
    figure=generate_fig(df)
)

# region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)

# define the region picker callback
@app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)

def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]

    # generate a new line chart with the filtered data
    figure = generate_fig(trimmed_data)
    return figure



# define the app layout
app.layout = html.Div(style={
        "textAlign": "center",
        "background-color": colors["primary"],
        "border-radius": "20px"
    },
    children=[
    html.H1(
        children='Pink morsels Visualizer',
        style={
            "background-color": colors["secondary"],
            "color": "#110366",
            "border-radius": "20px"
            # 'textAlign': 'center',
            # 'color': colors['text']
        }
    ),

    html.Div(children='Did the sales gone higher before or after the Pink Morsel price increase on the 15 Jan 2021?', 
     style={
         'textAlign': 'center',
         'color': colors['font']
     }
    ),
    visualization,

    html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%",
        'color': colors['font']
    })
])


if __name__ == '__main__':
    app.run_server(debug=True)
