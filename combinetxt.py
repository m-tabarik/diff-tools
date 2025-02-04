import os

# Get the current working directory
current_directory = os.getcwd()
output_file = 'all.txt'

with open(output_file, 'w') as outfile:
    for filename in os.listdir(current_directory):
        if filename.endswith('.txt'):
            with open(os.path.join(current_directory, filename), 'r') as infile:
                outfile.write(infile.read() + '\n')
   
