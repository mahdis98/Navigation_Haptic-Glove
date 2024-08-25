import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def main_effects_1(f):
    file_path = 'Updated_Apendix_A_Navigation_Responses.csv'
    df = pd.read_csv(file_path)

    # Assuming the column indices
    y_column_index = 4
    layout_index = 10
    approach_index = 7
    metaphor_index = 8
    # condition_column_index = 2

    # Filtering the data
    filtered_data = data

    # Create subplots with two side-by-side box plots, sharing y-axis only
    axes = f.subplots(1, 9, sharey=True, gridspec_kw={'width_ratios': [1.5, 4, 2.5, 4, 2.5, 4, 2.5, 4, 1.5]})

    axes[0].set_ylabel("Likert Scale")

    # Create a box plot for group_column_7 with thinner bars and reduced space between bars
    sns.barplot(data=df, ax=axes[1], x=df.columns[layout_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['skyblue', 'royalblue'], order=['horizontal', 'vertical'])
    axes[1].set_ylabel("")  # Remove y-axis label
    axes[1].set_xlabel("Layout")  # Set custom label for the outer x-axis label
    axes[1].set_xticklabels(["H", "V"])  # Set custom labels for the x-axis ticks

    sns.barplot(data=df, ax=axes[3], x=df.columns[approach_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightcoral', 'firebrick'], order=['worst-axis', 'two-tactor'])
    axes[3].yaxis.set_visible(False)
    axes[3].set_xlabel("Approach")  # Set custom label for the outer x-axis label
    axes[3].set_xticklabels(["WA", "TT"])

    # Create a box plot for group_column_8 with thinner bars and reduced space between bars
    sns.barplot(data=df, ax=axes[5], x=df.columns[metaphor_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightgreen', 'forestgreen'], order=['push', 'pull'])
    axes[5].yaxis.set_visible(False)
    axes[5].set_xlabel("Metaphor")  # Set custom label for the outer x-axis label
    axes[5].set_xticklabels(["Push", "Pull"])  # Set custom labels for the x-axis ticks

    sns.barplot(data=df, ax=axes[7], x=df.columns[gender_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightsalmon', 'orangered'], order=['M', 'F'])
    axes[7].yaxis.set_visible(False)
    axes[7].set_xlabel("Gender")  # Set custom label for the outer x-axis label
    axes[7].set_xticklabels(["M", "F"])  # Set custom labels for the x-axis ticks

    # Remove only the left and bottom spines
    sns.despine(trim=False, left=False, bottom=False, ax=axes[0])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[1])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[2])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[3])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[4])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[5])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[6])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[7])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[8])

    axes[1].yaxis.set_visible(False)
    axes[0].xaxis.set_visible(False)
    axes[2].yaxis.set_visible(False)
    axes[2].xaxis.set_visible(False)
    axes[4].yaxis.set_visible(False)
    axes[4].xaxis.set_visible(False)
    axes[6].yaxis.set_visible(False)
    axes[6].xaxis.set_visible(False)
    axes[8].yaxis.set_visible(False)
    axes[8].xaxis.set_visible(False)

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
        ax.set_ylim(top=7.5)

    def add_significance_bar(x1, x2, bar_height, bar_tips, p_value, ax1):
        ax1.plot([x1, x1, x2, x2], [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k')
        sig_symbol = ''
        text_height = bar_height + 2
        ax1.text((x1 + x2) * 0.5, text_height, sig_symbol, ha='center', va='bottom', c='k', fontsize=14)

    # Add significance bars
    add_significance_bar(0, 1, 7.5, 7.3, "", axes[1])
    add_significance_bar(0, 1, 7.5, 7.3, "", axes[3])
    add_significance_bar(0, 1, 7.5, 7.3, "", axes[5])




def main_effects_2(f):
    file_path = 'Updated_Apendix_A_Navigation_Responses.csv'
    df = pd.read_csv(file_path)

    # Assuming the column indices
    y_column_index = 5
    layout_index = 10
    approach_index = 7
    metaphor_index = 8
    # condition_column_index = 2

    # Filtering the data
    filtered_data = data

    # Create subplots with two side-by-side box plots, sharing y-axis only
    axes = f.subplots(1, 9, sharey=True, gridspec_kw={'width_ratios': [1.5, 4, 2.5, 4, 2.5, 4, 2.5, 4, 1.5]})

    axes[0].set_ylabel("Likert Scale")

    # Create a box plot for group_column_7 with thinner bars and reduced space between bars
    sns.barplot(data=df, ax=axes[1], x=df.columns[layout_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['skyblue', 'royalblue'], order=['horizontal', 'vertical'])
    axes[1].set_ylabel("")  # Remove y-axis label
    axes[1].set_xlabel("Layout")  # Set custom label for the outer x-axis label
    axes[1].set_xticklabels(["H", "V"])  # Set custom labels for the x-axis ticks

    sns.barplot(data=df, ax=axes[3], x=df.columns[approach_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightcoral', 'firebrick'], order=['worst-axis', 'two-tactor'])
    axes[3].yaxis.set_visible(False)
    axes[3].set_xlabel("Approach")  # Set custom label for the outer x-axis label
    axes[3].set_xticklabels(["WA", "TT"])

    # Create a box plot for group_column_8 with thinner bars and reduced space between bars
    sns.barplot(data=df, ax=axes[5], x=df.columns[metaphor_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightgreen', 'forestgreen'], order=['push', 'pull'])
    axes[5].yaxis.set_visible(False)
    axes[5].set_xlabel("Metaphor")  # Set custom label for the outer x-axis label
    axes[5].set_xticklabels(["Push", "Pull"])  # Set custom labels for the x-axis ticks

    sns.barplot(data=df, ax=axes[7], x=df.columns[gender_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightsalmon', 'orangered'], order=['M', 'F'])
    axes[7].yaxis.set_visible(False)
    axes[7].set_xlabel("Gender")  # Set custom label for the outer x-axis label
    axes[7].set_xticklabels(["M", "F"])  # Set custom labels for the x-axis ticks

    # Remove only the left and bottom spines
    sns.despine(trim=False, left=False, bottom=False, ax=axes[0])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[1])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[2])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[3])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[4])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[5])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[6])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[7])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[8])

    axes[1].yaxis.set_visible(False)
    axes[0].xaxis.set_visible(False)
    axes[2].yaxis.set_visible(False)
    axes[2].xaxis.set_visible(False)
    axes[4].yaxis.set_visible(False)
    axes[4].xaxis.set_visible(False)
    axes[6].yaxis.set_visible(False)
    axes[6].xaxis.set_visible(False)
    axes[8].yaxis.set_visible(False)
    axes[8].xaxis.set_visible(False)

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
        ax.set_ylim(top=7.5)

    def add_significance_bar(x1, x2, bar_height, bar_tips, p_value, ax1):
        ax1.plot([x1, x1, x2, x2], [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k')
        sig_symbol = ''
        text_height = bar_height + 2
        ax1.text((x1 + x2) * 0.5, text_height, sig_symbol, ha='center', va='bottom', c='k', fontsize=14)

    # Add significance bars

    add_significance_bar(0, 1, 7.5, 7.3, "", axes[3])
    add_significance_bar(0, 1, 7.5, 7.3, "", axes[5])
def main_effects_3(f):
    file_path = 'Updated_Apendix_A_Navigation_Responses.csv'
    df = pd.read_csv(file_path)

    # Assuming the column indices
    y_column_index = 6
    layout_index = 10
    approach_index = 7
    metaphor_index = 8
    gender_index = 2
    # condition_column_index = 2

    # Filtering the data
    filtered_data = data

    # Create subplots with two side-by-side box plots, sharing y-axis only
    axes = f.subplots(1, 9, sharey=True, gridspec_kw={'width_ratios': [1.5, 4, 2.5, 4, 2.5, 4, 2.5, 4, 1.5]})

    axes[0].set_ylabel("Likert Scale")

    # Create a box plot for group_column_7 with thinner bars and reduced space between bars
    sns.barplot(data=df, ax=axes[1], x=df.columns[layout_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['skyblue', 'royalblue'], order=['horizontal', 'vertical'])
    axes[1].set_ylabel("")  # Remove y-axis label
    axes[1].set_xlabel("Layout")  # Set custom label for the outer x-axis label
    axes[1].set_xticklabels(["H", "V"])  # Set custom labels for the x-axis ticks

    sns.barplot(data=df, ax=axes[3], x=df.columns[approach_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightcoral', 'firebrick'], order=['worst-axis', 'two-tactor'])
    axes[3].yaxis.set_visible(False)
    axes[3].set_xlabel("Approach")  # Set custom label for the outer x-axis label
    axes[3].set_xticklabels(["WA", "TT"])

    # Create a box plot for group_column_8 with thinner bars and reduced space between bars
    sns.barplot(data=df, ax=axes[5], x=df.columns[metaphor_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightgreen', 'forestgreen'], order=['push', 'pull'])
    axes[5].yaxis.set_visible(False)
    axes[5].set_xlabel("Metaphor")  # Set custom label for the outer x-axis label
    axes[5].set_xticklabels(["Push", "Pull"])  # Set custom labels for the x-axis ticks

    sns.barplot(data=df, ax=axes[7], x=df.columns[gender_index], y=df.columns[y_column_index],
                ci='sd', capsize=.2, palette=['lightsalmon', 'orangered'], order=['M', 'F'])
    axes[7].yaxis.set_visible(False)
    axes[7].set_xlabel("Gender")  # Set custom label for the outer x-axis label
    axes[7].set_xticklabels(["M", "F"])  # Set custom labels for the x-axis ticks

    # Remove only the left and bottom spines
    sns.despine(trim=False, left=False, bottom=False, ax=axes[0])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[1])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[2])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[3])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[4])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[5])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[6])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[7])
    sns.despine(trim=False, left=True, bottom=False, ax=axes[8])

    axes[1].yaxis.set_visible(False)
    axes[0].xaxis.set_visible(False)
    axes[2].yaxis.set_visible(False)
    axes[2].xaxis.set_visible(False)
    axes[4].yaxis.set_visible(False)
    axes[4].xaxis.set_visible(False)
    axes[6].yaxis.set_visible(False)
    axes[6].xaxis.set_visible(False)
    axes[8].yaxis.set_visible(False)
    axes[8].xaxis.set_visible(False)

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
        ax.set_ylim(top=7.5)

    def add_significance_bar(x1, x2, bar_height, bar_tips, p_value, ax1):
        ax1.plot([x1, x1, x2, x2], [bar_tips, bar_height, bar_height, bar_tips], lw=1, c='k')
        sig_symbol = ''
        text_height = bar_height + 2
        ax1.text((x1 + x2) * 0.5, text_height, sig_symbol, ha='center', va='bottom', c='k', fontsize=14)

    # Add significance bars
    add_significance_bar(0, 1, 4.5, 4.3, "", axes[1])
    add_significance_bar(0, 1, 4.5, 4.3, "", axes[3])
    add_significance_bar(0, 1, 4.5, 4.3, "", axes[5])
    add_significance_bar(0, 1, 4.5, 4.3, "", axes[7])
# Read the CSV file skipping the first row
data = pd.read_csv('Updated_Apendix_A_Navigation_Responses.csv')

# Assuming the column indices
y_column_index = 6
group_column_index = 10
approach_index = 7
metaphor_index = 8
gender_index = 2
# condition_column_index = 2

# Filtering the data
filtered_data = data

# Extracting the required columns
y_data = filtered_data.iloc[:, y_column_index]
layout_data = filtered_data.iloc[:, group_column_index]
approach_data = filtered_data.iloc[:, approach_index]
metaphor_data = filtered_data.iloc[:, metaphor_index]

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
fig = plt.figure(figsize=(30, 8))

subfigs = fig.subfigures(1, 3, width_ratios=(1, 1, 1), wspace=-0.1)

main_effects_1(subfigs[0])
main_effects_2(subfigs[1])
main_effects_3(subfigs[2])
#
# # Set a custom color palette for the bars
# custom_palette = ['lightgreen', 'forestgreen']
# sns.set_palette(custom_palette)
#
# # Create box plots using Seaborn
# ax = sns.barplot(ax=axess, x=layout_data, y=y_data, ci=None, palette=['skyblue', 'royalblue'],
#                  order=['horizontal', 'vertical'])
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
plt.savefig("prelim_figures/appendixA_all.png")
