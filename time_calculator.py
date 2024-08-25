# Open the text file in read mode
file_path = 'Outputs/P23_H/P23_H_horizontal_12-13-23_16-16-09.txt'  # Replace 'your_file.txt' with your file path
with open(file_path, 'r') as file:
    lines = file.readlines()  # Read all lines into a list
    count = 0
# Iterate through each line in the file
for i in range(len(lines)):
    line = lines[i].strip()  # Remove leading/trailing whitespaces

    # Check if the line starts with "Time"
    if line.startswith("Time"):
        # Split the line by space to extract the number (assuming the number is the second element)
        words = line.split()
        if len(words) > 1:
            try:
                count += 1
                number = round(float(words[3]), 2)  # Convert the number to float (or int)
                print("Count: ", count, "Number on this line:", number)
                # print("\n")
                # Move to the next line if it exists
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # print("Next line after 'Time':", next_line)
            except ValueError:
                print("No valid number found after 'Time' on this line")
print("Counts: ", count)
