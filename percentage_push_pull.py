import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual file name
file_path = 'Apendix B - Navigation (Responses).csv'

# Read the CSV file
data = pd.read_csv(file_path)

# Specify the column numbers for analysis (10th, 11th, and 12th columns)
columns_to_analyze = [13, 15, 17]  # 0-indexed

# Create subplots with shared y-axis and no horizontal spacing
fig, axes = plt.subplots(1, len(columns_to_analyze), figsize=(12, 5), sharey=True)

# Define colors for the first and second bars
colors = ['#1f78b4', '#ff7f00']  # Change these colors as needed

# Iterate through each column and plot the bar chart
for i, column_index in enumerate(columns_to_analyze):
    # Calculate the percentage of each unique value in the specified column
    percentage_values = data.iloc[:, column_index].value_counts(normalize=True) * 100

    # Plot the first bar in the first color and the second bar in the second color
    axes[i].bar(percentage_values.index[:2], percentage_values.values[:2], color=colors, align='center', linewidth=0, width=0.5)

    # Set labels and title for each subplot
    axes[i].set_xlabel(data.columns[column_index])

    # Hide y-axis ticks and labels for the second and third subplots
    if i > 0:
        axes[i].tick_params(axis='y', which='both', left=False, labelleft=False)
        axes[i].set_ylabel('')  # Remove y-axis label

    # Remove the y-axis spine (vertical frame) for the second and third subplots
    if i > 0:
        axes[i].spines['left'].set_visible(False)

# Set a common y-axis label for the first subplot
axes[0].set_ylabel('Preference Percentage (%)')

# Adjust layout to remove horizontal spacing
plt.subplots_adjust(wspace=0)

# Show the plot
plt.show()
