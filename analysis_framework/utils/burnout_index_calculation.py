import os
import pandas as pd
from analysis_framework import PIPELINE_PATH


class Burnout:

    def __init__(self):
        pass

    @classmethod
    def percent_calculation(self):
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


if __name__ == "__main__":
    obj = Burnout()
    out = obj.percent_calculation()
