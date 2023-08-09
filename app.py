import numpy as np
import pandas as pd

from distutils.version import StrictVersion
from backlog_item import generate_backlog_item
from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

# LOCAL: Testing
df = pd.read_csv("./tmp_data/app_store_model_inputs.csv")
import random
random_values_list = ["Bad", "Good", "Neutral", "Horrible", "Great"]
def random_value(row):
    return random.choice(random_values_list)
df['fb'] = df.apply(random_value, axis=1)

testing_backlog_items = df.fb.unique()
##

app.layout = html.Div([
    html.P("Backlog Items"),
    html.Div([generate_backlog_item(item) for item in testing_backlog_items])
])

if __name__ == '__main__':
    app.run(debug=True)