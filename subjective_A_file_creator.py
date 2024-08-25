import csv

def process_csv_in_place(file_path):
    rows = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row

        # Find column indices
        col_4_index = header.index('Task Number:')
        col_8_index = header.index('Approach')
        col_9_index = header.index('Metaphor')
        col_10_index = header.index('Intensity')
        col_11_index = header.index('Layout')

        for row in reader:
            # Assuming row index starts from 0, if the 4th column is 0
            if row[col_4_index] == '0':
                # Modify columns 8 to 11 as specified
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'push'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '1':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'push'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '2':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'push'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '3':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'push'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '4':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'push'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '5':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'push'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '6':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'push'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '7':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'push'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '8':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '9':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '10':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '11':
                row[col_8_index] = 'two-tactor'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '12':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '13':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'linear'
                row[col_11_index] = 'horizontal'
            elif row[col_4_index] == '14':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'vertical'
            elif row[col_4_index] == '15':
                row[col_8_index] = 'worst-axis'
                row[col_9_index] = 'pull'
                row[col_10_index] = 'zone'
                row[col_11_index] = 'horizontal'


            rows.append(row)

    # Write the modified rows back to the file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

# Example usage:
file_path = 'Apendix A - Navigation (Responses).csv'
process_csv_in_place(file_path)
