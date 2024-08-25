import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})  # Set font size to 14
# Read CSV file
df = pd.read_csv('appendix_b_gender.csv')  # Replace 'your_file.csv' with the path to your CSV file

# Melt the DataFrame to have a column for the variable being measured and one for its value
melted_df = df.melt(id_vars=[df.columns[1]], value_vars=df.columns[2:7], var_name='Column', value_name='Value')

# Set custom colors
custom_palette = {'F': 'red', 'M': 'blue'}

# Plot using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=melted_df, x='Column', y='Value', hue=df.columns[1], ci='sd', palette=custom_palette,
            errwidth=1, capsize=0.2, linewidth=1, width=0.7)  # Adjust width of bars to increase horizontal distance
plt.ylabel('7-Point Likert-Scale')
plt.xlabel('')
plt.legend(title=df.columns[1])
plt.tight_layout()  # Add some space between bars
plt.ylim(1, 7.9)  # Limit y-axis to 7.5
plt.show()
