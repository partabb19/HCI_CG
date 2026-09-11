import numpy as np
import matplotlib.pyplot as plt

# Create a 300 x 400 x 3 image matrix filled with zeros
image = np.zeros((300, 400, 3), dtype=np.uint8)

# Fill the four quadrants
image[:150, :200] = [255, 0, 0]       # Top-Left: Red
image[:150, 200:] = [0, 255, 0]       # Top-Right: Green
image[150:, :200] = [0, 0, 255]       # Bottom-Left: Blue
image[150:, 200:] = [255, 255, 255]   # Bottom-Right: White

# Display matrix metrics
print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C) : {image.shape}")
print(f"Data Type : {image.dtype}")
print(f"Total Elements : {image.size:,} values")
print(f"Memory Footprint : {image.nbytes:,} bytes ({image.nbytes / 1024:.2f} KB)")

# --- ADD THESE LINES TO RENDER AND SAVE THE IMAGE ---
plt.imshow(image)
plt.axis('off')  # Hides coordinate axes ticks

# Save the image file to disk for your PDF report
plt.savefig('outputs/task2_synthetic.png', bbox_inches='tight', pad_inches=0)

# Display the window on screen
plt.show()