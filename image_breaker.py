import cv2
import os

# Load the video
video_path = 'video2050373719.mp4'
video = cv2.VideoCapture(video_path)

# Create a directory to store the frames
os.makedirs('frames', exist_ok=True)

# Process the video
frame_count = 0
while True:
    success, frame = video.read()
    if not success:
        break  # No more frames or there's an error

    # Save each frame to the 'frames' directory
    frame_filename = f'frames/frame_{frame_count}.jpg'
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

# Release the video capture object
video.release()
print(f'All frames are extracted and saved to "frames" directory. Total frames: {frame_count}')
