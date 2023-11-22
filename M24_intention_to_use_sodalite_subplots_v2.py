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
gs = fig.add_gridspec(4, 3, hspace=0.825, wspace=0.125)
axes = gs.subplots(sharey=True)
#way 2
# Create a single figure with two subplots sharing the same y-axis
#fig, axes = plt.subplots(2, 3, figsize=(fig_width, 4), dpi=dpi, sharey=True)  # Adjust the height as needed

df_perf = pd.read_csv('csv/Intention_to_use_non_experts.CSV', index_col=False)

sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[0, 0])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=0, ha="center")
axes[0, 0].set_aspect(0.8)
axes[0, 0].set_ylabel('Adoption')  # Add this line to set the y-axis label
axes[0, 0].set(xlabel=None)



df_perf = pd.read_csv('csv/Intention_to_use_experts.CSV', index_col=False)

sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[0, 1])
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=0, ha="center")
axes[0, 1].set_aspect(0.8)
axes[0, 1].set_ylabel('Adoption')  # Add this line to set the y-axis label
axes[0, 1].set(xlabel=None)

df_perf = pd.read_csv('csv/Intention_to_use_use_case_owners.CSV', index_col=False)

sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[0, 2])
axes[0, 2].set_xticklabels(axes[0, 2].get_xticklabels(), rotation=0, ha="center")
axes[0, 2].set_aspect(0.8)
axes[0, 2].set_ylabel('Adoption')  # Add this line to set the y-axis label
axes[0, 2].set(xlabel=None)



df_perf = pd.read_csv('csv/UsingTheEditorAtACompany_nonexperts.CSV', index_col=False)
sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[1, 0])
axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=0, ha="center")
axes[1, 0].set_aspect(0.8)
axes[1, 0].set_ylabel('Future use')  # Add this line to set the y-axis label
axes[1, 0].set(xlabel=None)

df_perf = pd.read_csv('csv/UsingTheEditorAtACompany_experts.CSV', index_col=False)
sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[1, 1])
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=0, ha="center")
axes[1, 1].set_aspect(0.8)
axes[1, 1].set_ylabel('Future use')  # Add this line to set the y-axis label
axes[1, 1].set(xlabel=None)

df_perf = pd.read_csv('csv/UsingTheEditorAtCompany_UseCaseOwners.CSV', index_col=False)
sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[1, 2])
axes[1, 2].set_xticklabels(axes[1, 2].get_xticklabels(), rotation=0, ha="center")
axes[1, 2].set_aspect(0.8)
axes[1, 2].set_ylabel('Future use')  # Add this line to set the y-axis label
axes[1, 2].set(xlabel=None)



df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_nonexperts.CSV', index_col=False)
sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[2, 0])
axes[2, 0].set_xticklabels(axes[2, 0].get_xticklabels(), rotation=0, ha="center")
axes[2, 0].set_aspect(0.8)
axes[2, 0].set_ylabel('Easiness')  # Add this line to set the y-axis label
axes[2, 0].set(xlabel=None)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_experts.CSV', index_col=False)
sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[2, 1])
axes[2, 1].set_xticklabels(axes[2, 1].get_xticklabels(), rotation=0, ha="center")
axes[2, 1].set_aspect(0.8)
axes[2, 1].set_ylabel('Easiness')  # Add this line to set the y-axis label
axes[2, 1].set(xlabel=None)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_usecase.CSV', index_col=False)
sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3, ax=axes[2, 2])
axes[2, 2].set_xticklabels(axes[2, 2].get_xticklabels(), rotation=0, ha="center")
axes[2, 2].set_aspect(0.8)
axes[2, 2].set_ylabel('Easiness')  # Add this line to set the y-axis label
axes[2, 2].set(xlabel=None)


# Adjust layout for better spacing
#fig.tight_layout()
#fig.subplots_adjust(wspace=0.125)  # Adjust the value for your desired spacing

# Save the figure



df_perf = pd.read_csv('csv/Recommending_it1_non_experts.CSV', index_col=False)

sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Users"], width=0.3, ax=axes[3, 0])
axes[3, 0].set_xticklabels(axes[3, 0].get_xticklabels(), rotation=0, ha="center")
axes[3, 0].set_aspect(0.8)
axes[3, 0].set_ylabel('Recommendation')  # Add this line to set the y-axis label
axes[3, 0].set(xlabel='IDE')
axes[3, 0].set_xticklabels([])


df_perf = pd.read_csv('csv/Recommending_it1_tosca_experts.CSV', index_col=False)

sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Users"], width=0.3,  ax=axes[3, 1])
axes[3, 1].set_xticklabels(axes[3, 1].get_xticklabels(), rotation=0, ha="center")
axes[3, 1].set_aspect(0.8)
axes[3, 1].set_xticklabels([])

axes[3, 1].set_ylabel('Recommendation')  # Add this line to set the y-axis label
axes[3, 1].set(xlabel='IDE')

df_perf = pd.read_csv('csv/Recommending_it1_use_case_owners.CSV', index_col=False)

sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Users"], width=0.3,  ax=axes[3, 2])
axes[3, 2].set_xticklabels(axes[3, 2].get_xticklabels(), rotation=0, ha="center")
axes[3, 2].set_aspect(0.8)
axes[3, 2].set_xticklabels([])
axes[3, 2].set_ylabel('Recommendation')  # Add this line to set the y-axis label
axes[3, 2].set(xlabel='IDE')


# Read data and create box plots
for i in range(4):
    for j in range(3):
       axes[i, j].set_aspect('auto', adjustable='datalim')  # Set aspect ratio for x-axis
   #     axes[i, j].set_aspect(0.4)

fig.align_ylabels()
fig.tight_layout()
fig.subplots_adjust(wspace=0.0)  # Adjust the value for your desired spacing in the x-axis


plt.savefig("pngboxplots_subplots/M24_Intention_of_use.png", dpi=dpi)
plt.show()