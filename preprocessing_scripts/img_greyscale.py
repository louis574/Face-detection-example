import os
import cv2

# Folders

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder containing the script
print(script_dir)
input_folder = os.path.join(script_dir, "Indoor67_chosen/Images_selected_mixed")
output_folder = os.path.join(script_dir, "Indoor67_chosen/Images_selected_mixed_grey")     # Where processed images will go
target_size = (64, 64)                 # Desired output size

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg"):  # only process .jpg files
        img_path = os.path.join(input_folder, filename)
        
        # Read image
        img = cv2.imread(img_path)
        if img is None:
            print(f"Failed to read {filename}, skipping...")
            continue
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Resize to target size
        resized = cv2.resize(gray, target_size, interpolation=cv2.INTER_AREA)
        
        # Save processed image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resized)

        print(f"Processed {filename} -> {output_path}")