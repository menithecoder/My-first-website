import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Constants
OUTPUT_FILENAME = "audio.wav"
DURATION = 10  # Duration of recording in seconds
SAMPLE_RATE = 44100  # Sample rate (samples per second)

def create_audio(duration):
    print("Recording...")
    audio_data = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()  # Wait for the recording to complete

    print("Finished recording.")

    # Save the recorded audio to a WAV file
    wav.write(OUTPUT_FILENAME, SAMPLE_RATE, audio_data)

    print(f"Audio saved as {OUTPUT_FILENAME}")

if __name__ == "__main__":
    create_audio(10)
