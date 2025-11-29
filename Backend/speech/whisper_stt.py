from faster_whisper import WhisperModel

model = WhisperModel("tiny", device="cpu", compute_type="int8")

def audio_to_text(audio_path):
    segments, info = model.transcribe(audio_path)
    text = " ".join([seg.text for seg in segments])
    return text
