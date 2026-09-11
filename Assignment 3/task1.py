import math

# Input
Wpx = int(input("Enter horizontal resolution (pixels): "))
Hpx = int(input("Enter vertical resolution (pixels): "))
Dinches = float(input("Enter physical diagonal size (inches): "))

# Total pixel count
total_pixels = Wpx * Hpx

# Simplified aspect ratio
gcd = math.gcd(Wpx, Hpx)
aspect_width = Wpx // gcd
aspect_height = Hpx // gcd

# Calculate PPI/DPI
dpi = ((Wpx ** 2 + Hpx ** 2) ** 0.5) / Dinches

# Classify display density
if dpi < 100:
    density_category = "Low Density (Standard Monitor)"
elif dpi <= 200:
    density_category = "Medium Density (HD Display)"
else:
    density_category = "High Density (Retina / Mobile)"

# Output
print("--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio : {aspect_width}:{aspect_height}")
print(f"Calculated DPI : {dpi:.2f} DPI")
print(f"Density Category : {density_category}")