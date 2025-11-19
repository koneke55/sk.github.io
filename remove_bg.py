from PIL import Image
import numpy as np

# Open the profile image
img = Image.open('assets/img/profile.jpg')

# Convert to RGBA if not already
if img.mode != 'RGBA':
    img = img.convert('RGBA')

# Convert to numpy array for processing
data = np.array(img)

# Get the background color (assuming it's the most common color in corners)
# Sample corners to determine background
corners = [
    data[0:10, 0:10],  # top-left
    data[0:10, -10:],  # top-right
    data[-10:, 0:10],  # bottom-left
    data[-10:, -10:]   # bottom-right
]

# Flatten corner pixels
corner_pixels = np.concatenate([c.reshape(-1, 4) for c in corners], axis=0)

# Find the most common color in corners (background)
unique_colors, counts = np.unique(corner_pixels, axis=0, return_counts=True)
background_color = unique_colors[np.argmax(counts)]

# Create a mask for background removal
# Use a threshold to handle slight variations in background color
threshold = 30  # Adjust this value if needed (0-255)

# Calculate distance from background color
color_diff = np.abs(data[:, :, :3].astype(np.int16) - background_color[:3].astype(np.int16))
distance = np.sqrt(np.sum(color_diff ** 2, axis=2))

# Create mask: pixels close to background color become transparent
mask = distance > threshold

# Apply mask to alpha channel
data[:, :, 3] = data[:, :, 3] * mask

# Convert back to Image
result = Image.fromarray(data)

# Save the result
result.save('assets/img/profile.png', 'PNG')
print("Background removed successfully! Saved as profile.png")

