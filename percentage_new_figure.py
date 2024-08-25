import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'zone_calculation/total.csv'
df = pd.read_csv(file_path)

# Assuming the column indices for the group and response
group_column_index = 2  # Update this to the correct index for your data
response_column_index = 12  # Update this to the correct index for your data

# Create the figure
plt.figure(figsize=(10, 6))

# Generate the boxplot
sns.boxplot(x=df.columns[group_column_index], y=df.columns[response_column_index],
            data=df, showfliers=False, palette=['lightgreen', 'forestgreen'])

# Customize labels and title as needed
plt.ylabel('Percentage of Time in Critical Area (%)', fontsize=14)
plt.xlabel('Condition', fontsize=14)  # Update 'Condition' to the appropriate label
plt.title('Exploration Time by Condition', fontsize=16)

# Optional: Customize tick labels for clarity
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Remove the top and right spines for a cleaner look
sns.despine()

# Display the plot
plt.tight_layout()
plt.show()
