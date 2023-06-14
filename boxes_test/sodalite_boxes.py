# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

color = ['#6495ED', '#B6D0E2']
sns.set_palette(color)
plt.rcParams['font.size'] = 14.0

fields = ['Editor', 'Perceived Usefulness']
df_perf = pd.read_csv('csv/perceived_usefulness_it1_nonexperts.CSV', index_col=False)
plt.rcParams["figure.figsize"] = (8, 4)
plt.rcParams["xtick.labelsize"] = 14

sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/usefulness_non_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Perceived_Usefulness_experts_it1.csv', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/usefulness_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Perceived_Usefulness_Use_Case_Owners_it1.csv', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/usefulness_use_case.png", dpi=600)

df_perf = pd.read_csv('csv/Ease_of_Use_Experts_it1.csv', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Perceived Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/ease_of_use_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Ease_of_Use_Use_Case_Owners_it1.csv', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Perceived Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/ease_of_use_case_owners.png", dpi=600)

df_perf = pd.read_csv('csv/Intention_to_use_non_experts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/potential_adoption_nonexperts.png", dpi=600)

df_perf = pd.read_csv('csv/Intention_to_use_experts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/potential_adoption_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Intention_to_use_use_case_owners.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("potential_adoption_use_case_owners", dpi=600)

df_perf = pd.read_csv('csv/UsingTheEditorAtACompany_nonexperts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/company_nonexperts.png", dpi=600)


df_perf = pd.read_csv('csv/UsingTheEditorAtCompany_UseCaseOwners.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("company_use_case.png", dpi=600)

df_perf = pd.read_csv('csv/Recommending.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Users"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/recommendation.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_nonexperts.CSV', index_col=False)

sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/easiness_skilled_nonexperts.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_experts.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/easiness_skilled_experts.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_usecase.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Intention to use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/easiness_skilled_use_case.png", dpi=600)

df_perf = pd.read_csv('csv/Perceived_usefulnessIT2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Perceived Usefulness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/usefulness_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Ease_of_use_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Ease of Use"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/ease_of_use_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Potential_adoption_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Potential Adoption"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/potential_adoption_it2.png", dpi=600)

df_perf = pd.read_csv('csv/UseInCompanyIT2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Use in Company"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("company_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Easiness_in_becoming_skilled_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Easiness"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/easiness_skilled_it2.png", dpi=600)

df_perf = pd.read_csv('csv/Recommendation_it2.CSV', index_col=False)


sns_plot = sns.boxplot(y=df_perf["Recommendation"], x=df_perf["Editor"], width=0.3)
sns_plot.set_xticklabels(sns_plot.get_xticklabels(), rotation=15, ha="right")
plt.tight_layout()
fig = sns_plot.get_figure()
fig.savefig("png/recommendation_it2.png", dpi=600)