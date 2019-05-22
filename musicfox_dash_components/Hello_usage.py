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
    dict(element='.hello', intro="Did you know that testing resultant outcomes is important?",
        position="bottom",),
    dict(element='.world', intro="The software world is decent with this, fortunately."),
    dict(element='#subheader', intro="But because the growth of things using software is growing faster than those who write software can manage, our world remains perilous.",
        position="bottom-right"),
    dict(element=".right-tooltip", intro="If this worked, it's on the right.",
        position="right"),
    dict(element=".left-tooltip", intro="If this worked, it's on the left.",
        position="left"),
    dict(element="#bottom-button", intro="If this worked, it's on the bottom.",
        position="bottom"),
    dict(element=".top-tooltip", intro="If this worked, it's on the top.",
        position="top"),
]
app.layout = html.Div(className='container-fluid bg-light my-auto', children=[

    mdc.Hello(
        id='input',
        steps=steps,
    ),
    html.Div(className="jumbotron bglight",
        children=[
            html.H1("Introducing the musicfox.io Hello component for Dash.",
                className="display-4 hello"
            ),
            html.P("This is a test.",
                id='output',
                className='lead world text-secondary',
            ),
            html.P("And we're testing the introductory tooltip that will make up the functionality of the Hello component.",
                id="subheader",
                className="text-left",
            ),

        ],
    ),
    html.Div(className="row", 
        children=[
            html.P(children="Tooltip right", className="col text-center mx-4 right-tooltip"),
            html.P(children="Tooltip left", className="col text-center mx-4 left-tooltip"),
        ],
    ),
    html.Hr(className="my-4"),
    html.Div(className="row",
        children=[
            html.Div(className="col text-center", 
                children=html.A("Tooltip Bottom",
                    className="btn btn-secondary bottom-tooltip",
                    href='https://github.com/thinkjrs/musicfox-dash-components', 
                    role='button',
                    id='bottom-button',
                ),
            ),
            html.Div(className="col text-center", 
                children=html.P("Tooltip top",
                        className="btn btn-secondary top-tooltip"
                ),
            ),
        ],
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
