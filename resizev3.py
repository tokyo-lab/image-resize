from PIL import Image


def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    aspect_ratio = height/width
    new_height = int(size * aspect_ratio)

    # Resize the image with a high-quality downsampling filter
    resized_image = original_image.resize((size, new_height), Image.LANCZOS)

    # Save the resized image
    resized_image.save(output_image_path)


# Example usage:
resize_image('images/IMG-1284.jpg', 'images/me-resized.jpg',
             800)  # Resizes to 192px width
