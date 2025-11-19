import numpy as np
from PIL import Image, ImageDraw

# Create a 200x200 image with transparent background
width, height = 200, 200
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Draw X and Y axes
axis_color = (0, 0, 0, 200)  # Black with some transparency
axis_thickness = 2

# Y-axis (vertical) - left side
y_axis_x = 15
draw.line([(y_axis_x, 10), (y_axis_x, height - 10)], fill=axis_color, width=axis_thickness)
# Y-axis arrow (top)
draw.polygon([(y_axis_x, 10), (y_axis_x - 3, 17), (y_axis_x + 3, 17)], fill=axis_color)

# X-axis (horizontal) - bottom
x_axis_y = height - 15
draw.line([(10, x_axis_y), (width - 10, x_axis_y)], fill=axis_color, width=axis_thickness)
# X-axis arrow (right)
draw.polygon([(width - 10, x_axis_y), (width - 17, x_axis_y - 3), (width - 17, x_axis_y + 3)], fill=axis_color)

# Add axis labels
# Y-axis label
draw.text((y_axis_x - 12, 5), "Y", fill=axis_color)
# X-axis label
draw.text((width - 20, x_axis_y + 5), "X", fill=axis_color)

# DFT (Discrete Fourier Transform) - emphasize discrete nature
# Create discrete frequency components (not continuous)
t = np.linspace(0, 4*np.pi, width)

# Discrete frequency components - stepped/sampled waveform
# Sample at discrete points to show DFT's discrete nature
sample_rate = 20  # Discrete sampling points
discrete_points = np.linspace(20, width - 20, sample_rate)
discrete_t = np.linspace(0, 4*np.pi, sample_rate)

# Create discrete frequency components
waveform_discrete = (np.sin(discrete_t) + 
                     0.6 * np.sin(2*discrete_t) + 
                     0.4 * np.sin(3*discrete_t) + 
                     0.3 * np.sin(4*discrete_t) + 
                     0.2 * np.sin(5*discrete_t))

# Normalize and scale to fit within axes
waveform_discrete = (waveform_discrete - waveform_discrete.min()) / (waveform_discrete.max() - waveform_discrete.min())
waveform_range = (x_axis_y - 25) - 25  # Space between axes
waveform_discrete = waveform_discrete * waveform_range + 25

# Draw discrete points and connect them (showing discrete sampling)
points = [(int(discrete_points[i]), int(waveform_discrete[i])) for i in range(len(discrete_points))]
for i in range(len(points) - 1):
    # Draw line connecting discrete points
    draw.line([points[i], points[i+1]], fill=(0, 0, 0, 255), width=3)
    # Draw circles at discrete sample points to emphasize discreteness
    draw.ellipse([points[i][0]-3, points[i][1]-3, points[i][0]+3, points[i][1]+3], 
                 fill=(0, 0, 0, 255))

# Draw discrete frequency spectrum bars on the right (DFT characteristic - discrete bins)
bar_x_start = width - 35
bar_x_end = width - 15
bar_positions = [45, 65, 85, 105, 125, 145, 165]
bar_heights = [18, 30, 22, 15, 10, 7, 4]
for pos, h in zip(bar_positions, bar_heights):
    # Draw discrete bars with gaps between them
    draw.rectangle([bar_x_start, pos, bar_x_end, pos+h], fill=(0, 0, 0, 200))
    # Add small gaps to emphasize discrete nature
    if pos + h < x_axis_y - 5:
        draw.rectangle([bar_x_start, pos+h, bar_x_end, pos+h+2], fill=(255, 255, 255, 0))

# Save the image
img.save('assets/img/dft-logo.png', 'PNG')
print("DFT logo generated successfully with X and Y axes!")
