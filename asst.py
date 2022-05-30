from helper import *
import speech_recognition as sr

if __name__ == "__main__":
    #while True:
        #speak("Hello there! Please tell me your question:")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            #speak("Recognising your question....")
            print("Recognising")
            query = r.recognize_google(audio, language='en-in')
            print("You said\n", query.split())

        except Exception as e:
            speak(f"I could not understand your query. There is an error, {e}")
        
    answer = check_question(query)
    
    if answer[0] == "Not Found":
        speak("Opening your query on Google")
        browser = webbrowser.get("chrome")
        browser.open(answer[1])
    else:
        speak(answer)