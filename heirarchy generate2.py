import os

# Specify the root directory for the hierarchy
root_dir = 'arithmetic operation'

# Open a text file to write the hierarchy
# replace logical with arithmetic for  hierarchy of arithmetic
with open('logical operation/folder_hierarchy.txt', 'w') as f:
    # Walk through the directory hierarchy
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Write the current directory path to the file
        f.write(f"Directory: {dirpath}\n")

        # Write the subdirectories to the file
        if dirnames:
            f.write("Subdirectories:\n")
            for dirname in dirnames:
                f.write(f"\t- {dirname}\n")

        # Write the filenames to the file
        if filenames:
            f.write("Files:\n")
            for filename in filenames:
                f.write(f"\t- {filename}\n")

        # Add a newline for readability
        f.write('\n')
