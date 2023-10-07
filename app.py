import pickle
import numpy as np
import pandas as pd

from _train import train

from distutils.version import StrictVersion
from backlog_item import generate_backlog_item
from dash import Dash, html, dcc, callback, Output, Input

app = Dash(__name__)

# LOCAL: Testing
df = pd.read_csv("./tmp_data/app_store_model_inputs.csv")

retrain = False
if retrain:
    train(df["review"])

with open("tmp_data/topic_model.pkl", "rb") as f_in:
    topic_model = pickle.load(f_in)

testing_backlog_items = ["test 1", "test 2"]




# App
app.layout = html.Div([
    html.P("Backlog Items"),
    html.Div([generate_backlog_item(item) for item in testing_backlog_items]),
])

if __name__ == '__main__':
    app.run(debug=True)