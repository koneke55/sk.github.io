import numpy as np
from PIL import Image, ImageDraw

# Create a 200x200 image with transparent background
# Optimized for navbar visibility
width, height = 200, 200
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Draw X and Y axes - enhanced for visibility
axis_color = (0, 0, 0, 255)  # Solid black for better visibility
axis_thickness = 3  # Thicker for navbar visibility

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

# DFT (Discrete Fourier Transform) - Square wave with random variations
# Optimized for left navbar logo - clear and visible
sample_rate = 30  # More sampling points for smoother square wave
discrete_points = np.linspace(25, width - 25, sample_rate)

# Generate square wave with random variations
np.random.seed(42)  # For reproducibility, but still random-looking
waveform_discrete = []

# Base square wave parameters
base_period = len(discrete_points) / 4  # 4 cycles
base_amplitude = 0.8

for i, x in enumerate(discrete_points):
    # Calculate position in square wave cycle
    cycle_pos = (i / base_period) % 1.0
    
    # Square wave: high for first half, low for second half
    if cycle_pos < 0.5:
        value = base_amplitude
    else:
        value = -base_amplitude
    
    # Add random variations to amplitude and timing
    random_amplitude = np.random.uniform(-0.15, 0.15)
    random_phase = np.random.uniform(-0.05, 0.05)
    
    # Apply randomness
    adjusted_cycle_pos = (cycle_pos + random_phase) % 1.0
    if adjusted_cycle_pos < 0.5:
        value = base_amplitude + random_amplitude
    else:
        value = -base_amplitude + random_amplitude
    
    # Add some random spikes for more variation
    if np.random.random() < 0.1:  # 10% chance of spike
        value += np.random.uniform(-0.2, 0.2)
    
    waveform_discrete.append(value)

waveform_discrete = np.array(waveform_discrete)

# Normalize and scale to fit within axes
waveform_discrete = (waveform_discrete - waveform_discrete.min()) / (waveform_discrete.max() - waveform_discrete.min())
waveform_range = (x_axis_y - 25) - 25  # Space between axes
waveform_discrete = waveform_discrete * waveform_range + 25

# Draw square wave with discrete points
points = [(int(discrete_points[i]), int(waveform_discrete[i])) for i in range(len(discrete_points))]

# Draw square wave pattern (horizontal and vertical lines) - enhanced for navbar
waveform_color = (0, 0, 0, 255)  # Solid black for maximum visibility
waveform_thickness = 4  # Thicker lines for navbar visibility

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    
    # Draw horizontal line (square wave characteristic) - thicker for visibility
    mid_x = (x1 + x2) // 2
    draw.line([(x1, y1), (mid_x, y1)], fill=waveform_color, width=waveform_thickness)
    draw.line([(mid_x, y1), (mid_x, y2)], fill=waveform_color, width=waveform_thickness)
    draw.line([(mid_x, y2), (x2, y2)], fill=waveform_color, width=waveform_thickness)
    
    # Draw circles at discrete sample points - larger for visibility
    circle_radius = 4
    draw.ellipse([x1-circle_radius, y1-circle_radius, x1+circle_radius, y1+circle_radius], 
                 fill=waveform_color, outline=waveform_color, width=2)
    if i == len(points) - 2:  # Draw last point
        draw.ellipse([x2-circle_radius, y2-circle_radius, x2+circle_radius, y2+circle_radius], 
                     fill=waveform_color, outline=waveform_color, width=2)

# Draw discrete frequency spectrum bars on the right (DFT characteristic - discrete bins)
# Enhanced for navbar visibility
bar_x_start = width - 40
bar_x_end = width - 18
bar_positions = [45, 65, 85, 105, 125, 145, 165]
bar_heights = [20, 32, 24, 17, 12, 8, 5]  # Slightly taller for visibility
bar_color = (0, 0, 0, 255)  # Solid black

for pos, h in zip(bar_positions, bar_heights):
    # Draw discrete bars with gaps between them - thicker for visibility
    draw.rectangle([bar_x_start, pos, bar_x_end, pos+h], fill=bar_color, outline=bar_color, width=1)
    # Add small gaps to emphasize discrete nature
    if pos + h < x_axis_y - 5:
        draw.rectangle([bar_x_start, pos+h, bar_x_end, pos+h+2], fill=(255, 255, 255, 0))

# Save the image
img.save('assets/img/dft-logo.png', 'PNG')
print("DFT logo generated successfully with X and Y axes!")
