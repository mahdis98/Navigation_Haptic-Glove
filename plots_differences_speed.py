import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Read the CSV file skipping the first row
data = pd.read_csv('zone_calculation/total.csv', skiprows=1)

# Assuming the column indices
y_column_index = 6
group_column_index = 13
# gender_column_index = 7  # Index of the column containing 'Male' and 'Female'
# condition_column_index = 2  # Index of the column with 'Vertical'

# Filtering the data where the third column is 'Vertical'
# filtered_data = data[data.iloc[:, condition_column_index] == 'Vertical']
filtered_data = data
# Extracting the required columns from the filtered data
y_data = filtered_data.iloc[:, y_column_index]
group_data = filtered_data.iloc[:, group_column_index]
# gender_data = filtered_data.iloc[:, gender_column_index]

anova_result = f_oneway(y_data[group_data == 'push_two_tactor'],
                        y_data[group_data == 'pull_two_tactor'],
                        y_data[group_data == 'push_worst_axis'],
                        y_data[group_data == 'pull_worst_axis'])

# Print the ANOVA result
print("ANOVA p-value:", anova_result.pvalue)

# If the ANOVA result is significant, you can perform post-hoc tests (e.g., Tukey-Kramer)
if anova_result.pvalue < 0.05:
    # Perform Tukey-Kramer post-hoc test
    tukey_result = pairwise_tukeyhsd(y_data, group_data, alpha=0.05)

    # Print the post-hoc test results
    print(tukey_result)

# Create side-by-side box plots for each group based on 'Male' and 'Female' without outliers
plt.figure(figsize=(8, 5))  # Adjust the figure size

# custom_palette = {'Vertical_Push': 'white', 'Vertical_Pull': 'white',
#                   'Horizontal_Push': 'white', 'Horizontal_Pull': 'white'}

# sns.set_palette("Set4")
# Use Seaborn's boxplot function to create side-by-side plots with modified width and dodge parameters
ax = sns.boxplot(x=group_data, y=y_data, color = 'white', showfliers=False,
                 width=0.3,
                 order=['push_two_tactor', 'pull_two_tactor', 'push_worst_axis', 'pull_worst_axis'], legend=False)

# Set labels and title
plt.ylabel('Speed (cm/s)', fontsize=18)
plt.xlabel('')

def add_significance_bar(x1, x2, bar_height, bar_tips, p_value):
    plt.plot(
        [x1, x1, x2, x2],
        [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k'
    )
    sig_symbol = ''
    if p_value < 0.0001:
        sig_symbol = '<.0001' + '*'
    else:
        sig_symbol = str(p_value) + '*'
    text_height = bar_height + 0.26
    plt.text((x1 + x2) * 0.5, text_height, sig_symbol, ha='center', va='bottom', c='k', fontsize=14)

# Add significance bars
add_significance_bar(2, 3, 25.8, 24.8, 0.005)
# add_significance_bar(0, 2, 30, 29, tukey_result.pvalues[4])
# add_significance_bar(0, 3, 33, 32, tukey_result.pvalues[2])
# add_significance_bar(1, 3, 36, 35, tukey_result.pvalues[2])


# Manually set x-axis labels
tick_positions = range(0, 4)
tick_labels = ['Push', 'Pull', 'Push', 'Pull']
plt.xticks(tick_positions, tick_labels, fontsize=18)
plt.yticks(fontsize=18)

# Show legend outside the plot
# plt.legend(title='Gender', loc='upper right', fontsize=14, title_fontsize='14')


# plt.text(3.5, -0.15 * fig_height, 'Hate', ha='center', va='center', fontsize=12)



# Adjust y-axis limits to make space for the text
plt.ylim(top=28, bottom=2)

# Get current figure size
fig_height = plt.gcf().get_figheight()

# Manually set the y-axis position for the text labels
plt.text(0.5, -0.22 * fig_height, 'Two_tactor', ha='center', va='center', fontsize=18)
plt.text(2.5, -0.22 * fig_height, 'Worst_axis', ha='center', va='center', fontsize=18)

# Adjust figure size to accommodate the text labels
plt.gcf().set_size_inches(8, fig_height + 0.5)

plt.show()
