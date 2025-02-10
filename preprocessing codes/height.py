import os
from PIL import Image

def find_largest_image_height(folder_path):
    max_height = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                width, height = img.size
                if height > max_height:
                    max_height = height
    return max_height

# Example usage
folder_path = r'Not augmented\testing_data'
largest_height = find_largest_image_height(folder_path)
print(f'The largest image height is: {largest_height}')