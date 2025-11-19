import numpy as np
from PIL import Image, ImageDraw

# Create a 200x200 image with transparent background
width, height = 200, 200
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Create Fast Fourier Series waveform
t = np.linspace(0, 4*np.pi, width)
# Sum of multiple sine waves (Fourier series)
waveform = (np.sin(t) + 
            0.6 * np.sin(2*t) + 
            0.4 * np.sin(3*t) + 
            0.3 * np.sin(4*t) + 
            0.2 * np.sin(5*t))

# Normalize to fit in the image
waveform = (waveform - waveform.min()) / (waveform.max() - waveform.min())
waveform = waveform * (height - 40) + 20  # Scale with padding

# Draw the waveform
points = [(int(x), int(waveform[i])) for i, x in enumerate(np.linspace(10, width-10, len(waveform)))]
for i in range(len(points) - 1):
    draw.line([points[i], points[i+1]], fill=(0, 0, 0, 255), width=3)

# Draw frequency spectrum bars on the right
bar_positions = [40, 60, 80, 100, 120]
bar_heights = [25, 40, 30, 18, 12]
for pos, h in zip(bar_positions, bar_heights):
    draw.rectangle([width-30, pos, width-10, pos+h], fill=(0, 0, 0, 180))

# Save the image
img.save('assets/img/fft-logo.png', 'PNG')
print("FFT logo generated successfully!")
