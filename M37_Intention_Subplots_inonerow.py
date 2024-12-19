import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the desired width in pixels
width_in_pixels = 1000
dpi = 100  # Setting DPI explicitly
fig_width = width_in_pixels / dpi
fig_height = 5  # Adjust height as needed for better visualization

# Create the figure and gridspec
fig = plt.figure(figsize=(fig_width, fig_height), dpi=dpi)
gs = fig.add_gridspec(1, 4, hspace=0.425, wspace=0.3)  # Adjusted wspace for more spacing
axes = gs.subplots(sharey=False)

# Titles for the plots
titles = [
    "Potential Adoption",
    "Use in Company",
    "Easiness in Becoming Skilled",
    "Recommendation"
]

# Boxplot 1: Potential Adoption
df_perf = pd.read_csv('csv/Potential_adoption_it2.CSV', index_col=False)
sns.boxplot(y=df_perf["Potential Adoption"], x=df_perf["Editor"], width=0.3, ax=axes[0])
#axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0, ha="center")
#axes[0].set_ylabel('Potential Adoption', labelpad=15)
axes[0].set(xticks=[], xlabel=None)  # Remove x-axis ticks and label
axes[0].set(ylabel=None)
axes[0].set_title(titles[0], fontsize=10)  # Added title

# Boxplot 2: Use in Company
df_perf = pd.read_csv('csv/UseInCompanyIT2.CSV', index_col=False)
sns.boxplot(y=df_perf["Use in Company"], x=df_perf["Editor"], width=0.3, ax=axes[1])
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0, ha="center")
#axes[1].set_ylabel('Use in Company', labelpad=15)
axes[1].set(xticks=[], xlabel=None)  # Remove x-axis ticks and label
axes[1].set(ylabel=None)
axes[1].set_title(titles[1], fontsize=10)  # Added title

# Boxplot 3: Easiness in Becoming Skilled
df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_it2.CSV', index_col=False)
sns.boxplot(y=df_perf["Easiness"], x=df_perf["Editor"], width=0.3, ax=axes[2])
axes[2].set_xticklabels(axes[2].get_xticklabels(), rotation=0, ha="center")
#axes[2].set_ylabel('Easiness', labelpad=15)
axes[2].set(xticks=[], xlabel=None)  # Remove x-axis ticks and label
axes[2].set(ylabel=None)
axes[2].set_title(titles[2], fontsize=10)  # Added title

# Boxplot 4: Recommendation
df_perf = pd.read_csv('csv/Recommendation_it2.CSV', index_col=False)
sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Editor"], width=0.3, ax=axes[3])
axes[3].set_xticklabels(axes[3].get_xticklabels(), rotation=0, ha="center")
#axes[3].set_ylabel('Recommendation', labelpad=15)
axes[3].set(xticks=[], xlabel=None)  # Remove x-axis ticks and label
axes[3].set(ylabel=None)
axes[3].set_title(titles[3], fontsize=10)  # Added title

# Save the figure
plt.savefig("pngboxplots_subplots/M37_Intention_of_use2_with_titles.png", dpi=dpi)

# Show the plot
plt.show()
