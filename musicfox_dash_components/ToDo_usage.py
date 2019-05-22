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

app.layout = html.Div(className='container-fluid bg-light my-auto', children=[
    mdc.ToDo(
        id='demo',
        title="Business Planning",
        subtitle="Michael Porter's Five Forces Framework",
        todos=[
            {
                'Competitive rivalry':[
                    'sustainable innovative advantage',
                    'online vs offline competition',
                    'advertising cost',
                    'industry concentration ratio of firms',
                ],
            },
            {
                'Supplier bargaining power':[
                    'presence of substitute inputs',
                    'degree of differentiation amongst inputs',
                    'strength of employee solidarity @ suppliers',
                    {
                        'supply-chain competitive landscape': [
                            "is there an ability of the supplier(s) to vertically integrate and cut out the buyer?",
                        ],
                    },
                    'supplier switching costs',
                ],
            },
            {
                'Customer bargaining power':[
                    'buyer concentration to firm concentration ratio',
                    'distribution channel dependence',
                    {
                        'bargaining leverage':[
                            'high fixed costs -> IMPORTANT',
                            'low fixed costs -> NOT IMPORTANT',
                        ]
                    },
                    'buyer price sensitivity',
                    'availability of substitute products',
                    'buyer information availability',
                ],
            },            
            {
                'Threat of substitutes':[
                    'buyer propensity to substitute',
                    'relative price performance of substitute',
                    "buyers' switching costs",
                    "perceived level of product differentiation",
                    "number of substitute products available in the market",
                    "ease of subsitution",
                ],
            },            
            {
                'Threat of new entrants':[
                    {'barriers to entry': ['patents', 'rights'],},
                    'government policies', 
                    'capital requirements',
                    'industry, product, and unique cost structures',
                    'customer loyalty',
                    'product differentiation',
                    'network effect',
                    'industry profitability',
                ],
            },
        ],
    ),
    html.Div(className="jumbotron bglight",
        children=[
            html.H1("Introducing the musicfox.io ToDo component for Dash.",
                className="display-4 hello"
            ),
            html.P("This is a test.",
                id='output',
                className='lead world text-secondary',
            ),
            html.P("And we're testing the main parts that make up the ToDo component.",
                id="subheader",
                className="text-left",
            ),

        ],
    ),
    #html.Div(className="row", 
    #    children=[
    #        html.P(children="Tooltip right", className="col text-center mx-4 right-tooltip"),
    #        html.P(children="Tooltip left", className="col text-center mx-4 left-tooltip"),
    #    ],
    #),
    #html.Hr(className="my-4"),
    #html.Div(className="row",
    #    children=[
    #        html.Div(className="col text-center", 
    #            children=html.A("Tooltip Bottom",
    #                className="btn btn-secondary bottom-tooltip",
    #                href='https://github.com/thinkjrs/musicfox-dash-components', 
    #                role='button',
    #                id='bottom-button',
    #            ),
    #        ),
    #        html.Div(className="col text-center", 
    #            children=html.P("Tooltip top",
    #                    className="btn btn-secondary top-tooltip"
    #            ),
    #        ),
    #    ],
    #),
])

if __name__ == '__main__':
    app.run_server(debug=True)
