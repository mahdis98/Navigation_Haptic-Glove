import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main_effects(axes):
    # Create box plots using Seaborn
    ax = sns.boxplot(ax=axes, data=data_h, x="Metaphor Approach", y="speed", showfliers=False,
                     width=0.6, order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
                     boxprops=dict(facecolor="white", edgecolor="black"),
                     whiskerprops=dict(color="black"),
                     capprops=dict(color="black"),
                     medianprops=dict(color="black"))

    sns.stripplot(ax=ax, data=data_h, x="Metaphor Approach", y="speed",
                  order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
                  dodge=True, jitter=0.2, color='black', size=4)

    # Manually set x-axis labels
    tick_positions = range(0, 4)
    tick_labels = ['TT', 'WA', 'TT', 'WA']
    axes.set_xticklabels(tick_labels)
    axes.tick_params(axis='both', labelsize=18)

    axes.text(0.5, -7, 'Push', ha='center', va='center', fontsize=18, weight='bold')
    axes.text(2.5, -7, 'Pull', ha='center', va='center', fontsize=18, weight='bold')

    axes.set_ylabel('Median Hand Speed (cm/s)', fontsize=18)
    axes.set_xlabel('', labelpad=15, weight='bold', fontsize=18)

    sns.despine(top=True, right=True, left=False, bottom=False, ax=axes)
    ax.legend([], [], frameon=False)
    axes.set_title("Horizontal", fontsize=25)


# Read the CSV file skipping the first row
data = pd.read_csv('zone_calculation/total.csv')

# Assuming the column indices
y_column_index = 6
group_column_index = 14
condition_column_index = 1

# Filtering the data
filtered_data = data
condition_data = filtered_data.iloc[:, condition_column_index]
data_h = data[condition_data == "horizontal"]

data_v = data[condition_data == "vertical"]

# Extracting the required columns
y_data = filtered_data.iloc[:, y_column_index].astype(float)
group_data = filtered_data.iloc[:, group_column_index]

# Create side-by-side box plots without outliers
fig, ax_t = plt.subplots(1, 2, figsize=(20, 8))

main_effects(ax_t[0])

axess = ax_t[1]

# Extracting the required columns
y_data_h = data_h.iloc[:, y_column_index].astype(float)
group_data_h = data_h.iloc[:, group_column_index]

# Create box plots using Seaborn
ax = sns.boxplot(ax=axess, data=data_v, x="Metaphor Approach", y="speed", showfliers=False, legend=False,
                 width=0.6, order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
                 boxprops=dict(facecolor="white", edgecolor="black"),
                 whiskerprops=dict(color="black"),
                 capprops=dict(color="black"),
                 medianprops=dict(color="black"))
sns.stripplot(ax=ax, data=data_v, x="Metaphor Approach", y="speed",
              order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
              dodge=True, jitter=0.2, color='black', size=4)

# Set y-axis limits and ticks
for axis in ax_t:
    axis.set_ylim(0, 50)
    axis.set_yticks(range(0, 51, 10))  # Major ticks
    # axis.set_yticks(range(0, 401, 10), minor=True)  # Minor ticks
    axis.grid(False)  # Disable grid

# Set labels and title
axess.set_ylabel('Median Hand Speed (cm/s)', fontsize=18)
axess.set_xlabel('', labelpad=15, weight='bold', fontsize=18)

# Manually set x-axis labels
tick_positions = range(0, 4)
tick_labels = ['TT', 'WA', 'TT', 'WA']
axess.set_xticklabels(tick_labels)
axess.tick_params(axis='both', labelsize=18)

axess.text(0.5, -7, 'Push', ha='center', va='center', fontsize=18, weight='bold')
axess.text(2.5, -7, 'Pull', ha='center', va='center', fontsize=18, weight='bold')
axess.set_title("Vertical", fontsize=25)

sns.despine(top=True, right=True, left=False, bottom=False, ax=axess)

plt.tight_layout()  # Adjust layout to prevent clipping of the legend
plt.savefig("HFES/speed_all.png", bbox_inches='tight')  # Save the plot with legend outside the plot
plt.show()
