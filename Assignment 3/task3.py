import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 1. Load the image into a NumPy array
image = np.array(Image.open("sample.jpg").convert("RGB"))

# 2. Extract individual 2D channel intensity grids using Axis 2 slicing
red_channel = image[:, :, 0]
green_channel = image[:, :, 1]
blue_channel = image[:, :, 2]

# 3. Construct 3D isolated color arrays (one active channel, others set to 0)
red_only = np.zeros_like(image)
green_only = np.zeros_like(image)
blue_only = np.zeros_like(image)

red_only[:, :, 0] = red_channel
green_only[:, :, 1] = green_channel
blue_only[:, :, 2] = blue_channel

# Print summary text before plt.show() so it displays while the window renders
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape : {image.shape}")
print(f"Red Channel 2D Shape : {red_channel.shape} | Mean Intensity: {red_channel.mean():.2f}")
print(f"Green Channel 2D Shape: {green_channel.shape} | Mean Intensity: {green_channel.mean():.2f}")
print(f"Blue Channel 2D Shape : {blue_channel.shape} | Mean Intensity: {blue_channel.mean():.2f}")
print("Display Window : Matplotlib 2x3 Subplot Grid Rendered.")

# 4. Display the output in a 2 x 3 subplot layout
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Top Row: Single-channel 3D color images
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only")

# Bottom Row: 2D Grayscale intensity maps
axes[1, 0].imshow(red_channel, cmap="gray")
axes[1, 0].set_title("Red Intensity")

axes[1, 1].imshow(green_channel, cmap="gray")
axes[1, 1].set_title("Green Intensity")

axes[1, 2].imshow(blue_channel, cmap="gray")
axes[1, 2].set_title("Blue Intensity")

# Hide axis markings for clean rendering
for ax in axes.flat:
    ax.axis("off")

plt.tight_layout()

# Save image file to disk for LaTeX PDF report inclusion
plt.savefig("outputs/task3_subplots.png", bbox_inches="tight")

plt.show()