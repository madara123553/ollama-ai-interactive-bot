from transcriber import transcribe
from tts import speak
from commands import handle_command

def main():
    print("🎤 Listening for your command...")
    text = transcribe()
    print("🗣️ You said:", text)

    response = handle_command(text)
    print("🤖", response)
    speak(response)

if __name__ == "__main__":
    while True:
        main()
