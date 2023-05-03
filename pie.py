# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# declaring exploding pie
explode = [0,  0, 0]
# declaring exploding pie
data = [9, 5, 4]

keys = ['IaC non-experts', 'IaC experts', 'Use Case Owners']

plt.rcParams['font.size'] = 16.0

# define Seaborn color palette to use
palette_color = sns.color_palette('pastel')

pie, ax = plt.subplots(figsize=[15,10])

plt.pie(x=data, autopct="%.1f%%", explode=[0.01]*3, labels=keys, pctdistance=0.3, colors=palette_color)
plt.title("Iteration A", fontsize=18);
pie.savefig("ParticipantsPieA.png",  dpi=600)

data2 = [3, 7, 4]

pie2, ax = plt.subplots(figsize=[15,10])

plt.pie(x=data2, autopct="%.1f%%", explode=[0.01]*3, labels=keys, pctdistance=0.3, colors=palette_color)
plt.title("Iteration B", fontsize=18);
pie2.savefig("ParticipantsPieB.png",  dpi=600)

