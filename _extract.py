import yaml
import json
import argparse
import pandas as pd
from datetime import datetime
from app_store_scraper import AppStore

def load_config_yaml(path_to_yaml):
    with open(path_to_yaml,'r') as config_in:
        yaml_contents = yaml.load(config_in, Loader=yaml.SafeLoader)

    return yaml_contents

def _serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def extract(country, app_name, app_id, num_reviews, output_file):
    met_us_app = AppStore(country=country, app_name=app_name, app_id=app_id)
    met_us_app.review(how_many=num_reviews)
    with open(output_file, 'w') as out_file:
        json.dump(met_us_app.reviews, out_file, default=_serialize_datetime)

def transform(input_path, output_file):
    df_raw = pd.read_json(input_path)
    drop_columns = ["isEdited", "userName", "title"]
    df_raw.drop(columns=drop_columns, inplace=True)
    df_raw.to_csv(output_file, index=False)

def main(params):
    # Hard Coded Parameters for the process
    extract_path = "./tmp_data/app_store_scrape.json"
    transform_data_path = "./tmp_data/app_store_model_inputs.csv"
    country_of_scrape = "us"
    num_reviews = 100

    # Configuration Parameters
    config_contents = load_config_yaml(params.config_path)
    app_store_id = config_contents["data-scrape"]["app_store_id"]
    app_store_name = config_contents["data-scrape"]["app_store_app_name"]
    num_reviews_to_scrape = config_contents["data-scrape"]["num_reviews"]

    # Extract-Transform
    extract(
        country=country_of_scrape, 
        app_name=app_store_name, 
        app_id=app_store_id, 
        num_reviews=num_reviews_to_scrape, 
        output_file=extract_path
        )

    transform(
        input_path=extract_path, 
        output_file=transform_data_path
        )

if __name__ == '__main__':
    default_config_path = "./config.yaml"

    parser = argparse.ArgumentParser(description="Update data extraction for app of choice")
    parser.add_argument(
        '--config_path', 
        default=default_config_path, 
        required=False, 
        help='Path to configuration file'
    )

    params = parser.parse_args()
    main(params)