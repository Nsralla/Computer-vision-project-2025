import os
from PIL import Image

def find_largest_image_width(folder_path):
    max_width = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(folder_path, filename)
            # print it's name
           
            with Image.open(image_path) as img:
                width, height = img.size
                if width > max_width:
                    print(image_path)
                    max_width = width
    return max_width

# Example usage
folder_path = r'Not augmented\training_data'
largest_width = find_largest_image_width(folder_path)
print(f'The largest image width is: {largest_width}')