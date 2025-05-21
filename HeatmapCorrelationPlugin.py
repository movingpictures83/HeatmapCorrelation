
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

class HeatmapCorrelationPlugin:
    def input(self, infile):
        corr_file = infile
        self.corr_df = pd.read_csv(corr_file)

    def run(self):
        self.corr_df_reshaped = self.corr_df.pivot(index="from", columns="to", values="spearman")
        self.corr_df_reshaped = self.corr_df_reshaped.fillna(0)

    def output(self, outfile):
        sns.clustermap(self.corr_df_reshaped, annot=True, cmap='coolwarm', center=0,figsize=(25,15))
        self.corr_df_reshaped.to_csv(outfile+".csv")
        plt.savefig(outfile)

# # Get skeleton of the
# corr_dict = {"from":[]}
#
#
#
# with open(corr_file, 'r') as f:
#     f.readline()
#     for line in f.readlines():
#         row = line.split(",")
#         from_name = row[0]
#         to_name = row[1]
#         corr = row[4]
#         corr_dict["from"].append(from_name)
#         if to_name not in corr_dict.keys():
#             corr_dict[to_name] = []
