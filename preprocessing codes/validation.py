import os
import pandas as pd
import shutil

# Define paths
training_path = "Not augmented/training_data_resized"
validation_path = "Not augmented/validation_data_resized"
csv_file_path = "training_resized.csv"

# Define the validation split ratio (e.g., 20% of each user's data)
validation_split_ratio = 0.2

# Ensure the validation directory exists
os.makedirs(validation_path, exist_ok=True)

# Load the CSV file
data = pd.read_csv(csv_file_path)

# Group data by user ID
grouped = data.groupby('User ID')

# Process each user's data
for user_id, group in grouped:
    # Get all files for the current user
    user_files = group['File Name'].tolist()
    
    # Determine the number of files for validation
    num_validation_files = int(len(user_files) * validation_split_ratio)
    
    # Split the data: take the first `num_validation_files` for validation
    validation_files = user_files[:num_validation_files]
    
    # Move the selected files to the validation directory
    for file_name in validation_files:
        src_path = os.path.join(training_path, file_name)
        dest_path = os.path.join(validation_path, file_name)
        
        # Create subdirectories in validation folder if needed
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Move the file
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)

print("Validation set created successfully.")
