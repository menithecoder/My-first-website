import cv2
import numpy as np
import pyautogui
import time

def create_movie(record_second):
    output_file = 'movie.avi'
    codec = cv2.VideoWriter_fourcc(*'MJPG')
    fps = 10.0
    screen_width, screen_height = pyautogui.size()
    out = cv2.VideoWriter(output_file, codec, fps, (screen_width, screen_height))
    print("Movie start")

    # Calculate the total number of frames needed for the specified duration
    total_frames = int(fps * (record_second))

    # Calculate the duration of each frame in seconds
    frame_duration = 1.0 / fps

    start_time = time.time()

    # Capture screenshots and add frames to the video based on timestamps
    for i in range(total_frames):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

        # Calculate the expected timestamp of the next frame
        expected_frame_time = start_time + (i + 1) * frame_duration

        # Wait until the expected frame time is reached
        while time.time() < expected_frame_time:
            pass  # Wait until the next frame time

    # Release the video writer and close OpenCV windows

    print("Finished recording")


