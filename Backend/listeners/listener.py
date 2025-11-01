import speech_recognition as sr
from commands.executor import CommandExecutor

class MicListener:
    def __init__(self, executor: CommandExecutor):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.executor = executor

    def listen(self, timeout=5, phrase_time_limit=10):
        with self.microphone as source:
            print("🎧 Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("🎤 Listening...")

            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            except sr.WaitTimeoutError:
                print("⏳ Listening timed out.")
                return None

        try:
            print("🧠 Recognizing speech...")
            command = self.recognizer.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError as e:
            print(f"⚠️ Speech recognition error: {e}")
        return None
