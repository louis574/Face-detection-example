# Face-detection-example

# 📸 Custom Low-Res Face Detection Dataset

# 📖 Intro

I built this dataset as part of my “Neural Network on FPGA” project to test whether ultra-low-resolution data could still power complex deep learning tasks.

The focus on 64×64 grayscale images was intentional:

🏎️ Ultra-low resolution means very little data to compute → perfect for fast FPGA inference.

🎥 Enables high framerates, where the FPGA can process every frame in real time (outperforming software).

🧮 Puts quantisation-aware training and the FPGA hardware to the test — can they still handle complex, noisy tasks at scale?

To make the dataset genuinely usable for low-res face detection, I prioritised real-world robustness over “lab conditions.” That meant building in variation across:

😀 Expressions

👶🧓 Ages

🌍 Ethnicities

💡 Lighting

📐 Angles

🏠 Backgrounds

This way, the network would learn to detect faces themselves — not just a simple cue like a plain white background.



# ✨ Key Features

👥 Face Images from Genki4k

~4000 face images across different people

Variation in lighting, angles, backgrounds, and expressions

Originally for smile/no-smile classification so has varied expressions

🏠 Complex Background Negatives from MIT Indoor67

~4200 background images without faces

Includes offices, kitchens, bedrooms, corridors, etc.

Captures natural variation in lighting, perspective, and clutter

⚖️ Balanced Dataset

Even split: ~4000 face images vs. ~4200 non-face images (~5% difference)

Prevents bias toward always predicting “face” or “no-face” just from distribution of cases in data

Ensures model focuses on learning actual face features instead of background simplicity
