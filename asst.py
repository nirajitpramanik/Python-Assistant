from helper import *
import speech_recognition as sr
import time
import random

if __name__ == "__main__":
    awake = True
    ini_loop = True
    while awake:
        if ini_loop:
            print("--------------------------------------")
            print("Welcome to your very own assistant made in Python.\n\n")
            print("Get started by asking a question after 'Listening...' appears on the screen.")
            print("----------")
            time.sleep(3)

            speak("Hello there! Please tell me your question:")
            ini_loop = False

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            lis = random.choice(["Go ahead, I'm listening...", "I'm listening...", "Speak now..."])
            speak(lis)
            audio = r.listen(source)
            try:
                #speak("Recognising your question....")
                print("🗘 Recognising")
                query = r.recognize_google(audio, language='en-in')
                print("You said\n", query)

            except Exception as e:
                speak(f"I could not understand your query. There is an error, {e}")

        answer = check_question(query)
        
        if answer[0] in ["Not Found", "Wikipedia", "Youtube"]:
            if answer[0] == "Not Found":
                speak("Opening your query on Google")
            elif answer[0] == "Wikipedia":
                speak("Opening the page on Wikipedia")
            else:
                speak("Opening youtube")

            chrome_path= r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            webbrowser.register('brave', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get("brave").open(answer[1])
        else:
            speak(answer)

        time.sleep(5)
        question = random.choice(["Would you like to ask another question?", "Have another question in mind?", "Got another question for me?"])
        cont = speak(question)
        inp = input("Yes/No: ")

        if inp.lower() in ["no", "n"]:
            awake = False
            speak("Thank you, and have a great day!")
            print("--------------------------------------")