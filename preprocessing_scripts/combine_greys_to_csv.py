import os
import numpy as np
import pandas as pd
from PIL import Image

os.chdir(r"C:/Users/louja/Desktop/OwnProjects/Face_detection/")

def two_folders_to_csv(folder0, folder1, output_csv):
    """
    Takes 64x64 grayscale JPG images from two folders and outputs a single CSV.
    All images in folder0 get label 0, all images in folder1 get label 1.
    Label column is the first column, no filename is included.
    """
    data = []

    for label, folder in enumerate([folder0, folder1]):
        for fname in os.listdir(folder):
            if fname.lower().endswith(".jpg"):
                fpath = os.path.join(folder, fname)

                # Open image, force grayscale, resize 64x64
                img = Image.open(fpath).convert("L").resize((64, 64))
                arr = np.array(img).flatten()  # (4096,)

                # Put label at start
                row = [label] + arr.tolist()
                data.append(row)

    # Build dataframe
    col_names = ["label"] + [f"pixel_{i}" for i in range(64*64)]
    df = pd.DataFrame(data, columns=col_names)

    # Save CSV
    df.to_csv(output_csv, index=False)
    print(f"CSV saved to {output_csv}")

# Example usage:
# two_folders_to_csv("cats_folder", "dogs_folder", "cats_vs_dogs.csv")
two_folders_to_csv("Indoor67_chosen/Images_selected_mixed_grey", "kaggle-genki4k/faces_grey_close", "face_detection.csv")