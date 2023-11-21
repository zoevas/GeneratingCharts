# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

color = ['#6495ED', '#B6D0E2']
sns.set_palette(color)
plt.rcParams['font.size'] = 14.0

fields = ['Editor', 'Perceived Usefulness']
df_perf = pd.read_csv('csv/perceived_usefulness_it1_nonexperts.CSV', index_col=False)
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["xtick.labelsize"] = 14

plt.figure(figsize=(4, 4))  # Adjust the width and height as needed
sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
# plt.tight_layout()
sns_plot.set_aspect(0.8)
sns_plot.set(xlabel=None)

fig = sns_plot.get_figure()
plt.savefig("pngboxplots/usefulness_non_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Perceived_Usefulness_experts_it1.csv', index_col=False)
plt.figure(figsize=(4, 4))  # Adjust the width and height as needed

sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set(xlabel=None)
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
plt.savefig("pngboxplots/usefulness_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Perceived_Usefulness_Use_Case_Owners_it1.csv', index_col=False)
plt.figure(figsize=(5, 4))  # Adjust the width and height as needed
sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set(xlabel=None)
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
plt.savefig("pngboxplots/usefulness_use_case.png", dpi=600)

df_perf = pd.read_csv('csv/Ease_of_Use_Non_Experts_it1.csv', index_col=False)

plt.figure(figsize=(4, 4))  # Adjust the width and height as needed
sns_plot = sns.boxplot(y=df_perf["Perceived Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set(xlabel=None)
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
plt.savefig("pngboxplots/ease_of_use_non_experts.png", dpi=600)


df_perf = pd.read_csv('csv/Ease_of_Use_Experts_it1.csv', index_col=False)

plt.figure(figsize=(4, 4))  # Adjust the width and height as needed
sns_plot = sns.boxplot(y=df_perf["Perceived Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set(xlabel=None)
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
plt.savefig("pngboxplots/ease_of_use_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Ease_of_Use_Use_Case_Owners_it1.csv', index_col=False)

plt.figure(figsize=(5, 4))  # Adjust the width and height as needed

sns_plot = sns.boxplot(y=df_perf["Perceived Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set(xlabel=None)
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
plt.savefig("pngboxplots/ease_of_use_case_owners.png", dpi=600)

df_perf = pd.read_csv('csv/Intention_to_use_non_experts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/potential_adoption_nonexperts.png", dpi=600)

df_perf = pd.read_csv('csv/Intention_to_use_experts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/potential_adoption_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Intention_to_use_use_case_owners.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/potential_adoption_use_case_owners", dpi=600)

df_perf = pd.read_csv('csv/UsingTheEditorAtACompany_nonexperts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/company_nonexperts.png", dpi=600)


df_perf = pd.read_csv('csv/UsingTheEditorAtCompany_UseCaseOwners.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/company_use_case.png", dpi=600)

df_perf = pd.read_csv('csv/Recommending.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Users"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/recommendation.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_nonexperts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/easiness_skilled_nonexperts.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_experts.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/easiness_skilled_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_usecase.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/easiness_skilled_use_case.png", dpi=600)

df_perf = pd.read_csv('csv/Perceived_usefulnessIT2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
sns_plot.set(xlabel=None)
sns_plot.set_xticks([])
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/usefulness_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Ease_of_use_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
plt.tight_layout()
sns_plot.set(xlabel=None)
fig = sns_plot.get_figure()
sns_plot.set_xticks([])
fig.savefig("pngboxplots/ease_of_use_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Potential_adoption_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Potential Adoption"], x=df_perf["Editor"], width=0.1, dodge=False)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
xmin, xmax = sns_plot.get_xlim()
sns_plot.set(xlabel=None)
#sns_plot.set_xlim(xmin + 0.3, xmax+0.3)
sns_plot.set_aspect(0.8)
sns_plot.set_xticks([])

fig = sns_plot.get_figure()
fig.savefig("pngboxplots/potential_adoption_it2.png", dpi=600)

df_perf = pd.read_csv('csv/UseInCompanyIT2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Use in Company"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/company_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Easiness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/easiness_skilled_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Recommendation_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=0, ha="center")
sns_plot.set_aspect(0.8)
fig = sns_plot.get_figure()
fig.savefig("pngboxplots/recommendation_it2.png", dpi=600)