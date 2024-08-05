import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error

def calculate_metrics(video1_path, video2_path, num_frames=100):
    cap1 = cv2.VideoCapture(video1_path)
    cap2 = cv2.VideoCapture(video2_path)

    psnr_values = []
    ssim_values = []
    mse_values = []

    for _ in range(num_frames):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break

        # Convert frames to grayscale for SSIM
        frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        # Calculate PSNR
        psnr_value = psnr(frame1, frame2)
        psnr_values.append(psnr_value)

        # Calculate SSIM
        ssim_value = ssim(frame1_gray, frame2_gray)
        ssim_values.append(ssim_value)

        # Calculate MSE
        mse_value = mean_squared_error(frame1, frame2)
        mse_values.append(mse_value)

    cap1.release()
    cap2.release()

    avg_psnr = np.mean(psnr_values)
    avg_ssim = np.mean(ssim_values)
    avg_mse = np.mean(mse_values)

    return avg_psnr, avg_ssim, avg_mse

original_video = '/Users/yuthishkumar/Desktop/python project/test_video.mp4'
compressed_video = '/Users/yuthishkumar/Desktop/python project/compressed_video.mp4'

avg_psnr_value, avg_ssim_value, avg_mse_value = calculate_metrics(original_video, compressed_video)

print(f"Average PSNR: {avg_psnr_value:.2f} dB")
print(f"Average SSIM: {avg_ssim_value:.4f}")
print(f"Average MSE: {avg_mse_value:.4f}")
