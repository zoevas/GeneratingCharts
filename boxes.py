# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fields = ['Editor', 'Perceived Usefulness']
df_perf = pd.read_csv('perceived_usefulness_it1_nonexperts.CSV', index_col=False)
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["xtick.labelsize"] = 7
sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"] )
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=40, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("test.png", dpi=600)
