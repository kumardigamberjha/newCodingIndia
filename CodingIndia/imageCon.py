from PIL import Image

# Open the JPG image
jpg_image = Image.open('static/images/webd.jpg')

# Specify the output filename with the .webp extension
output_filename = 'output.webp'

# Convert and save the image in WebP format
jpg_image.save(output_filename, 'webp', lossless=True)

print(f'Image converted and saved as {output_filename}')