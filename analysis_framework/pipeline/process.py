import intake
import pandas as pd

from dagster import get_dagster_logger, job, op
from analysis_framework import DATA_CATALOG_PATH
from factor_analyzer import FactorAnalyzer

logger = get_dagster_logger()


@op
def read_raw_data():
    catalog_path = DATA_CATALOG_PATH.joinpath("catalog.yml")
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.review_dataset.read()
    print(df_raw.head())
    return df_raw


@op
def subset_data(read_raw_data):
    df_subset = read_raw_data[['skillDevelopment', 'salaryBenefits',
               'workLifeBalance', 'workSatisfaction',
               'jobSecurity', 'careerGrowth', 'companyCulture']]

    df_subset = df_subset.dropna()
    df_reset = df_subset.reset_index(drop=True)
    logger.info("data shape",df_reset.shape)
    return df_reset


@op
def factor_analysis(df_reset):
    fa = FactorAnalyzer(n_factors=2, rotation='varimax')
    fa.fit(df_reset)
    df_factor_scores = pd.DataFrame(fa.transform(df_reset))
    df_reset[['factor1', 'factor2']] = df_factor_scores
    fa_data = df_reset
    logger.info("Data for factor analysis computation", fa_data.head())
    return 0

@job
def compute():
    df_raw = read_raw_data()
    df_subset = subset_data(df_raw)
    df_result = factor_analysis(df_subset)
    # factor_df = df_result[['factor1', 'factor2']]
    print(df_result.head())
    logger.info("Factor compute results", df_result)
    # logger.info("Min and max for factors computed", factor_df.min(), factor_df.max())
    #

# @asset
# def cluster_analysis():
#     factor_analysis(df_reset)
