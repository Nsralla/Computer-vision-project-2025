import os
import pandas as pd
import shutil

# Define paths
TRAIN_CSV = "training_resized.csv"
TRAIN_FOLDER = "Not augmented/training_data_resized"
VALIDATION_CSV = "validation_resized.csv"
VALIDATION_FOLDER = "Not augmented/validation_data_resized"

# Number of validation samples per word per user
VALIDATION_SAMPLES_PER_GROUP = 2

# Load the training CSV
df = pd.read_csv(TRAIN_CSV)

# Extract word information from file names
df['Word'] = df['File Name'].apply(lambda x: x.split('_')[2])

# Group by User ID and Word
grouped = df.groupby(['User ID', 'Word'])

# Create a list to store validation entries
validation_entries = []

# Iterate over each group and select samples for validation
for (user_id, word), group in grouped:
    # Select the first N samples for validation
    validation_samples = group.head(VALIDATION_SAMPLES_PER_GROUP)
    validation_entries.append(validation_samples)

# Concatenate all selected validation entries into a DataFrame
validation_df = pd.concat(validation_entries)

# Remove selected entries from the training DataFrame
remaining_training_df = df.drop(validation_df.index)

# Create directories if not exist
os.makedirs(VALIDATION_FOLDER, exist_ok=True)

# Move selected files to the validation directory
for _, row in validation_df.iterrows():
    src_path = os.path.join(TRAIN_FOLDER, row['File Name'])
    dst_path = os.path.join(VALIDATION_FOLDER, row['File Name'])
    shutil.move(src_path, dst_path)

# Save updated CSV files
remaining_training_df.to_csv(TRAIN_CSV, index=False)
validation_df.to_csv(VALIDATION_CSV, index=False)

print(f"Validation set created with {len(validation_df)} samples.")
print(f"Training set updated with {len(remaining_training_df)} samples.")
