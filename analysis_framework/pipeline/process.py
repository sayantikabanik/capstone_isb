import intake
import pandas as pd

from dagster import get_dagster_logger, job, op, Output, graph
from analysis_framework import DATA_CATALOG_PATH
from factor_analyzer import FactorAnalyzer

logger = get_dagster_logger()

#
# @op
# def index_reset(df):
#     df_reset = df.reset_index(drop=True)
#     return df_reset


@op
def read_raw_data():
    catalog_path = DATA_CATALOG_PATH.joinpath("catalog.yml")
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.review_dataset.read()
    return df_raw


@op
def subset_data(df_raw):
    df_subset = df_raw[['skillDevelopment', 'salaryBenefits',
                        'workLifeBalance', 'workSatisfaction',
                        'jobSecurity', 'careerGrowth', 'companyCulture']]
    df_subset = df_subset.dropna()
    return df_subset


@op
def factor_analysis(df_subset):
    df_reset = df_subset.reset_index(drop=True)
    fa = FactorAnalyzer(n_factors=2, rotation='varimax')
    fa.fit(df_reset)
    df_factor_scores = pd.DataFrame(fa.transform(df_reset))
    df_subset[['factor1', 'factor2']] = df_factor_scores
    fa_data = df_reset
    return fa_data


@job
def compute():
    df_raw = read_raw_data()
    df_subset = subset_data(df_raw)
    df_result = factor_analysis(df_subset)
    # factor_df = df_result[['factor1', 'factor2']]
    # logger.info("Factor compute results", factor_df.head())


if __name__ == "__main__":
    result = compute.execute_in_process()
