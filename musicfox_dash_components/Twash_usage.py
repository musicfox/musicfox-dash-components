import musicfox_dash_components as mdc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc


app = dash.Dash(__name__)
app.css.config.serve_locally = False
app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css"
    }
)
app.layout = html.Div(
    className='container fluid bg-light',
    children=[
        html.Div(className="jumbotron bglight",
            children=[
                html.H1("Introducing Twash, a Twitter Profile embedded Timeline for Dash by musicfox.io.",
                    className="display-4 hello"
                ),
                html.P("This is a test.",
                    id='output',
                    className='lead world text-secondary',
                ),
                html.P("And we're testing the main parts that make up the Twash component.",
                    id="subheader",
                    className="text-left",
                ),

            ],
        ),
        html.Div(className='row', children=[
            html.Div(className='col', children=[
                dcc.Markdown([
                    '###### Basic use: Twitter timeline',

                ],), 
                mdc.Twash(
                    id='input1',
                    handle='ArianaGrande',
                    height=400,
                    width=400,
                ),
            ],),
            html.Div(className='col', children=[
                dcc.Markdown([
                    '###### Adjust width and center',
                    '  ',
                    'Make it *skinny* with the `width` property.  ',
                    "*Center* with the container's `text-align` style properties.  ",
                ]),
                    
                mdc.Twash(
                    id='input2',
                    handle='ArianaGrande',
                    height=700,
                    width=180,
                ),
                ],style={'text-align':'center'}),            
            html.Div(className='col', children=[
                dcc.Markdown([
                    '###### Extend to the end of the page and change the theme.',
                    '  ',
                    'The profile defaults to the full-page height  ', 
                    'The default theme is `light` but `dark` is available  ',
                ]),
                mdc.Twash(
                    id='input3',
                    handle='ArianaGrande',
                    width=400,
                    theme='dark',
                ),
            ],),            
        ],),
    ],
)


if __name__ == '__main__':
    app.run_server(debug=False)
