import cv2
import os

# Define directories
i_frames_dir = '/Users/yuthishkumar/Desktop/python project/I_frames'
output_video_path = '/Users/yuthishkumar/Desktop/python project/reconstructed_video.mp4'

# List I-frame image files
i_frame_files = [os.path.join(i_frames_dir, f) for f in os.listdir(i_frames_dir) if f.endswith('.png')]
i_frame_files.sort()  # Ensure correct order

# Read the first frame to get video dimensions
first_frame = cv2.imread(i_frame_files[0])
height, width, _ = first_frame.shape

# Create a VideoWriter object
frame_rate = 2  # Reduced frame rate
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

# Add each I-frame to the video
for frame_file in i_frame_files:
    frame = cv2.imread(frame_file)
    video_writer.write(frame)

# Release the VideoWriter object
video_writer.release()
print(f"Reconstructed video saved at: {output_video_path}")
