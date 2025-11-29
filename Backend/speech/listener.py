import pyaudio
import wave
import time
import struct
from wake_word import porcupine, stream
from whisper_stt import audio_to_text 
import requests


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
BACKEND_URL = "http://localhost:8000/execute"



def record_audio(filename="command.wav"):
    """Record audio from microphone for RECORD_SECONDS"""
    pa = pyaudio.PyAudio()
    stream_rec = pa.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    
    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream_rec.read(CHUNK)
        frames.append(data)

    stream_rec.stop_stream()
    stream_rec.close()
    pa.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Recording finished.")
    return filename


def listen_for_command():
    print("Listening for wake word: VISOR...")

    while True:
        # Read raw audio and unpack it into int16 PCM
        pcm = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        result = porcupine.process(pcm)

        if result >= 0:
            print("Wake word detected! Recording command...")
            
            audio_file = record_audio()
            command_text = audio_to_text(audio_file)

            print(f"Detected Command: {command_text}")

            response = requests.post(BACKEND_URL, json={"command_text": command_text})
            print("Backend Response:", response.json())
            print("Waiting for next command...\n")
            time.sleep(1)


if __name__ == "__main__":
    listen_for_command()
