import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Read the CSV file skipping the first row
data = pd.read_csv('zone_calculation/total.csv', skiprows=1)

# Assuming the column indices
y_column_index = 10
group_column_index = 12
condition_column_index = 2

# Filtering the data
filtered_data = data

# Extracting the required columns
y_data = filtered_data.iloc[:, y_column_index]
group_data = filtered_data.iloc[:, group_column_index]

# Perform ANOVA
anova_result = f_oneway(
    y_data[group_data == 'Vertical_Push'],
    y_data[group_data == 'Vertical_Pull'],
    y_data[group_data == 'Horizontal_Push'],
    y_data[group_data == 'Horizontal_Pull']
)

# Print the ANOVA result
print("ANOVA p-value:", anova_result.pvalue)

# If the ANOVA result is significant, perform post-hoc tests (e.g., Tukey-Kramer)
if anova_result.pvalue < 0.05:
    tukey_result = pairwise_tukeyhsd(y_data, group_data, alpha=0.05)
    print(tukey_result)

# Create side-by-side box plots without outliers
plt.figure(figsize=(12, 8))

# Set a custom color palette for the bars
custom_palette = ['lightgreen', 'forestgreen']
sns.set_palette(custom_palette)

# Create box plots using Seaborn
ax = sns.boxplot(x=group_data, y=y_data, showfliers=False, palette = ['lightgreen', 'forestgreen'],
                 width=0.3, order=['vertical_pull', 'vertical_push', 'horizontal_pull', 'horizontal_push'])

custom_palette = ['lightgreen', 'forestgreen']
sns.set_palette(custom_palette)
# Set labels and title
plt.ylabel('Time (s)', fontsize=16)
plt.xlabel('')

# Function to add significance bars
def add_significance_bar(x1, x2, bar_height, bar_tips, p_value):
    plt.plot([x1, x1, x2, x2], [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k')
    sig_symbol = ''
    text_height = bar_height + 2
    plt.text((x1 + x2) * 0.5, text_height, sig_symbol, ha='center', va='bottom', c='k', fontsize=14)

# Add significance bars
add_significance_bar(0, 1, 143, 140, "")
add_significance_bar(0, 3, 123, 120, "")
add_significance_bar(0, 2, 133, 130, "")
add_significance_bar(2, 3, 93, 90, "")

# Manually set x-axis labels
tick_positions = range(0, 4)
tick_labels = ['Pull', 'Push', 'Pull', 'Push']
plt.xticks(tick_positions, tick_labels, fontsize=16)
plt.yticks(fontsize=16)

fig_height = plt.gcf().get_figheight()

plt.text(0.5, -15, 'Vertical', ha='center', va='center', fontsize=18)
plt.text(2.5, -15, 'Horizontal', ha='center', va='center', fontsize=18)

# Adjust y-axis limits to make space for the text
plt.ylim(top=155, bottom=-0.2)

# Remove top and right frames
sns.despine(top=True, right=True, left=False, bottom=False)

plt.tight_layout()
# plt.show()
plt.savefig("./time_interaction.png")
