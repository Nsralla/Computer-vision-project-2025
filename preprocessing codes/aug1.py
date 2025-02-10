import albumentations as A
import cv2
import os

# Define the updated augmentation pipeline without Gaussian noise
final_augmentation_pipeline = A.Compose([
    A.Rotate(limit=5, p=0.5),  # Very slight rotations
    A.ShiftScaleRotate(shift_limit=0.02, scale_limit=0.02, rotate_limit=5, p=0.7),  # Subtle shifts and rotations
    A.RandomBrightnessContrast(brightness_limit=0.05, contrast_limit=0.05, p=0.5),  # Subtle brightness/contrast changes
    A.Perspective(scale=(0.005, 0.02), p=0.3),  # Subtle perspective distortions
    A.MotionBlur(blur_limit=3, p=0.2),  # Minimal motion blur for added variety
])

# Function to apply refined augmentations for a flat folder structure
def augment_and_save_flat(input_dir, output_dir, num_augmented_per_image=5):
    """
    Applies refined augmentation to images in a flat folder and saves them to the output directory.
    
    :param input_dir: Path to the folder containing original images
    :param output_dir: Path to the folder to save augmented images
    :param num_augmented_per_image: Number of augmented versions to generate per image
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over all images in the input directory
    for file in os.listdir(input_dir):
        if file.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, file)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            # Resize images to ensure consistency
            image = cv2.resize(image, (224, 224))
            
            # Generate and save augmented images
            for i in range(num_augmented_per_image):
                augmented = final_augmentation_pipeline(image=image)['image']
                save_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}_aug_{i}.png")
                cv2.imwrite(save_path, augmented)

# Paths for augmentation
input_dir = "splits_grouped/training"  # Flat folder with training images
output_dir = "augmented_training"

augment_and_save_flat(input_dir, output_dir, num_augmented_per_image=4)
