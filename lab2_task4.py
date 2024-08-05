import os

# Define the directories containing the frames
i_frames_dir = '/Users/yuthishkumar/Desktop/python project/I_frames'
p_frames_dir = '/Users/yuthishkumar/Desktop/python project/P_frames'
b_frames_dir = '/Users/yuthishkumar/Desktop/python project/B_frames'

# Function to calculate average file size and total directory size
def calculate_file_sizes(dir_path):
    frame_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.png')]
    if not frame_files:
        raise FileNotFoundError(f"No frames found in directory: {dir_path}")
    
    total_size = 0
    for frame_file in frame_files:
        total_size += os.path.getsize(frame_file)
    
    average_size = total_size / len(frame_files)
    return average_size, total_size

# Calculate average and total file sizes
average_size_i, total_size_i = calculate_file_sizes(i_frames_dir)
average_size_p, total_size_p = calculate_file_sizes(p_frames_dir)
average_size_b, total_size_b = calculate_file_sizes(b_frames_dir)

# Print average file sizes and total directory sizes
print(f"Average file size of I-frames: {average_size_i:.2f} bytes")
print(f"Total size of I-frames directory: {total_size_i / 1024:.2f} KB")

print(f"Average file size of P-frames: {average_size_p:.2f} bytes")
print(f"Total size of P-frames directory: {total_size_p / 1024:.2f} KB")

print(f"Average file size of B-frames: {average_size_b:.2f} bytes")
print(f"Total size of B-frames directory: {total_size_b / 1024:.2f} KB")
