from PIL import Image
import matplotlib.pyplot as plt
import os
def load_and_convert_to_array(frame_dir):
    """Load the first frame from the directory and convert it to a numpy array."""
    frame_files = sorted([f for f in os.listdir(frame_dir) if f.endswith('.png')])
    if frame_files:
        img = Image.open(os.path.join(frame_dir, frame_files[0]))
        return img
    else:
        return None
# Load frames
i_frame = load_and_convert_to_array('I_frames')
p_frame = load_and_convert_to_array('P_frames')
b_frame = load_and_convert_to_array('B_frames')

# Display frames side by side
def plot_frame_comparison(i_frame, p_frame, b_frame):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # Plot I-Frame
    if i_frame is not None:
        axs[0].imshow(i_frame)
        axs[0].set_title('I-Frame')
        axs[0].axis('off')

    # Plot P-Frame
    if p_frame is not None:
        axs[1].imshow(p_frame)
        axs[1].set_title('P-Frame')
        axs[1].axis('off')

    # Plot B-Frame
    if b_frame is not None:
        axs[2].imshow(b_frame)
        axs[2].set_title('B-Frame')
        axs[2].axis('off')

    plt.show()
# Visualize the comparison
plot_frame_comparison(i_frame, p_frame, b_frame)