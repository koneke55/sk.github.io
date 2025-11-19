import numpy as np
from PIL import Image, ImageDraw

# Create a 200x200 image with transparent background
width, height = 200, 200
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# DFT (Discrete Fourier Transform) - emphasize discrete nature
# Create discrete frequency components (not continuous)
t = np.linspace(0, 4*np.pi, width)

# Discrete frequency components - stepped/sampled waveform
# Sample at discrete points to show DFT's discrete nature
sample_rate = 20  # Discrete sampling points
discrete_points = np.linspace(0, width-10, sample_rate)
discrete_t = np.linspace(0, 4*np.pi, sample_rate)

# Create discrete frequency components
waveform_discrete = (np.sin(discrete_t) + 
                     0.6 * np.sin(2*discrete_t) + 
                     0.4 * np.sin(3*discrete_t) + 
                     0.3 * np.sin(4*discrete_t) + 
                     0.2 * np.sin(5*discrete_t))

# Normalize
waveform_discrete = (waveform_discrete - waveform_discrete.min()) / (waveform_discrete.max() - waveform_discrete.min())
waveform_discrete = waveform_discrete * (height - 40) + 20

# Draw discrete points and connect them (showing discrete sampling)
points = [(int(discrete_points[i]), int(waveform_discrete[i])) for i in range(len(discrete_points))]
for i in range(len(points) - 1):
    # Draw line connecting discrete points
    draw.line([points[i], points[i+1]], fill=(0, 0, 0, 255), width=3)
    # Draw circles at discrete sample points to emphasize discreteness
    draw.ellipse([points[i][0]-3, points[i][1]-3, points[i][0]+3, points[i][1]+3], 
                 fill=(0, 0, 0, 255))

# Draw discrete frequency spectrum bars on the right (DFT characteristic - discrete bins)
bar_positions = [40, 60, 80, 100, 120, 140, 160]
bar_heights = [20, 35, 25, 18, 12, 8, 5]
for pos, h in zip(bar_positions, bar_heights):
    # Draw discrete bars with gaps between them
    draw.rectangle([width-30, pos, width-10, pos+h], fill=(0, 0, 0, 200))
    # Add small gaps to emphasize discrete nature
    if pos + h < height - 5:
        draw.rectangle([width-30, pos+h, width-10, pos+h+2], fill=(255, 255, 255, 0))

# Save the image
img.save('assets/img/dft-logo.png', 'PNG')
print("DFT logo generated successfully with discrete characteristics!")
