import os

# Define the directories containing the frames
i_frames_dir = '/Users/yuthishkumar/Desktop/python project/I_frames'
p_frames_dir = '/Users/yuthishkumar/Desktop/python project/P_frames'
b_frames_dir = '/Users/yuthishkumar/Desktop/python project/B_frames'

# Function to calculate average file size in a directory
def calculate_average_file_size(dir_path):
    frame_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.png')]
    if not frame_files:
        raise FileNotFoundError(f"No frames found in directory: {dir_path}")
    
    total_size = 0
    for frame_file in frame_files:
        total_size += os.path.getsize(frame_file)
    
    average_size = total_size / len(frame_files)
    return average_size

# Calculate average file sizes
average_size_i = calculate_average_file_size(i_frames_dir)
average_size_p = calculate_average_file_size(p_frames_dir)
average_size_b = calculate_average_file_size(b_frames_dir)

# Print average file sizes
print(f"Average file size of I-frames: {average_size_i:.2f} bytes")
print(f"Average file size of P-frames: {average_size_p:.2f} bytes")
print(f"Average file size of B-frames: {average_size_b:.2f} bytes")


