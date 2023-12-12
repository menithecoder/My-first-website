from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
import os
from moviepy.editor import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import audio
import movie
import threading

# Define functions to create audio and movie concurrently
def create_audio(second):
    audio.create_audio(second)

def create_movie(second):
    movie.create_movie(second)

print("Please enter how much miniut do you want to record  ")
user_input = float(input())
time=user_input*60
# Run the functions concurrently using threads
audio_thread = threading.Thread(target=create_audio,args=(time,))
movie_thread = threading.Thread(target=create_movie,args=(time,))

audio_thread.start()
movie_thread.start()

# Wait for both threads to finish before proceeding
audio_thread.join()
movie_thread.join()
# Once both threads are finished, continue with combining audio and video
# Replace 'movie.avi' with the path to your AVI video file


# Load your existing video
video = VideoFileClip('movie.avi')

# Load the audio file
wav = AudioFileClip('audio.wav')

# Set the video file's audio to the provided audio
video = video.set_audio(wav)

# Load the camera feed (replace 'camera_video.mp4' with your camera recording)
camera_feed = VideoFileClip('camera_video.mp4')

# Define the size of the final video
final_width = video.w + camera_feed.w
final_height = max(video.h, camera_feed.h)

# Resize camera feed to fit the bottom left corner of the video
camera_feed = camera_feed.resize(height=video.h / 4)  # Adjust the size as needed

# Place the camera feed at the bottom left corner
camera_position = (0, final_height - camera_feed.h)

# Combine the existing video and the camera feed as an overlay
final_video = CompositeVideoClip([video.set_position('center'), camera_feed.set_position(camera_position)])

# Define the output file path within the downloads directory
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
output_file_path = os.path.join(downloads_dir, 'output_video_with_camera.mp4')

# Export the final video with the combined audio and camera overlay as an MP4 file in the downloads folder
final_video.write_videofile(output_file_path, codec='libx264', audio_codec='aac')
