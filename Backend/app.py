from listeners.listener import MicListener
from commands.executor import CommandExecutor

def main():
    listener = MicListener()
    executor = CommandExecutor()

    print("Starting voice command listener...")
    command = listener.listen(timeout=5, phrase_time_limit=10)

    if command:
        print(f"Received command: {command}")
        executor.execute_command(command)
    else:
        print("No command received.")
if __name__ == "__main__":
    main()