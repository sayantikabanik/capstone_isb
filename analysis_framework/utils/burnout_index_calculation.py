import os
import pandas as pd
from analysis_framework import PIPELINE_PATH


class Burnout:

    def __init__(self):
        pass

    @classmethod
    def percent_calculation(cls):
        file_name = "cluster_output.csv"
        output_file_path = PIPELINE_PATH.joinpath(file_name)
        if os.path.exists(output_file_path):
            print("file found")
            cluster_data = pd.read_csv(output_file_path)
            cluster_percent = cluster_data.groupby('cluster').count()[['exhaustion']]
            cluster_percent['percent'] = (cluster_percent['exhaustion'] /
                                          cluster_percent['exhaustion'].sum()) * 100
            return cluster_percent
        else:
            print("Cluster data out generated, please run the pipeline")

    @classmethod
    def combine_scores(cls):
        output = cls.percent_calculation()
        medium_amber = output.iloc[[0, 1, 4]].percent.sum()
        not_burned_out_green = output.iloc[[2]].percent.sum()
        burned_out_red = output.iloc[[3]].percent.sum()
        return medium_amber, not_burned_out_green, burned_out_red
