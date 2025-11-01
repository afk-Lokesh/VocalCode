import pyttsx3 as tts

class CommandExecutor:
    def __init__(self):
        self.engine = tts.init()
        self.engine.setProperty('rate', 180)   # Speech speed
        self.engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)

    def execute_command(self, command):
        print(f"Executing command: {command}")
        # Here you can later add logic like:
        # if "open notepad" in command: os.system("notepad")
        # elif "time" in command: self.speak(datetime.now().strftime("%H:%M"))
        # etc.

    def speak(self, text):
        if not text:
            print("⚠️ No text provided to speak.")
            return
        print(f"🤖 Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
