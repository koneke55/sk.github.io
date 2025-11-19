from PIL import Image

# Open the image
img = Image.open('assets/img/capture.png')

# Get image dimensions
width, height = img.size
print(f"Original size: {width}x{height}")

# Crop to remove text - adjust these values based on where the text is
# This crops from top-left (0, 0) to bottom-right, removing bottom portion where text might be
# Adjust the crop box coordinates as needed
# Format: (left, top, right, bottom)

# Example: Crop to keep top 80% of the image (remove bottom 20% where text might be)
crop_top = 0
crop_left = 0
crop_right = width
crop_bottom = int(height * 0.8)  # Keep top 80%

# Or crop from center - adjust these values
# crop_left = int(width * 0.1)  # Remove 10% from left
# crop_top = int(height * 0.1)   # Remove 10% from top
# crop_right = int(width * 0.9)  # Remove 10% from right
# crop_bottom = int(height * 0.9)  # Remove 10% from bottom

# Crop the image
cropped_img = img.crop((crop_left, crop_top, crop_right, crop_bottom))

# Save the cropped image
cropped_img.save('assets/img/capture.png', 'PNG')
print(f"Cropped size: {cropped_img.size[0]}x{cropped_img.size[1]}")
print("Image cropped successfully!")

