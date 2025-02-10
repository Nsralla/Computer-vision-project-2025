import os
from PIL import Image

def find_largest_image(folder_path):
    """
    Finds the largest image in terms of dimensions (width x height) in a folder.

    Args:
        folder_path (str): Path to the folder containing images.

    Returns:
        tuple: (image_name, dimensions) of the largest image.
    """
    largest_image = None
    largest_size = 0  # Initialize to 0

    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        # Skip non-image files
        if not image_name.lower().endswith(('png', 'jpg', 'jpeg')):
            continue

        try:
            # Open image to get its dimensions
            with Image.open(image_path) as img:
                width, height = img.size
                size = width * height  # Calculate the area of the image

                # Check if this image is the largest so far
                if size > largest_size:
                    largest_size = size
                    largest_image = (image_name, (width, height))
        except Exception as e:
            print(f"Error processing {image_name}: {e}")

    return largest_image

# Folder path containing images
folder_path = r'Not augmented\testing_data'

# Find and print the largest image
largest = find_largest_image(folder_path)
if largest:
    print(f"Largest image: {largest[0]} with dimensions {largest[1]}")
else:
    print("No valid images found in the folder.")
