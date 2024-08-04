import cv2
import os
import numpy as np

# Define the directories containing the frames
i_frames_dir = '/Users/yuthishkumar/Desktop/python project/I_frames'
p_frames_dir = '/Users/yuthishkumar/Desktop/python project/P_frames'
b_frames_dir = '/Users/yuthishkumar/Desktop/python project/B_frames'

# Function to display up to 2 frames from a directory in one window
def display_frames(dir_path, frame_type, max_frames=2):
    print(f"Displaying up to {max_frames} {frame_type} frames in one window...")
    frame_files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.png')]
    displayed_count = 0
    images = []

    # Load up to `max_frames` images
    for frame_file in sorted(frame_files):
        if displayed_count >= max_frames:
            break
        image = cv2.imread(frame_file)
        images.append(image)
        displayed_count += 1

    # Combine images into a single window
    if len(images) == 0:
        print(f"No frames found in {dir_path}.")
        return
    
    # Resize images to be the same height
    heights = [img.shape[0] for img in images]
    widths = [img.shape[1] for img in images]
    max_height = max(heights)
    total_width = sum(widths)
    
    resized_images = [cv2.resize(img, (widths[i], max_height)) for i, img in enumerate(images)]
    
    # Concatenate images horizontally
    combined_image = np.hstack(resized_images)
    
    # Display the combined image
    cv2.imshow(frame_type, combined_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

# Display up to 2 I-Frames
display_frames(i_frames_dir, 'I-Frames')

# Display up to 2 P-Frames
display_frames(p_frames_dir, 'P-Frames')

# Display up to 2 B-Frames
display_frames(b_frames_dir, 'B-Frames')
