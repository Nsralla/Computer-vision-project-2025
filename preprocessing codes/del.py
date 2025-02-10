import os
import re

# Specify the path to your testing folder
testing_folder = r"Augmented\testing_data_resized"

# Define the regular expression for matching filenames ending with '_aug'
pattern = re.compile(r".*_aug\d+\.(png|jpg|jpeg)$")  # Adjust extensions as needed

# Iterate through all files in the folder
for file_name in os.listdir(testing_folder):
    if pattern.match(file_name):  # Check if the file matches the pattern
        file_path = os.path.join(testing_folder, file_name)
        try:
            os.remove(file_path)  # Delete the file
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

print("Cleanup completed.")
