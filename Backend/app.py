import speech_recognition as sr
from listeners.listener import MicListener
from commands.executor import CommandExecutor

def main():
    Listen = MicListener()
    execute = CommandExecutor()

    while True:
        print("Listening for command...")
        command = Listen.listen_for_command()
        if command:
            print(f"Command received: {command}")
            execute.execute_command(command)
        else:
            print("No command recognized. Please try again.")
    
