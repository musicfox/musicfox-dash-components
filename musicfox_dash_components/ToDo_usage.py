import musicfox_dash_components as mdc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
#app.css.config.serve_locally = True
app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css"
    }
)

app.layout = html.Div(className='container-fluid bg-light my-auto', children=[
    #mdc.ToDo(
    #    id='demo',
    #    title="Business Planning",
    #    subtitle="Michael Porter's Five Forces Framework",
    #    todos=[
    #        {
    #            'Competitive rivalry':[
    #                'sustainable innovative advantage',
    #                'online vs offline competition',
    #                'advertising cost',
    #                'industry concentration ratio of firms',
    #            ],
    #        },
    #        {
    #            'Supplier bargaining power':[
    #                'presence of substitute inputs',
    #                'degree of differentiation amongst inputs',
    #                'strength of employee solidarity @ suppliers',
    #                {
    #                    'supply-chain competitive landscape': [
    #                        "is there an ability of the supplier(s) to vertically integrate and cut out the buyer?",
    #                    ],
    #                },
    #                'supplier switching costs',
    #            ],
    #        },
    #        {
    #            'Customer bargaining power':[
    #                'buyer concentration to firm concentration ratio',
    #                'distribution channel dependence',
    #                {
    #                    'bargaining leverage':[
    #                        'high fixed costs -> IMPORTANT',
    #                        'low fixed costs -> NOT IMPORTANT',
    #                    ]
    #                },
    #                'buyer price sensitivity',
    #                'availability of substitute products',
    #                'buyer information availability',
    #            ],
    #        },            
    #        {
    #            'Threat of substitutes':[
    #                'buyer propensity to substitute',
    #                'relative price performance of substitute',
    #                "buyers' switching costs",
    #                "perceived level of product differentiation",
    #                "number of substitute products available in the market",
    #                "ease of subsitution",
    #            ],
    #        },            
    #        {
    #            'Threat of new entrants':[
    #                {'barriers to entry': ['patents', 'rights'],},
    #                'government policies', 
    #                'capital requirements',
    #                'industry, product, and unique cost structures',
    #                'customer loyalty',
    #                'product differentiation',
    #                'network effect',
    #                'industry profitability',
    #            ],
    #        },
    #    ],
    #),
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
    html.Div(className="row", 
        children=[
            html.Div(className='col',
                children=mdc.ToDo(
                    id='demo-1',
                    todos=['Testing 1', 'Testing 2','Testing 3'],
                    title="Making a list and testing it. *Thrice*.",
                    subtitle="Are we going to find out if we're **naughty** or **nice**?",
                ),
            ),
            html.Div(className='col', 
                children=mdc.ToDo(
                    id='demo-2',
                    todos=['Testing 1', '~~Testing 2~~','[Testing 3](https://musicfox.io)'],
                    title="Making a **second** list and testing it. *Thrice*.",
                    subtitle="Are we going to find out if we're **naughty** or **nice**?",
                ),
            )
        ],
        style = dict(margin='auto'),
    ),
    html.Div(className="row",
        children=html.Div(className='col',
            children=mdc.ToDo(
                id='demo-3',
                todos=[
                    '''*Unit* Tests:  \n    ```python -m pytest --verbose```  ''', 
                    '''*Integration* Tests:  \n    **[Gitlab CI](https://docs.gitlab.com/ee/ci/quick_start/)**''',
                    '''*Acceptance* Tests:  \n> Yo, buddy, how about we sit down and write down *exactly* what we need here?  '''],
                header="High-quality software development strategies.",
                title="Types of tests",
                subtitle="End beneficiaries include business, development, and open-source communities",
                footer='>> *It is not enough for code to work.* - Robert C. Martin',
            )
        ),
        style=dict(margin='auto', marginTop='1.25rem'),
    ),
])

if __name__ == '__main__':
    app.run_server(debug=False)
