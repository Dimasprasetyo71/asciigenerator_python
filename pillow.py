import urllib.request
from PIL import Image

url = input("Enter the URL of the image: ")
image = Image.open(urllib.request.urlopen(url))
image.show()
    

# Save the image
image.save("image.jpg")

# Resize the image
width, height = image.size
new_width = 800
new_height = int(new_width * (height / width))
resized_image = image.resize((new_width, new_height))
resized_image.save("resized_image.jpg")

# Rotate the image
rotated_image = image.rotate(45)
rotated_image.save("rotated_image.jpg")

# Crop the image
cropped_image = image.crop((100, 100, 300, 300))
cropped_image.save("cropped_image.jpg")

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.save("grayscale_image.jpg")

# Convert the image to black and white
black_and_white_image = image.convert("1")
black_and_white_image.save("black_and_white_image.jpg")

# 