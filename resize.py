from PIL import Image

# Open an image file
with Image.open('images/me.png') as img:
    # The new size (width, height)
    new_size = (192, 192)

    # Resize the image
    resized_img = img.resize(new_size)

    # Save the resized image
    resized_img.save('images/me-resized.jpeg', quality=85)
