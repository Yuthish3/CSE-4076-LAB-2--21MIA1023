import subprocess
import json
import matplotlib.pyplot as plt

def extract_frame_info(video_path):
    try:
        # Run ffprobe to get frame type information
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'frame=pict_type',
            '-of', 'json',
            video_path
        ]
        
        # Execute the command and capture the output
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Parse the JSON output
        frames = json.loads(result.stdout)['frames']
        
        # Count the number of I, P, and B frames
        frame_counts = {'I': 0, 'P': 0, 'B': 0}
        for frame in frames:
            pict_type = frame['pict_type']
            frame_counts[pict_type] += 1
        
        # Calculate total frames
        total_frames = sum(frame_counts.values())
        
        # Calculate the percentage of each frame type
        frame_percentages = {key: (count / total_frames) * 100 for key, count in frame_counts.items()}
        
        return {
            'Frame Counts': frame_counts,
            'Frame Percentages': frame_percentages
        }
    
    except Exception as e:
        return {"error": str(e)}

# Example usage
video_path = '/Users/yuthishkumar/Desktop/python project/test_video.mp4'  
frame_info = extract_frame_info(video_path)
print(frame_info)

# Extract data for plotting
frame_counts = frame_info['Frame Counts']
frame_percentages = frame_info['Frame Percentages']

# Plotting the distribution
def plot_frame_distribution(frame_counts, frame_percentages):
    # Bar Chart
    plt.figure(figsize=(12, 6))
    
    # Plot frame counts
    plt.subplot(1, 2, 1)
    bars = plt.bar(frame_counts.keys(), frame_counts.values(), color=['blue', 'green', 'red'])
    plt.title('Frame Type Counts')
    plt.xlabel('Frame Type')
    plt.ylabel('Count')
    
    # Add text above bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')
    
    # Plot frame percentages
    plt.subplot(1, 2, 2)
    plt.pie(frame_percentages.values(), labels=frame_percentages.keys(), autopct='%1.1f%%', colors=['blue', 'green', 'red'])
    plt.title('Frame Type Distribution (%)')
    
    plt.tight_layout()
    plt.show()

# Plot the results
plot_frame_distribution(frame_counts, frame_percentages)


