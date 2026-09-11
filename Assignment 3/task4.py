import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the input image as a NumPy array
image = np.array(Image.open("sample.jpg").convert("RGB"))

# Step factor
N = 8

# Downsample by taking every N-th pixel
downsampled = image[::N, ::N, :]

# Re-expand the image using pixel repetition
reexpanded = np.repeat(
    np.repeat(downsampled, N, axis=0),
    N,
    axis=1
)

# Crop to original dimensions if necessary
reexpanded = reexpanded[:image.shape[0], :image.shape[1], :]

# Calculate spatial dimension reduction
height_reduction = (1 - downsampled.shape[0] / image.shape[0]) * 100

# Calculate memory reduction
memory_reduction = (1 - downsampled.nbytes / image.nbytes) * 100

# Print analysis to console
print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape : {image.shape} | Memory: {image.nbytes:,} bytes")
print(f"Downsampled Shape : {downsampled.shape} | Memory: {downsampled.nbytes:,} bytes")
print(f"Re-expanded Shape : {reexpanded.shape} | Visual: Blocky Pixelation")
print(f"Dimension Reduction: {height_reduction:.2f}% reduction per axis")
print(f"Memory Savings : {memory_reduction:.2f}% data reduction")

# --- ADDED: RENDER AND SAVE VISUAL OUTPUT ---
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Left plot: Original Image
axes[0].imshow(image)
axes[0].set_title(f"Original Image\nShape: {image.shape}")
axes[0].axis('off')

# Right plot: Re-expanded Pixelated Image
axes[1].imshow(reexpanded)
axes[1].set_title(f"Re-expanded Pixelated Image (N={N})\nShape: {reexpanded.shape}")
axes[1].axis('off')

plt.tight_layout()

# Save image file to disk for your PDF report
plt.savefig('outputs/task4_downsampled.png', bbox_inches='tight')

# Display the window
plt.show()