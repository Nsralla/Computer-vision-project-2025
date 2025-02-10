import os
from PIL import Image

def resize_gray_images_in_folder(input_folder, output_folder, new_width, new_height):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)

            # Open the image
            with Image.open(input_image_path) as img:
                # Convert the image to grayscale
                gray_img = img.convert('L')
                
                # Resize the image
                resized_img = gray_img.resize((new_width, new_height))
                
                # Save the resized image
                resized_img.save(output_image_path)
                print(f'Resized image saved as: {output_image_path}')

# Example usage
input_folder = r'Not augmented\validation_data_resized'  # Replace with your input folder path
output_folder = r'Not augmented\validation_data_resized_new'  # Replace with your desired output folder path
new_width = 224  # Specify the desired width
new_height = 224  # Specify the desired height

resize_gray_images_in_folder(input_folder, output_folder, new_width, new_height)