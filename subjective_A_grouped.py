import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual file name
file_path = 'Updated_Apendix_A_Navigation_Responses.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Specify the column numbers for grouping and box plot
response_column = 4  # 0-indexed, represents the 5th column
group_column_7 = 7    # 0-indexed, represents the 7th column
group_column_8 = 8    # 0-indexed, represents the 8th column

# Determine the order of categories for each subplot
order_7 = df.iloc[:, group_column_7].unique()
order_8 = df.iloc[:, group_column_8].unique()

# Create subplots with two side-by-side box plots, sharing y-axis only
fig, axes = plt.subplots(1, 5, figsize=(16, 8), sharey=True, gridspec_kw={'width_ratios': [2.5, 3, 5, 3, 2.5]})


# Create a box plot for group_column_7 with thinner bars and reduced space between bars
sns.boxplot(ax=axes[1], x=df.columns[group_column_7], y=df.columns[response_column],
            data=df, palette="husl", showfliers=False, width=0.8, order=order_7)
axes[1].set_ylabel("")  # Remove y-axis label
axes[1].set_xlabel("Guidance Approach")  # Set custom label for the outer x-axis label
axes[1].set_xticklabels(["Two-tactor", "Worst-axis"])  # Set custom labels for the x-axis ticks

# Create a box plot for group_column_8 with thinner bars and reduced space between bars
sns.boxplot(ax=axes[3], x=df.columns[group_column_8], y=df.columns[response_column],
            data=df, palette="husl", showfliers=False, width=0.8, order=order_8)
axes[3].yaxis.set_visible(False)
axes[3].set_xlabel("Guidance Metaphor")  # Set custom label for the outer x-axis label
axes[3].set_xticklabels(["Push", "Pull"])  # Set custom labels for the x-axis ticks

# Remove only the left and bottom spines
sns.despine(trim=False, left=False, bottom=False, ax=axes[0])
sns.despine(trim=False, left=True, bottom=False, ax=axes[1])
sns.despine(trim=False, left=True, bottom=False, ax=axes[2])
sns.despine(trim=False, left=True, bottom=False, ax=axes[3])
sns.despine(trim=False, left=True, bottom=False, ax=axes[4])

axes[1].yaxis.set_visible(False)
axes[0].xaxis.set_visible(False)
axes[2].yaxis.set_visible(False)
axes[2].xaxis.set_visible(False)
axes[4].yaxis.set_visible(False)
axes[4].xaxis.set_visible(False)
# sns.despine(trim=True, left=True, bottom=False, ax=axes[1])

# Adjust layout with increased horizontal space between subplots
plt.subplots_adjust(wspace=0)
# plt.tight_layout()
# Show the plot
plt.show()
