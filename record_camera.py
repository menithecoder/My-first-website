import cv2
import threading
import time

class VideoRecorder(threading.Thread):
    def __init__(self, duration):
        super().__init__()
        self.duration = duration
        self.time_diff = None

    def run(self):
        video_capture = cv2.VideoCapture(0)

        self.time_diff = 1
        normal_fps = 20  # Normal frames per second
        adjusted_fps = normal_fps * 1.5  # Adjusted frames per second for faster recording
        delay = 1.0 / adjusted_fps
        frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec
        out = cv2.VideoWriter('camera_video.mp4', fourcc, adjusted_fps, (frame_width, frame_height))

        start_time = time.time()
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            out.write(frame)


            # Calculate elapsed time and break if duration exceeded
            elapsed_time = time.time() - start_time

            if elapsed_time >= self.duration:
                break

            # Calculate the time to sleep to achieve desired FPS
            execution_time = time.time() - start_time
            sleep_time = max(0, delay - execution_time)
            time.sleep(sleep_time)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        out.release()
        cv2.destroyAllWindows()

    def get_time_diff(self):
        return self.time_diff

# Example usage:
