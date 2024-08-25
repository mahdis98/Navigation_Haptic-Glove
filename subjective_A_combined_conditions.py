import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual file name
file_path = 'Updated_Apendix_A_Navigation_Responses.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Specify the column numbers for grouping and box plot
group_column_10th = 11  # 0-indexed, represents the 10th column
# group_column_3rd = 2   # 0-indexed, represents the 3rd column
boxplot_column = 4     # 0-indexed, represents the column for box plot

# Set the style and color palette for Seaborn
sns.set(style="whitegrid")
palette = sns.color_palette("husl", n_colors=len(df.iloc[:, group_column_10th].unique()))

# Create a box plot using Seaborn
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed
sns.boxplot(x=df.columns[group_column_10th], y=df.columns[boxplot_column],
            data=df, palette=palette, showfliers=False, width=0.8)

# Set plot labels and title
plt.xlabel(df.columns[group_column_10th])
plt.ylabel(df.columns[boxplot_column])
plt.title(f'Box Plots Grouped by {df.columns[group_column_10th]}')

# Show the plot
plt.legend( loc='upper right', bbox_to_anchor=(1.2, 1))
plt.show()
