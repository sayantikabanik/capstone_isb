import intake
import pandas as pd
import numpy as np
from dagster import get_dagster_logger, job, op, Output, graph, Out
from analysis_framework import DATA_CATALOG_PATH, PIPELINE_PATH
from analysis_framework.utils.extract_location import extract_location
from analysis_framework.utils.map_maj_location import map_maj_location
from factor_analyzer import FactorAnalyzer

from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans

catalog_path = DATA_CATALOG_PATH.joinpath("catalog.yml")


@op
def read_raw_data():
    catalog = intake.open_catalog(catalog_path)
    df_raw = catalog.review_dataset.read()
    return df_raw

@op
def read_loc_mapping():
    catalog = intake.open_catalog(catalog_path)
    df_loc = catalog.location_mapping.read()
    return df_loc

@op
def subset_data(df_raw):
    df_subset = df_raw[['skillDevelopment', 'salaryBenefits',
                        'workLifeBalance', 'workSatisfaction',
                        'jobSecurity', 'careerGrowth', 'companyCulture']]
    df_subset = df_subset.dropna()
    return df_subset

@op
def subset_data_dim(df_raw):
    df_subset_dim = df_raw[['reviewText', 'location', 'cons',
                            'pros', 'jobFunction', 'company']]
    return df_subset_dim


@op
def maj_loc_list(df_loc):
    major_locations=df_loc[df_loc['Type']=='Major']['Mapped Value'].to_list()
    return major_locations

@op
def maj_loc_harmonize(df_loc):
    # #Harmonizing Locations
    location_mapping=df_loc.set_index('Original Value')['Mapped Value'].to_dict()
    return location_mapping

@op
def clean_location(df_subset_dim,major_locations,location_mapping,location_col='location',jobFunc_col='jobFunction'):
    '''Takes a data-frame, location and Job Function column,
	- extracts Location from Job Function,
	- Renames ambiguous major cities
	- Buckets 10% other cities to Others'''
    #Extracting Expirience and Location from jobFunction column
    df_subset_dim['extract_location']=df_subset_dim[jobFunc_col].apply(lambda x:extract_location(x))
    #Imputing Blanks in Location column with data extracted from jobFunction, if available
    df_subset_dim['cleaned_location']=np.where(df_subset_dim[location_col].isna(),df_subset_dim['extract_location'],df_subset_dim[location_col])
    #Imputing unknown locations with Not Specified
    df_subset_dim['cleaned_location']=df_subset_dim['cleaned_location'].fillna('Not Specified')
    #Extracting location city from location columns
    df_subset_dim['cleaned_location']=df_subset_dim['cleaned_location'].apply(lambda x:map_maj_location(major_locations,str(x)))
    df_subset_dim['cleaned_location']=df_subset_dim['cleaned_location'].map(location_mapping)
    #major_locations=df_loc[df_loc['Type']=='Major']['Mapped Value'].to_list()
    major_locations.append('Not Specified')
    df_subset_dim['cleaned_location']=np.where(df_subset_dim['cleaned_location'].isin(major_locations),df_subset_dim['cleaned_location'],'Others')
    df_subset_dim=df_subset_dim.drop(columns=location_col)
    df_subset_dim=df_subset_dim.rename(columns={'cleaned_location':'location'})
    return df_subset_dim
@op
def index_reset(df):
    # important step: for factor analysis to have a similar sl no of the data
    df_reset = df.reset_index(drop=False)
    return df_reset


@op
def factor_analysis(df_subset_fa) -> Output:
    fa = FactorAnalyzer(n_factors=3, rotation='oblimin')
    fa.fit(df_subset_fa)
    df_factor_scores = pd.DataFrame(fa.transform(df_subset_fa))
    df_subset_fa[['exhaustion', 'Depersonalization',
                  'PersonalAccomplishment']] = df_factor_scores
    fa_data = df_subset_fa
    return fa_data


@op
def write_cluster_output(df_result):
    file_name = "cluster_output.csv"
    output_file_path = PIPELINE_PATH.joinpath(file_name)
    df_result.to_csv(output_file_path)
    return 0
    
@op
def intermediate_clustering_step(df_result):
    factor_df = df_result[['exhaustion', 'Depersonalization', 'PersonalAccomplishment']]
    return factor_df


@op
def scaling_data(factor_df):
    data_scaled = normalize(factor_df)
    data_scaled = pd.DataFrame(data_scaled, columns=factor_df.columns)
    return data_scaled


@op
def clustering_processed_factor_data(scaled_df, df_result):
    kmeans = KMeans(init="k-means++", n_clusters=5, n_init=10, max_iter=300, random_state=42)
    kmeans.fit(scaled_df)
    kmeans.inertia_
    kmeans.cluster_centers_
    df_cluster = df_result
    df_cluster['cluster'] = kmeans.labels_
    return df_cluster


@op
def cluster_operations(cluster_df):
    return cluster_df.groupby('cluster').mean()


@op
def combine_fact_dim(cluster_df,df_subset_dim):
    combined_df=cluster_df.merge(df_subset_dim, on='index', how='left')
    return combined_df


@job
def compute():
    df_raw = read_raw_data()
    df_loc = read_loc_mapping()
    df_subset = subset_data(df_raw)
    df_fa = index_reset(df_subset)
    df_subset_dim=subset_data_dim(df_raw)
    major_locations=maj_loc_list(df_loc)
    location_mapping=maj_loc_harmonize(df_loc)
    df_subset_dim=clean_location(df_subset_dim,major_locations,location_mapping)
    df_subset_dim=index_reset(df_subset_dim)
    df_result = factor_analysis(df_fa)
    factor_df = intermediate_clustering_step(df_result)
    scaled_df = scaling_data(factor_df)
    cluster_df = clustering_processed_factor_data(scaled_df, df_result)
    cluster_operation_df = cluster_operations(cluster_df)
    combined_df=combine_fact_dim(cluster_df, df_subset_dim)
    write_cluster_output(combined_df)


if __name__ == "__main__":
    result = compute.execute_in_process()
