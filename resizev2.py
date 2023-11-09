from PIL import Image
import os


def resize_and_reduce(image_path, output_path, new_size, quality):
    # Open an image file
    with Image.open(image_path) as img:
        # Resize the image
        resized_img = img.resize(new_size)

        # Save the resized image with reduced quality
        resized_img.save(output_path, quality=quality)

        # Get the file size of the original and resized images
        original_size = os.path.getsize(image_path)
        resized_size = os.path.getsize(output_path)

        # Calculate the reduction in file size
        size_reduction = original_size - resized_size

        # Print out the file sizes for comparison
        print(f"Original file size: {original_size / 1024:.2f} KB")
        print(f"Resized file size: {resized_size / 1024:.2f} KB")
        print(f"Reduction in file size: {size_reduction / 1024:.2f} KB")

# Example usage:


# Path to the original image
image_path = 'images/IMG-1284.jpg'
# Path where the resized image will be saved
output_path = 'images/IMG-1286-resized.jpg'
# New size for the image (width, height)
new_size = (192, 192)
# Quality setting for saving the image (1-95)
quality = 85

# Resize and reduce the image
resize_and_reduce(image_path, output_path, new_size, quality)
