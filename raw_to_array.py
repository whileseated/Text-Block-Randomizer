# Replace 'raw_text.txt' with the path to your text file
input_file_path = 'raw_text.txt'
# Replace 'output.js' with the desired output JavaScript file
output_file_path = 'output_for_script.js'

# Read lines from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Escape double quotes and backslashes, and format lines for JavaScript array
formatted_lines = ['    "' + line.strip().replace('\\', '\\\\').replace('"', '\\"') + '"' for line in lines]

# Combine the formatted lines into the final JavaScript array content
javascript_array = "const fileContent1 = [\n" + ',\n'.join(formatted_lines) + "\n];"

# Write the JavaScript array to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(javascript_array)

print(f'JavaScript array has been written to {output_file_path}')