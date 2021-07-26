# THAT IS THE RELLY AI
from typing import Text
import speech_recognition
rec = speech_recognition.Recognizer()

x = input("Enter Your Name: ")

while True:
    with speech_recognition.Microphone() as source:
        print("Say Something . . .")
        myad = rec.listen(source)
    text = rec.recognize_google(myad)

    if 'hello' in text:
        print(f"\nHello {x}")

    elif 'how are you' in text:
        print("\nI am good you?")

    elif 'I am fine' in text:
        print("\ngood")

    elif 'goodbye' in text:
        print(f"\ngood bye {x}")
    else:
        print("\nI do not understand you")
