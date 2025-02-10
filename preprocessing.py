import os
from PIL import Image

# Paths
original_dataset_path = "isolated_words_per_user"  # Folder containing original images
preprocessed_dataset_path = "preprocessed_dataset"  # Folder to save preprocessed images
os.makedirs(preprocessed_dataset_path, exist_ok=True)

# Resize and convert settings
target_size = (64, 64)

def preprocess_images(original_path, output_path, target_size):
    for root, dirs, files in os.walk(original_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image file extensions
                input_path = os.path.join(root, file)
                output_subfolder = root.replace(original_path, output_path)
                os.makedirs(output_subfolder, exist_ok=True)
                output_file_path = os.path.join(output_subfolder, file)  # Use a different variable name

                try:
                    # Open the image
                    img = Image.open(input_path)
                    # Convert to grayscale
                    img = img.convert("L")
                    # Resize the image using LANCZOS filter
                    img = img.resize(target_size, Image.LANCZOS)
                    # Save the preprocessed image
                    img.save(output_file_path, format='PNG')  # Specify format if needed
                except Exception as e:
                    print(f"Error processing image {input_path}: {e}")

# Execute the preprocessing
preprocess_images(original_dataset_path, preprocessed_dataset_path, target_size)
print("All images have been preprocessed!")