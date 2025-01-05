import speech_recognition as sr
import json

# Mapping spoken phrases to simplified commands
COMMAND_MAPPING = {
    "go forward": "forward",
    "forward": "forward",
    "walk": "forward",
    "go, walk": "forward",
    "go back": "backward",
    "back": "backward",
    "turn left": "left",
    "left": "left",
    "turn right": "right",
    "right": "right",
    "stop": "stop",
}


# Function to map a command to its simplified version
def simplify_command(command):
    command = command.lower()
    return COMMAND_MAPPING.get(command, "unknown")


# Function to recognize speech and save it to JSON
def recognize_and_save_to_json(json_file):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    commands = []

    print("Setting up the microphone... Please wait a moment.")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ready. Start speaking!")

    try:
        while True:
            print("Listening...")
            with microphone as source:
                audio = recognizer.listen(source)

            try:
                # Recognizing speech
                text = recognizer.recognize_google(audio, language="en-US")
                print(f"Recognized: {text}")

                # Simplifying the command
                simplified_command = simplify_command(text)
                print(f"Command: {simplified_command}")

                # Saving the command
                if simplified_command != "unknown":
                    # Reading the existing JSON file
                    try:
                        with open(json_file, "r") as file:
                            commands = json.load(file)
                    except FileNotFoundError:
                        commands = []

                    # Adding the new command and writing it to the file
                    commands.append(simplified_command)
                    with open(json_file, "w") as file:
                        json.dump(commands, file, indent=4)
                    print(f"Command '{simplified_command}' saved to {json_file}.")

            except sr.UnknownValueError:
                print("Could not understand the speech. Please try again.")
            except sr.RequestError as e:
                print(f"Error connecting to Google Speech Recognition service: {e}")
                break

    except KeyboardInterrupt:
        print("\nProgram terminated.")


if __name__ == "__main__":
    recognize_and_save_to_json("commands.json")
