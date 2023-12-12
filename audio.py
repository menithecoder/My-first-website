import pyaudio
import wave
import time

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Mono
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer
# Duration of recording in seconds
OUTPUT_FILENAME = "audio.wav"  # Output file name

def create_audio(record_second):
    # Initialize PyAudio
    audio = pyaudio.PyAudio()
    start_time=time.time()
    print("start teimer")
    # Open the microphone for recording
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")


    frames = []


    # Record audio in chunks and store in frames list
    for i in range(0, int(RATE / CHUNK * record_second)):

        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {OUTPUT_FILENAME}")

if __name__=="__main__":
    create_audio(10)