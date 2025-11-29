from pvporcupine import Porcupine
import pyaudio

porcupine = Porcupine(keywords=['visor'])
pa = pyaudio.PyAudio()
stream = pa.open(rate=porcupine.sample_rate,
                 channels=1,
                 format=pyaudio.paInt16,
                 input=True,
                 frames_per_buffer=porcupine.frame_length)

while True:
    pcm = stream.read(porcupine.frame_length)
    result = porcupine.process(pcm)
    if result >= 0:
        print("Wake word detected!")
        break
