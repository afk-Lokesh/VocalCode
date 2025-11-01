import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please say something...")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        transcription = recognizer.recognize_google(audio)
        print("You said: " + transcription)
    except sr.RequestError:
        print("API unavailable or unresponsive")
    except sr.UnknownValueError:
        print("Unable to recognize speech")

if __name__ == "__main__":
    main()