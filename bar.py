import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv("./Development_Modification.CSV")
ax = df.plot.bar(x='Activity', color=['#336699', '#bfcfff'])
ax.set_ylabel('Minutes', fontsize=16)

activities = ['Development', 'Modification']
ax.set_xticklabels(activities, rotation=0, fontsize=14)
plt.tight_layout()
plt.xlabel('Activity', fontsize=16);
plt.savefig("timeExpertsIt1.png")