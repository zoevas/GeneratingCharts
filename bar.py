import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv("./Development_Modification.CSV")
ax = df.plot.bar(x='activity', color=['#6495ED', '#B6D0E2'])
ax.set_ylabel('Minutes')

activities = ['Development', 'Modification']
ax.set_xticklabels(activities, rotation=15)
plt.tight_layout()

plt.savefig("timeExpertsIt1.png")