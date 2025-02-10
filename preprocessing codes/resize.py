from PIL import Image

def resize_gray_image(input_image_path, output_image_path, new_width, new_height):
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
input_image_path = r'Not augmented\training_data\user003_user003_abjadiyah_040.png'  # Replace with your input image path
output_image_path = 'image_resized.jpg'  # Replace with your desired output path
new_width = 224  # Specify the desired width
new_height = 224  # Specify the desired height

resize_gray_image(input_image_path, output_image_path, new_width, new_height)