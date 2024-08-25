import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file skipping the first row
data = pd.read_csv('Apendix B - Navigation (Responses).csv', skiprows=1)

# Specify the columns for which you want to calculate mean and standard deviation
columns_to_analyze = ['Column4', 'Column5', 'Column6', 'Column7']

# Rename columns for better compatibility with seaborn
data.columns = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8']

# Melt the DataFrame to create a format suitable for seaborn
melted_data = pd.melt(data, id_vars='Column3', value_vars=columns_to_analyze,
                      var_name="Columns", value_name="Values")

# Plotting the bar chart using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Column3', y="Values", hue="Columns", data=melted_data, ci='sd', capsize=0.1)

# Customize the plot
plt.title('Mean and Standard Deviation for Columns 4, 5, 6, 7 grouped by Column 3')
plt.xlabel('Groups (Column 3 values)')
plt.ylabel('Values')
plt.legend(title='Columns', loc='upper right')
plt.show()
