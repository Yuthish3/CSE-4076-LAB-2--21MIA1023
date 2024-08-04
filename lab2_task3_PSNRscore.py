import cv2
import os
import numpy as np

# Define the directories containing the frames
i_frames_dir = '/Users/yuthishkumar/Desktop/python project/I_frames'
p_frames_dir = '/Users/yuthishkumar/Desktop/python project/P_frames'
b_frames_dir = '/Users/yuthishkumar/Desktop/python project/B_frames'

# Function to load a single frame from a directory
def load_single_frame(dir_path):
    frame_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.png')]
    if not frame_files:
        raise FileNotFoundError(f"No frames found in directory: {dir_path}")
    # Load the first frame in the directory
    return cv2.imread(frame_files[0])

# Function to compute PSNR between two images
def compute_psnr(img1, img2):
    if img1.shape != img2.shape:
        raise ValueError("Images must have the same dimensions for PSNR calculation")
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')  # Images are identical
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Load one frame from each type
i_frame = load_single_frame(i_frames_dir)
p_frame = load_single_frame(p_frames_dir)
b_frame = load_single_frame(b_frames_dir)

# Compute PSNR values
psnr_ip = compute_psnr(i_frame, p_frame)
psnr_ib = compute_psnr(i_frame, b_frame)
psnr_pb = compute_psnr(p_frame, b_frame)

# Print PSNR values
print(f"PSNR (I vs P): {psnr_ip:.2f} dB")
print(f"PSNR (I vs B): {psnr_ib:.2f} dB")
print(f"PSNR (P vs B): {psnr_pb:.2f} dB")

# 