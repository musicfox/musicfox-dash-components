import musicfox_dash_components as mdc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
#app.css.config.serve_locally = True
app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    }
)
steps = [
    dict(element='.hello', intro="Did you know that testing is important?",
        position="bottom",),
    dict(element='.world', intro="The software world is decent with this, fortunately."),
    dict(element=".right-tooltip", intro="If this worked, it's on the right.",
        position="right"),
    dict(element=".left-tooltip", intro="If this worked, it's on the left.",
        position="left"),
    dict(element=".bottom-tooltip", intro="If this worked, it's on the bottom.",
        position="bottom"),
    dict(element=".top-tooltip", intro="If this worked, it's on the top.",
        position="top"),
]
app.layout = html.Div(className='container my-auto', children=[

    mdc.Hello(
        id='input',
        label='my-label',
        steps=steps,
    ),
    html.H1("Introducing the musicfox.io Hello component."),
    html.H2("This is a test.", id='output', className='align-center hello text-secondary',),
    html.H6("And we're testing the introductory tooltip that will make up the functionality of the Hello component.",
        id="subheader",
        className="world",
    ),
    html.Div(className="row", 
        children=[
            html.P(children="Tooltip right", className="col right-tooltip"),
            html.P(children="Tooltip left", className="col left-tooltip"),
        ],
    ),
    html.Div(className="row",
        children=[
            html.Div(className="col", 
                children=[
                    html.Label("Tooltip bottom"),
                    html.Select(title="Tooltip bottom", className="text-warning bottom-tooltip"),
                    html.P("Tooltip top", className="text-success top-tooltip"),
                ]
            ),
        ],
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
