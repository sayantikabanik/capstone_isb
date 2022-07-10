import intake
import pandas as pd

from dagster import get_dagster_logger, job, op, Output, graph
from analysis_framework import DATA_CATALOG_PATH
from factor_analyzer import FactorAnalyzer

from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans


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
def index_reset(df):
    # important step: for factor analysis to have a similar sl no of the data
    df_reset = df.reset_index(drop=True)
    return df_reset


@op
def factor_analysis(df_subset_fa) -> Output:
    fa = FactorAnalyzer(n_factors=2, rotation='varimax')
    fa.fit(df_subset_fa)
    df_factor_scores = pd.DataFrame(fa.transform(df_subset_fa))
    df_subset_fa[['factor1', 'factor2']] = df_factor_scores
    fa_data = df_subset_fa
    print(fa_data)
    return fa_data


@op
def write_csv(df_result):
    df_result.to_csv('cluster_output.csv')
    return 0


@op
def intermediate_clustering_step(df_result):
    factor_df = df_result[['factor1', 'factor2']]
    return factor_df


@op
def scaling_data(factor_df):
    data_scaled = normalize(factor_df)
    data_scaled = pd.DataFrame(data_scaled, columns=factor_df.columns)
    return data_scaled


@op
def clustering_processed_factor_data(scaled_df, df_result):
    kmeans = KMeans(init="k-means++", n_clusters=5, n_init=10,   max_iter=300,random_state=42)
    kmeans.fit(scaled_df)
    kmeans.inertia_
    kmeans.cluster_centers_
    df_cluster = df_result
    df_cluster['cluster'] = kmeans.labels_
    return df_cluster


@op
def cluster_operations(cluster_df):
    return cluster_df.groupby('cluster').mean()


@job
def compute():
    df_raw = read_raw_data()
    df_subset = subset_data(df_raw)
    df_fa = index_reset(df_subset)
    df_result = factor_analysis(df_fa)
    factor_df = intermediate_clustering_step(df_result)
    scaled_df = scaling_data(factor_df)
    cluster_df = clustering_processed_factor_data(scaled_df, df_result)
    cluster_operation_df = cluster_operations(cluster_df)
    write_csv(cluster_df)


if __name__ == "__main__":
    result = compute.execute_in_process()
