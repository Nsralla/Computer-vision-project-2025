import os
import random
import shutil
from pathlib import Path

# Define paths
input_folder = 'isolated_words_per_user'  # Input folder containing all writer folders
training_folder = r'isolated_words_per_user/training_data'  # Destination for training data
testing_folder = r'isolated_words_per_user/testing_data'  # Destination for testing data

# Create output directories if they don't exist
Path(training_folder).mkdir(parents=True, exist_ok=True)
Path(testing_folder).mkdir(parents=True, exist_ok=True)

# Set split ratio
train_ratio = 0.8  # 80% for training
test_ratio = 0.2   # 20% for testing

# Function to split data
def split_data():
    """
    Splits the data in 'processed_images' into training and testing sets.
    Moves 80% of the data to 'training_data' and 20% to 'testing_data',
    without preserving writer-based subfolders.
    """
    for writer_folder in os.listdir(input_folder):
        writer_path = os.path.join(input_folder, writer_folder)

        # Ensure it's a directory
        if not os.path.isdir(writer_path):
            continue

        # Get all image files in the writer's folder
        image_files = [f for f in os.listdir(writer_path) if f.endswith(('png', 'jpg', 'jpeg'))]

        # Group images by unique word (e.g., 'abjadiyah')
        word_groups = {}
        for img_file in image_files:
            # Extract the word (e.g., 'abjadiyah' is the second part of the filename)
            parts = img_file.split('_')
            if len(parts) > 1:
                word = parts[1]  # Second part is the word
                word_groups.setdefault(word, []).append(img_file)

        # Split each word group into training and testing
        for word, images in word_groups.items():
            # Shuffle images to randomize selection
            random.shuffle(images)

            # Calculate split sizes
            train_size = int(len(images) * train_ratio)

            # Split images
            train_images = images[:train_size]
            test_images = images[train_size:]

            # Move images to the respective directories
            for img_file in train_images:
                src = os.path.join(writer_path, img_file)
                dst = os.path.join(training_folder, f"{writer_folder}_{img_file}")
                shutil.move(src, dst)

            for img_file in test_images:
                src = os.path.join(writer_path, img_file)
                dst = os.path.join(testing_folder, f"{writer_folder}_{img_file}")
                shutil.move(src, dst)

    print("Data splitting completed. All training and testing images are consolidated.")

# Call the function
split_data()
