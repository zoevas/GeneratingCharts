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
gs = fig.add_gridspec(1, 2, hspace=0.425, wspace=0.125)
axes = gs.subplots(sharex=True)
#way 2
# Create a single figure with two subplots sharing the same y-axis
#fig, axes = plt.subplots(2, 3, figsize=(fig_width, 4), dpi=dpi, sharey=True)  # Adjust the height as needed

df_perf = pd.read_csv('csv/Perceived_usefulnessIT2.CSV', index_col=False)

sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3, ax=axes[0])
axes[0].set_xticklabels([])
#axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=0, ha="center")
axes[0].set_aspect(0.8)
axes[0].set_ylabel('Perceived Usefulness')  # Add this line to set the y-axis label
axes[0].set(xlabel=None)



df_perf = pd.read_csv('csv/Ease_of_use_it2.CSV', index_col=False)

sns.boxplot(y=df_perf["Ease of Use"], x=df_perf["Editor"], width=0.3, ax=axes[1])
axes[1].set_xticklabels([])
#axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=0, ha="center")
axes[1].set_aspect(0.8)
axes[1].set_ylabel('Ease of Use')  # Add this line to set the y-axis label
axes[1].set(xlabel=None)


# Save the figure
plt.savefig("pngboxplots_subplots/M37_ease_of_use_usefulness.png", dpi=dpi)


# Show the plot (if needed)
plt.show()

