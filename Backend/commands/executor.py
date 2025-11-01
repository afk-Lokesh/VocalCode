import speech_recognition as sr, pyttsx3, subprocess, re, time, random
r = sr.Recognizer()

def speak(t):
    print("Assistant:", t)
    e = pyttsx3.init(); e.say(t); e.runAndWait(); e.stop(); time.sleep(0.4)

def run_code(f="test.py"):
    try:
        p = subprocess.run(["python", f], capture_output=True, text=True)
        o, e = p.stdout.strip(), p.stderr.strip()
        if o: speak(f"Program output: {o[:150]}")
        elif e:
            speak("An error occurred.")
            if m := re.search(r'(\w+Error)', e): speak(f"Error type: {m.group(1)}.")
            speak("Error details: " + e[:150])
        else: speak("Program ran successfully with no output.")
    except Exception as x: speak(f"Failed to run code: {x}")

def listen():
    with sr.Microphone() as s:
        r.adjust_for_ambient_noise(s); speak("Hello! How can I help you?")
        while True:
            print("\nListening...")
            try: c = r.recognize_google(r.listen(s, phrase_time_limit=5)).lower(); print("You said:", c)
            except sr.UnknownValueError: speak("I didn't catch that."); continue
            except sr.RequestError: speak("Speech recognition service error."); continue

            if "run code" in c: speak("Running your code now."); run_code()
            elif "stop" in c or "exit" in c: speak("Goodbye! Have a nice day."); break
            elif "hello" in c: speak("Hi there! Hope you're doing great.")
            elif "how are you" in c: speak("I'm doing awesome! Ready to help you anytime.")
            elif "thank you" in c: speak("You're welcome!")
            else: speak(random.choice(["Sorry, I didn’t understand that.", "Could you repeat that?"]))

if __name__ == "__main__": listen()
