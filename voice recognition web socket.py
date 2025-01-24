import speech_recognition as sr
import json
import asyncio
import websockets

# WebSocket server URL
WEBSOCKET_URL = "ws://localhost:8765"

COMMAND_MAPPING = {
    "go forward": "goForward",
    "forward": "goForward",
    "walk": "goForward",
    "go, walk": "goForward",
    "go back": "goBackward",
    "back": "goBackward",
    "turn left": "turnLeft",
    "left": "turnLeft",
    "turn right": "turnRight",
    "right": "turnRight",
    "stop": "stop",
    "dance one" :"dance"
}


def simplify_command(command):
    command = command.lower()
    return COMMAND_MAPPING.get(command, "unknown")


async def send_command_to_js(command):
    async with websockets.connect(WEBSOCKET_URL) as websocket:
        await websocket.send(command)
        print(f"Sent command: {command}")


def recognize_and_send_commands():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Setting up the microphone... Please wait.")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ready. Start speaking!")

    try:
        while True:
            print("Listening...")
            with microphone as source:
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"Recognized: {text}")

                command = simplify_command(text)
                print(f"Command: {command}")

                if command != "unknown":
                    asyncio.run(send_command_to_js(command))
                else:
                    print("Unrecognized command.")

            except sr.UnknownValueError:
                print("Could not understand the speech. Please try again.")
            except sr.RequestError as e:
                print(f"Error connecting to Google Speech Recognition service: {e}")
                break

    except KeyboardInterrupt:
        print("\nProgram terminated.")


if __name__ == "__main__":
    recognize_and_send_commands()