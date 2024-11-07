import speech_recognition as sr  # Library for voice recognition
import pyttsx3                   # Library for text-to-speech
import datetime                  # Library for date and time functions
import webbrowser                # Library for opening URLs in the browser

# Initialize the speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """
    Convert text to speech.
    :param text: Text string to be converted to speech
    """
    engine.say(text)
    engine.runAndWait()

def greet():
    """
    Generate a greeting based on the time of day.
    :return: A greeting string
    """
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"

def listen_command():
    """
    Listen for voice commands and convert them to text.
    :return: Command as a text string, or None if not understood
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        print("Listening...")
        audio = recognizer.listen(source)  # Capture audio
        try:
            # Recognize speech using Google's recognition engine
            command = recognizer.recognize_google(audio).lower()
            print("User said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that. Could you repeat?")
            return None

def respond_to_command(command):
    """
    Respond to a given command based on predefined conditions.
    :param command: The recognized voice command as text
    """
    # Respond to a greeting
    if "hello" in command:
        speak("Hello! " + greet())

    # Provide the current time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    # Provide the current date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")

    # Search the web for a specific query
    elif "open" in command:
        speak("What would you like to search for?")
        query = listen_command()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    # Command not recognized
    else:
        speak("Sorry, I can't help with that.")

def main():
    """
    Main function to run the voice assistant.
    Continuously listens for commands until 'exit' or 'stop' is heard.
    """
    speak("Hello! My name is max. How can I help you today?")
    while True:
        command = listen_command()  # Listen for a command
        if command:
            if "exit" in command or "stop" in command:
                speak("Cancel!")
                break  # Exit the loop and end the program
            else:
                respond_to_command(command)  # Process the command

if __name__ == "__main__":
    main()