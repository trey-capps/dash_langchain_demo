from dash import html

def generate_backlog_item(item):
    html.Div(
        [
            html.Div(item, style={'flex': 1}),
            html.Div([html.Button("Yes", id=f"yes_{item}"),
                      html.Button("No", id=f"no_{item}")
                      ],
                     style={'display': 'flex', 'justify-content': 'center'})
        ],
        style={'display': 'flex', 'align-items': 'center', 'border': '1px solid black', 'margin': '5px', 'padding': '5px'}
    )