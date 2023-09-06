# Define the input and output file names
input_file_name = 'file_to_read.txt'
output_file_name = 'result.txt'

# Read the content of the input file
with open(input_file_name, 'r') as input_file:
    content = input_file.read()

# Calculate the total times the word "terrible" appears
total_terrible_count = content.lower().count("terrible")

# Split the content into words
words = content.split()

# Initialize a counter for tracking "terrible" occurrences
terrible_counter = 1

# Iterate through the words and replace "terrible" accordingly
for i in range(len(words)):
    if "terrible" in words[i].lower():
        if terrible_counter % 2 == 0:
            words[i] = "pathetic"
        else:
            words[i] = "marvellous"
        terrible_counter += 1

# Reconstruct the modified content
modified_content = ' '.join(words)

# Write the modified content to the output file
with open(output_file_name, 'w') as output_file:
    output_file.write(modified_content)

# Display the total count of "terrible"
print("Total 'terrible' count:", total_terrible_count)
