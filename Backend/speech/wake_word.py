import os
from dotenv import load_dotenv
from pvporcupine import Porcupine
import pyaudio

load_dotenv()

ACCESS_KEY = os.getenv("PICOVOICE_KEY")

if not ACCESS_KEY:
    raise Exception("PICOVOICE_KEY missing in .env file")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LIBRARY_PATH = os.path.join(BASE_DIR, "lib", "windows", "amd64", "pv_porcupine.dll")
MODEL_PATH = os.path.join(BASE_DIR, "porcupine_params.pv")
KEYWORD_PATH = os.path.join(BASE_DIR, "visor.ppn")

# Initialize Porcupine
porcupine = Porcupine(
    access_key=ACCESS_KEY,
    library_path=LIBRARY_PATH,
    model_path=MODEL_PATH,
    keyword_paths=[KEYWORD_PATH],
    sensitivities=[0.7]
)


pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)
