import speech_recognition as sr


def listen_and_transcribe() -> None:
    """Listen to the microphone and print the recognized text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as exc:
        print(f"Could not request results; {exc}")


if __name__ == "__main__":
    listen_and_transcribe()
