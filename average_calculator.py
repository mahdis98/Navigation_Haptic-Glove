import pandas as pd

def calculate_average_by_group(csv_file_path):
    # Read the CSV file, skipping the first line
    df = pd.read_csv(csv_file_path, skiprows=[0])

    # Group by the values in the third column and calculate the average of the 7th column for each group
    grouped_data = df.groupby(df.iloc[:, 12])[df.columns[5]].mean()
    # grouped_data_sd = df.groupby(df.iloc[:, 12])[df.columns[9]].std()

    return grouped_data

# Example usage
csv_file_path = 'zone_calculation/total.csv'  # Replace with the path to your CSV file
result= calculate_average_by_group(csv_file_path)
print(result)
