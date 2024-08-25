import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def main_effects(f):
    file_path = 'zone_calculation/total.csv'

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Specify the column numbers for grouping and box plot
    response_column = 9  # 0-indexed, represents the 5th column
    group_column_7 = 1  # 0-indexed, represents the 7th column
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
    axes = f.subplots(1, 5, sharey=True, gridspec_kw={'width_ratios': [1.5, 4, 2.5, 4, 1.5]})

    axes[0].set_ylabel("Percentage of Time in Critical Area (%)")

    # Create a box plot for group_column_7 with thinner bars and reduced space between bars
    sns.boxplot(ax=axes[1], x=df.columns[group_column_7], y=df.columns[response_column],
                width=0.65, data=df, palette=['skyblue', 'royalblue'], showfliers=False, order=order_7)
    axes[1].set_ylabel("")  # Remove y-axis label
    axes[1].set_xlabel("Layout")  # Set custom label for the outer x-axis label
    axes[1].set_xticklabels(["H", "V"])  # Set custom labels for the x-axis ticks

    # Create a box plot for group_column_8 with thinner bars and reduced space between bars
    sns.boxplot(ax=axes[3], x=df.columns[group_column_8], y=df.columns[response_column],
                width=0.65, data=df, palette=['lightgreen', 'forestgreen'], showfliers=False, order=order_8)
    axes[3].yaxis.set_visible(False)
    axes[3].set_xlabel("Metaphor")  # Set custom label for the outer x-axis label
    axes[3].set_xticklabels(["Pull", "Push"])  # Set custom labels for the x-axis ticks

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
    f.subplots_adjust(wspace=0)
    # plt.tight_layout()

    # Increase font size for all elements
    for ax in axes:
        ax.tick_params(axis='both', labelsize=18)  # Set font size for ticks
        ax.set_xlabel(ax.get_xlabel(), labelpad=15, weight='bold', fontsize=18)  # Set font size for x-axis label
        ax.set_ylabel(ax.get_ylabel(), fontsize=18)  # Set font size for y-axis label
        ax.set_title(ax.get_title(), fontsize=18)  # Set font size for title
        ax.set_ylim(top=110)


# Read the CSV file skipping the first row
# data = pd.read_csv('zone_calculation/total.csv', skiprows=1)
#
# # Assuming the column indices
# y_column_index = 14
# group_column_index = 12
# # condition_column_index = 2
#
# # Filtering the data
# filtered_data = data
#
# # Extracting the required columns
# y_data = filtered_data.iloc[:, y_column_index]
# group_data = filtered_data.iloc[:, group_column_index]

# Perform ANOVA
# anova_result = f_oneway(
#     y_data[group_data == 'Vertical_Push'],
#     y_data[group_data == 'Vertical_Pull'],
#     y_data[group_data == 'Horizontal_Push'],
#     y_data[group_data == 'Horizontal_Pull']
# )
#
# # Print the ANOVA result
# print("ANOVA p-value:", anova_result.pvalue)
#
# # If the ANOVA result is significant, perform post-hoc tests (e.g., Tukey-Kramer)
# if anova_result.pvalue < 0.05:
#     tukey_result = pairwise_tukeyhsd(y_data, group_data, alpha=0.05)
#     print(tukey_result)

# Create side-by-side box plots without outliers
fig = plt.figure(figsize=(9, 8))

# subfigs = fig.subfigures(1, 2, width_ratios=(3, 2))
#
main_effects(fig)
#
# axess = subfigs[1].subplots(1, 1)
#
# # Set a custom color palette for the bars
# custom_palette = ['lightgreen', 'forestgreen']
# sns.set_palette(custom_palette)
#
# # Create box plots using Seaborn
# ax = sns.boxplot(ax=axess, x=group_data, y=y_data, showfliers=False, palette=['lightgreen', 'forestgreen'],
#                  width=0.5, order=['vertical_pull', 'vertical_push', 'horizontal_pull', 'horizontal_push'])
#
# custom_palette = ['lightgreen', 'forestgreen']
# sns.set_palette(custom_palette)
#
# # Set labels and title
# axess.set_ylabel('Percentage of Time in Critical Area (%)', fontsize=18)
# axess.set_xlabel('', labelpad=15, weight='bold', fontsize=18)
#
#
# # Function to add significance bars
# def add_significance_bar(x1, x2, bar_height, bar_tips, p_value, ax1):
#     ax1.plot([x1, x1, x2, x2], [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k')
#     sig_symbol = ''
#     text_height = bar_height + 2
#     ax1.text((x1 + x2) * 0.5, text_height, sig_symbol, ha='center', va='bottom', c='k', fontsize=14)
#
#
# # Add significance bars
# add_significance_bar(1, 2, 103, 102, "", axess)
# add_significance_bar(1, 3, 110, 109, "", axess)
# add_significance_bar(2, 3, 117, 116, "", axess)
# add_significance_bar(0, 2, 124, 123, "", axess)
# add_significance_bar(0, 3, 131, 130, "", axess)
#
# # Manually set x-axis labels
# tick_positions = range(0, 4)
# tick_labels = ['Pull', 'Push', 'Pull', 'Push']
# axess.set_xticklabels(tick_labels)
# # axess.xticks(tick_positions, tick_labels, fontsize=16)
# # axess.set_yticklabels(fontsize=16)
# axess.tick_params(axis='both', labelsize=18)
#
# axess.text(0.5, -22, 'Vertical', ha='center', va='center', fontsize=18)
# axess.text(2.5, -22, 'Horizontal', ha='center', va='center', fontsize=18)
#
# # Adjust y-axis limits to make space for the text
# axess.set_ylim(top=140)
# # print("hey")
# # Remove top and right frames
# sns.despine(top=True, right=True, left=False, bottom=False, ax=axess)

# subfigs[1].tight_layout()
# plt.show()
plt.savefig("prelim_figures/percentage_time_all.png")
