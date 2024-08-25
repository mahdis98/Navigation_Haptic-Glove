import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def main_effects(axes):
    # Create box plots using Seaborn
    ax = sns.boxplot(ax=axes, data=data_h, x="Metaphor Approach", y="total_distance", showfliers=False, color='k',
                     fill=False, hue="Gender",
                     width=0.8, order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
                     gap=0.2)
    sns.stripplot(ax=ax, data=data_h, x="Metaphor Approach", y="total_distance",
                  order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
                  palette=['blue', 'red'], hue="Gender", dodge=True)

    # Manually set x-axis labels
    tick_positions = range(0, 4)
    tick_labels = ['TT', 'WA', 'TT', 'WA']
    axes.set_xticklabels(tick_labels)
    # axess.xticks(tick_positions, tick_labels, fontsize=16)
    # axess.set_yticklabels(fontsize=16)
    axes.tick_params(axis='both', labelsize=18)

    axes.text(0.5, -400, 'Push', ha='center', va='center', fontsize=18, weight='bold')
    axes.text(2.5, -400, 'Pull', ha='center', va='center', fontsize=18, weight='bold')
    # axes.text(1.5, -30, 'Vertical', ha='center', va='center', fontsize=18, weight='bold')

    # Adjust y-axis limits to make space for the text
    axes.set_ylim(top=3850, bottom=-3)
    axes.set_ylabel('Hand Trajectory Distance (cm)', fontsize=18)
    axes.set_xlabel('', labelpad=15, weight='bold', fontsize=18)

    # Remove top and right frames
    sns.despine(top=True, right=True, left=False, bottom=False, ax=axes)
    ax.legend([], [], frameon=False)
    # ax.legend(loc=2, prop={'size': 6})
    axes.set_title("Horizontal", fontsize=25)


# Read the CSV file skipping the first row
data = pd.read_csv('zone_calculation/total.csv')

# Assuming the column indices
y_column_index = 5
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
print(group_data)

# Create side-by-side box plots without outliers
fig, ax_t = plt.subplots(1, 2, figsize=(20, 8))

main_effects(ax_t[0])

axess = ax_t[1]

# Extracting the required columns
y_data_h = data_h.iloc[:, y_column_index].astype(float)
group_data_h = data_h.iloc[:, group_column_index]

# Create box plots using Seaborn
ax = sns.boxplot(ax=axess, data=data_v, x="Metaphor Approach", y="total_distance", showfliers=False, legend=False,
                 color='k', fill=False, hue="Gender",
                 width=0.8, order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'], gap=0.2)
sns.stripplot(ax=ax, data=data_v, x="Metaphor Approach", y="total_distance",
              order=['push_two_tactor', 'push_worst_axis', 'pull_two_tactor', 'pull_worst_axis'],
              palette=['blue', 'red'], hue="Gender", dodge=True)
# ax.legened(loc=2, prop={'size': 6})
# custom_palette = ['lightgreen', 'forestgreen']
# sns.set_palette(custom_palette)


# Set labels and title
axess.set_ylabel('Hand Trajectory Distance (cm)', fontsize=18)
axess.set_xlabel('', labelpad=15, weight='bold', fontsize=18)

# Manually set x-axis labels
tick_positions = range(0, 4)
tick_labels = ['TT', 'WA', 'TT', 'WA']
axess.set_xticklabels(tick_labels)
# axess.xticks(tick_positions, tick_labels, fontsize=16)
# axess.set_yticklabels(fontsize=16)
axess.tick_params(axis='both', labelsize=18)

axess.text(0.5, -400, 'Push', ha='center', va='center', fontsize=18, weight='bold')
axess.text(2.5, -400, 'Pull', ha='center', va='center', fontsize=18, weight='bold')
axess.set_title("Vertical", fontsize=25)
# Adjust y-axis limits to make space for the text
axess.set_ylim(top=3850, bottom=-3)

# Remove top and right frames
sns.despine(top=True, right=True, left=False, bottom=False, ax=axess)

# subfigs[1].tight_layout()
# plt.show()
legend = plt.legend(title="Gender", fontsize=18, title_fontsize=18, loc='upper left', bbox_to_anchor=(1.05, 1))

for handle in legend.legendHandles:
    handle.set_marker('s')  # Set the marker style to 's'
    handle.set_markersize(10)  # Set the marker size to 10 (adjust as needed)

plt.tight_layout()  # Adjust layout to prevent clipping of the legend
plt.savefig("Prelim_figures_final/distance_all.png", bbox_inches='tight')  # Save the plot with legend outside the plot
# plt.show()

