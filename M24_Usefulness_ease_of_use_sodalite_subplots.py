import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the first CSV file
df_perf_usefulness = pd.read_csv('csv/Perceived_Usefulness_Use_Case_Owners_it1.csv', index_col=False)

# Read the second CSV file
df_perf_ease_of_use = pd.read_csv('csv/Ease_of_Use_Use_Case_Owners_it1.csv', index_col=False)

# Identify common x-axis categories (assuming both dataframes share the same x-axis categories)
common_categories = set(df_perf_usefulness["Editor"]).intersection(set(df_perf_ease_of_use["Editor"]))

# Filter dataframes to include only common categories
df_perf_usefulness_common = df_perf_usefulness[df_perf_usefulness["Editor"].isin(common_categories)]
df_perf_ease_of_use_common = df_perf_ease_of_use[df_perf_ease_of_use["Editor"].isin(common_categories)]

# Set the desired width in pixels
width_in_pixels = 1000

# Calculate the required figure width in inches based on the DPI
dpi = width_in_pixels / 10  # Assuming 10 inches in width
fig_width = width_in_pixels / dpi

#way 1
fig = plt.figure()
gs = fig.add_gridspec(2, 3, hspace=0.325, wspace=0)
axes = gs.subplots(sharey=True)
#way 2
# Create a single figure with two subplots sharing the same y-axis
#fig, axes = plt.subplots(2, 3, figsize=(fig_width, 4), dpi=dpi, sharey=True)  # Adjust the height as needed

df_perf_usefulness_non_experts = pd.read_csv('csv/perceived_usefulness_it1_nonexperts.CSV', index_col=False)

df_perf_ease_of_use_non_experts = pd.read_csv('csv/Ease_of_Use_Non_Experts_it1.csv', index_col=False)

sns.boxplot(y=df_perf_ease_of_use_non_experts["Perceived Ease of Use"], x=df_perf_ease_of_use_non_experts["Editor"], width=0.3, ax=axes[0, 0])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=0, ha="center")
axes[0, 0].set(xlabel=None)
axes[0, 0].set_aspect(0.8)


df_perf_ease_of_use_experts = pd.read_csv('csv/Ease_of_Use_Experts_it1.csv', index_col=False)

# Plot for "Perceived Usefulness" use case owners
sns.boxplot(y=df_perf_ease_of_use_experts["Perceived Ease of Use"], x=df_perf_ease_of_use_experts["Editor"], width=0.3, ax=axes[0, 1])
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=0, ha="center")
axes[0, 1].set_aspect(0.8)
axes[0, 1].set_ylabel('Perceived Ease of Use')  # Add this line to set the y-axis label
axes[0, 1].set(xlabel=None)


# Plot for "Perceived Ease of Use" use case owners
sns.boxplot(y=df_perf_ease_of_use_common["Perceived Ease of Use"], x=df_perf_ease_of_use_common["Editor"], width=0.3, ax=axes[0, 2])
axes[0, 2].set_xticklabels(axes[0, 2].get_xticklabels(), rotation=0, ha="center")
axes[0, 2].set_aspect(0.8)
axes[0, 2].set_ylabel('Perceived Ease of Use')  # Add this line to set the y-axis label
axes[0, 2].set(xlabel=None)




# Plot for "Perceived Ease of Use" use case owners
sns.boxplot(y=df_perf_usefulness_non_experts["Perceived Usefulness"], x=df_perf_usefulness_non_experts["Editor"], width=0.3, ax=axes[1, 0])
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=0, ha="center")
axes[1, 0].set(xlabel=None)
axes[1, 0].set_aspect(0.8)
axes[1, 0].set_ylabel('Perceived  Usefulness')

df_perf_usefulness_experts = pd.read_csv('csv/Perceived_Usefulness_experts_it1.csv', index_col=False)

sns.boxplot(y=df_perf_usefulness_experts["Perceived Usefulness"], x=df_perf_usefulness_experts["Editor"], width=0.3, ax=axes[1, 1])
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=0, ha="center")
axes[1, 1].set(xlabel=None)
axes[1, 1].set_aspect(0.8)

sns.boxplot(y=df_perf_usefulness_common["Perceived Usefulness"], x=df_perf_usefulness_common["Editor"], width=0.3, ax=axes[1, 2])
axes[1, 2].set_xticklabels(axes[1, 2].get_xticklabels(), rotation=0, ha="center")
axes[1, 2].set(xlabel=None)
axes[1, 2].set_aspect(0.8)



# Adjust layout for better spacing
#fig.tight_layout()
fig.subplots_adjust(wspace=0.125)  # Adjust the value for your desired spacing

# Save the figure
plt.savefig("pngboxplots_subplots/M24_perceived_usefulness_ease_of_use.png", dpi=dpi)

# gridspec https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

# Show the plot (if needed)
plt.show()