import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Set the desired width in pixels
width_in_pixels = 1000

# Calculate the required figure width in inches based on the DPI
dpi = width_in_pixels / 10  # Assuming 10 inches in width
fig_width = width_in_pixels / dpi

#way 1 # gridspec https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html










fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0.425, wspace=0.125)
axes = gs.subplots(sharex=True)
#way 2
# Create a single figure with two subplots sharing the same y-axis
#fig, axes = plt.subplots(2, 3, figsize=(fig_width, 4), dpi=dpi, sharey=True)  # Adjust the height as needed

df_perf = pd.read_csv('csv/Potential_adoption_it2.CSV', index_col=False)

sns.boxplot(y=df_perf["Potential Adoption"], x=df_perf["Editor"], width=0.3, ax=axes[0, 0])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=0, ha="center")
axes[0, 0].set_aspect(0.8)
axes[0, 0].set_ylabel('Potential adoption')  # Add this line to set the y-axis label
axes[0, 0].set(xlabel=None)



df_perf = pd.read_csv('csv/UseInCompanyIT2.CSV', index_col=False)

sns.boxplot(y=df_perf["Use in Company"], x=df_perf["Editor"], width=0.3, ax=axes[0, 1])
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=0, ha="center")
axes[0, 1].set_aspect(0.8)
axes[0, 1].set_ylabel('Use in Company')  # Add this line to set the y-axis label
axes[0, 1].set(xlabel=None)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_it2.CSV', index_col=False)

sns.boxplot(y=df_perf["Easiness"], x=df_perf["Editor"], width=0.3, ax=axes[1, 0])
axes[1, 0].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=0, ha="center")
axes[1, 0].set_aspect(0.8)
axes[1, 0].set_ylabel('Easiness')  # Add this line to set the y-axis label
axes[1, 0].set(xlabel=None)



df_perf = pd.read_csv('csv/Recommendation_it2.CSV', index_col=False)
sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Editor"], width=0.3, ax=axes[1, 1])
axes[1, 1].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=0, ha="center")
axes[1, 1].set_aspect(0.8)
axes[1, 1].set_ylabel('Recommendation')  # Add this line to set the y-axis label
axes[1, 1].set(xlabel=None)

# Adjust layout for better spacing
#fig.tight_layout()
#fig.subplots_adjust(wspace=0.125)  # Adjust the value for your desired spacing

# Save the figure
plt.savefig("pngboxplots_subplots/M37_Intention_of_use.png", dpi=dpi)


# Show the plot (if needed)
plt.show()

fig = plt.figure()
df_perf = pd.read_csv('csv/Recommending.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Users"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
fig = sns_plot.get_figure()
sns_plot.set(xlabel=None)
fig.savefig("pngboxplots_subplots/recommendation.png", dpi=600)

plt.show()
