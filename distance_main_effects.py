import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual file name
file_path = 'zone_calculation/total.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Specify the column numbers for grouping and box plot
response_column = 5  # 0-indexed, represents the 5th column
group_column_7 = 1    # 0-indexed, represents the 7th column
group_column_8 = 2  # 0-indexed, represents the 8th column
# group_column_metaphor = 2
# group_column_gender = 11

# Determine the order of categories for each subplot
order_7 = df.iloc[:, group_column_7].unique()
order_8 = df.iloc[:, group_column_8].unique()
# order_metaphor = df.iloc[:, group_column_metaphor].unique()
# order_gender = df.iloc[:, group_column_gender].unique()

# sns.set_theme(rc={'figure.figsize':(100, 8)})

# Create subplots with two side-by-side box plots, sharing y-axis only
fig, axes = plt.subplots(1, 3, figsize=(3.2, 8), sharey=True, gridspec_kw={'width_ratios': [1.5, 4, 1.5]})

axes[0].set_ylabel("Hand Trajectory Distance (cm)")

# Create a box plot for group_column_7 with thinner bars and reduced space between bars
sns.boxplot(ax=axes[1], x=df.columns[group_column_7], y=df.columns[response_column],
            data=df, palette=['skyblue', 'royalblue'], showfliers=False, order=order_7)
axes[1].set_ylabel("")  # Remove y-axis label
axes[1].set_xlabel("Layout")  # Set custom label for the outer x-axis label
axes[1].set_xticklabels(["H", "V"])  # Set custom labels for the x-axis ticks

# # Create a box plot for group_column_8 with thinner bars and reduced space between bars
# sns.boxplot(ax=axes[3], x=df.columns[group_column_8], y=df.columns[response_column],
#             data=df, palette=['lightgreen', 'forestgreen'], showfliers=False, order=order_8)
# axes[3].yaxis.set_visible(False)
# axes[3].set_xlabel("Metaphor")  # Set custom label for the outer x-axis label
# axes[3].set_xticklabels(["Pull", "Push"])  # Set custom labels for the x-axis ticks


# Remove only the left and bottom spines
sns.despine(trim=False, left=False, bottom=False, ax=axes[0])
sns.despine(trim=False, left=True, bottom=False, ax=axes[1])
sns.despine(trim=False, left=True, bottom=False, ax=axes[2])



axes[1].yaxis.set_visible(False)
axes[0].xaxis.set_visible(False)
axes[2].xaxis.set_visible(False)
axes[2].yaxis.set_visible(False)


# sns.despine(trim=True, left=True, bottom=False, ax=axes[1])

# Adjust layout with increased horizontal space between subplots
plt.subplots_adjust(wspace=0)
# plt.tight_layout()

# Increase font size for all elements
for ax in axes:
    ax.tick_params(axis='both', labelsize=16)  # Set font size for ticks
    ax.set_xlabel(ax.get_xlabel(), labelpad=15, weight='bold', fontsize=16)  # Set font size for x-axis label
    ax.set_ylabel(ax.get_ylabel(), fontsize=16)  # Set font size for y-axis label
    ax.set_title(ax.get_title(), fontsize=16)  # Set font size for title
# Show the plot
# plt.show()
plt.subplots_adjust(left=0.3, right=0.975)
plt.savefig("prelim_figures/distance_main_effects.png")
