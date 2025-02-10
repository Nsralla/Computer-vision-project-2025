import pandas as pd
import os
import shutil

# Load the CSV file
csv_path = "training_resized.csv"
data = pd.read_csv(csv_path, header=None, names=["File Name", "User ID"])

# Define folder paths
training_folder = "Augmented/training_data_resized"
validation_folder = "Augmented/validation_data"

# Create the validation folder if it doesn't exist
os.makedirs(validation_folder, exist_ok=True)

# Define the validation split percentage
validation_split = 0.1

# Create empty lists to hold training and validation data
train_data = []
validation_data = []

# Group data by user_id and split
for user_id, group in data.groupby("User ID"):
    # Filter out augmented images for validation
    original_images = group[~group["File Name"].str.contains("_aug")]
    augmented_images = group[group["File Name"].str.contains("_aug")]

    # Shuffle and split original images for validation
    original_images = original_images.sample(frac=1, random_state=42)
    split_index = int(len(original_images) * validation_split)

    validation_data.append(original_images.iloc[:split_index])  # Add original images to validation
    train_data.append(original_images.iloc[split_index:])  # Add remaining original images to training
    train_data.append(augmented_images)  # Keep all augmented images in training

# Combine data into new DataFrames
validation_data = pd.concat(validation_data)
train_data = pd.concat(train_data)

# Move files to their respective folders
for _, row in validation_data.iterrows():
    file_name = row["File Name"]
    source_path = os.path.join(training_folder, file_name)
    target_path = os.path.join(validation_folder, file_name)
    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)  # Ensure target folder exists
        shutil.move(source_path, target_path)
    except Exception as e:
        print(f"Error moving {file_name}: {e}")

# Save the updated splits into new CSV files
train_data.to_csv("train_split.csv", index=False, header=False)
validation_data.to_csv("validation_split.csv", index=False, header=False)

print(f"Training set: {len(train_data)} samples")
print(f"Validation set: {len(validation_data)} samples")
print("Validation images moved successfully.")
