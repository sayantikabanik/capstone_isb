import intake
from dagster import asset
from analysis_framework import DATA_CATALOG_PATH
from dagster import materialize


@asset
def read_raw_data():
    catalog_path = DATA_CATALOG_PATH.joinpath("catalog.yml")
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.review_dataset.read()
    print(df_raw.head())
    return df_raw


#TODO: Add pre-processing and text score logic
@asset
def process_raw_data(read_raw_data):
    return 0


if __name__ == "__main__":
    materialize([read_raw_data, process_raw_data])
