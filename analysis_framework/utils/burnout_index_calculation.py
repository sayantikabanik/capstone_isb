import os
import pandas as pd
from analysis_framework import PIPELINE_PATH


class Burnout:

    def __init__(self, loc, comp, cluster):
        self.loc = loc
        self.comp = comp
        self.cluster = cluster

    def percent_calculation(self):
        file_name = "cluster_output.csv"
        output_file_path = PIPELINE_PATH.joinpath(file_name)
        if os.path.exists(output_file_path):
            print("file found")
            cluster_data = pd.read_csv(output_file_path)
            if(self.comp and self.loc is not None) and self.cluster > -1:
                print("*"*10, self.comp, self.loc, self.cluster)
                filtered_event_data = cluster_data.loc[(cluster_data["company"] == str(self.comp)) &
                                                       (cluster_data["location"] == str(self.loc)) &
                                                       (cluster_data["cluster"] == int(self.cluster))]
            elif (self.comp and self.loc is not None) and self.cluster == -1:
                print("*"*10, self.comp, self.loc, self.cluster)
                filtered_event_data = cluster_data.loc[(cluster_data["company"] == str(self.comp)) &
                                                       (cluster_data["location"] == str(self.loc))]
            else:
                print("exception occured")
            cluster_percent = filtered_event_data.groupby('cluster').count()[['exhaustion']]
            cluster_percent['percent'] = (cluster_percent['exhaustion'] /
                                          cluster_percent['exhaustion'].sum()) * 100
            print(cluster_percent)
            return cluster_percent
        else:
            print("Clustering data not found, please run the pipeline first")

    def combine_scores(self):
        output = self.percent_calculation()
        medium_amber = output.loc[(output.index == 0) |
                                  (output.index == 1) |
                                  (output.index == 4)].percent.sum()
        print(medium_amber)
        not_burned_out_green = output.loc[(output.index == 2)].percent.sum()
        burned_out_red = output.loc[(output.index == 3)].percent.sum()
        return medium_amber, not_burned_out_green, burned_out_red

    def filtered_data(self):
        file_name = "cluster_output.csv"
        output_file_path = PIPELINE_PATH.joinpath(file_name)
        if os.path.exists(output_file_path):
            print("file found")
            cluster_data = pd.read_csv(output_file_path)
            if (self.comp and self.loc is not None) and self.cluster > -1:
                print("*" * 10, self.comp, self.loc, self.cluster)
                filtered_event_data = cluster_data.loc[(cluster_data["company"] == str(self.comp)) &
                                                       (cluster_data["location"] == str(self.loc)) &
                                                       (cluster_data["cluster"] == int(self.cluster))]
            elif (self.comp and self.loc is not None) and self.cluster == -1:
                print("*" * 10, self.comp, self.loc, self.cluster)
                filtered_event_data = cluster_data.loc[(cluster_data["company"] == str(self.comp)) &
                                                       (cluster_data["location"] == str(self.loc))]
            else:
                print("exception occured")
        return filtered_event_data

