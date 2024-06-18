import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Řekni svůj příkaz:")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="cs-CZ")
        print(f"Rozpoznaný příkaz: {command}")
        return command
    except sr.UnknownValueError:
        print("Nerozpoznaný příkaz.")
    except sr.RequestError:
        print("Chyba při komunikaci se službou Google Speech Recognition.")
