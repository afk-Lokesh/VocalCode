# app.py
from listeners.listener import MicListener
from commands.executor import CommandExecutor

def main():
    executor = CommandExecutor()
    listener = MicListener(executor)

    print("🎙️ Starting voice command listener... Say 'exit' to quit.")
    executor.speak("Voice command listener activated. Say something!")

    while True:
        command = listener.listen(timeout=5, phrase_time_limit=10)

        if command:
            print(f"Received command: {command}")
            executor.speak(f"You said: {command}")  # 👈 Repeats back what you say

            if "exit" in command.lower():
                executor.speak("Exiting! Goodbye!")
                break

            executor.execute_command(command)
        else:
            print("No command received.")
            executor.speak("I didn’t hear anything. Try again.")

if __name__ == "__main__":
    main()
