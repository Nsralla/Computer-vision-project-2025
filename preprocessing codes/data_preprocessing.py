import os
import cv2
import numpy as np
from keras_preprocessing.image import ImageDataGenerator
from pathlib import Path

# Paths
input_folder = 'isolated_words_per_user'
output_folder = 'processed_images'

# Create output folder if not exists
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Data Augmentation Configuration
datagen = ImageDataGenerator(
    rotation_range=22,  # Rotation within ±10 degrees
    width_shift_range=0.1,  # Horizontal shift within 10% of the width
    height_shift_range=0.1,  # Vertical shift within 10% of the height
    zoom_range=[0.9, 1.2],  # Slight zoom-in to avoid clipping
    brightness_range=[0.2, 1.4],  # Illumination adjustment
    fill_mode='nearest'  # Fill empty pixels with nearest values
)

# Add noise injection functions
def add_gaussian_noise(image, mean=0, stddev=10):
    """Adds Gaussian noise to the image."""
    noise = np.random.normal(mean, stddev, image.shape)
    noisy_image = image + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

def add_salt_and_pepper_noise(image, prob=0.01):
    """Adds salt-and-pepper noise to the image."""
    noisy_image = image.copy()
    num_salt = int(prob * image.size * 0.5)
    num_pepper = int(prob * image.size * 0.5)

    # Add salt noise (white pixels)
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255

    # Add pepper noise (black pixels)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

# Process each user's folder
for user_folder in os.listdir(input_folder):
    user_input_path = os.path.join(input_folder, user_folder)
    user_output_path = os.path.join(output_folder, user_folder)

    # Skip non-directory files
    if not os.path.isdir(user_input_path):
        continue

    # Create output directory for user
    Path(user_output_path).mkdir(parents=True, exist_ok=True)

    # Process each image in the folder
    for image_name in os.listdir(user_input_path):
        image_path = os.path.join(user_input_path, image_name)
        
        # Load and convert the image to grayscale
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Skipping non-image file: {image_path}")
            continue

        # Expand dimensions to simulate a batch for data augmentation
        img = np.expand_dims(img, axis=-1)
        img = np.expand_dims(img, axis=0)

        # Apply data augmentation
        aug_iter = datagen.flow(img, batch_size=1)
        for i in range(4):  # Save 3 geometrically transformed versions
            aug_img = next(aug_iter)[0].astype('uint8').squeeze()
            aug_image_name = f"{Path(image_name).stem}_geo_aug{i+1}.png"
            aug_image_path = os.path.join(user_output_path, aug_image_name)
            cv2.imwrite(aug_image_path, aug_img)

        # Apply Gaussian noise augmentation
        gaussian_noisy_img = add_gaussian_noise(img.squeeze())
        gaussian_image_name = f"{Path(image_name).stem}_gaussian.png"
        gaussian_image_path = os.path.join(user_output_path, gaussian_image_name)
        cv2.imwrite(gaussian_image_path, gaussian_noisy_img)

        # Apply salt-and-pepper noise augmentation
        sp_noisy_img = add_salt_and_pepper_noise(img.squeeze())
        sp_image_name = f"{Path(image_name).stem}_saltpepper.png"
        sp_image_path = os.path.join(user_output_path, sp_image_name)
        cv2.imwrite(sp_image_path, sp_noisy_img)

print("Processing with geometric transformations and noise injection completed.")
