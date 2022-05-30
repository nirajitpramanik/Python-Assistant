
import pyttsx3
import speech_recognition as sr
import webbrowser  
import datetime  
import wikipedia

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #[1] for female
    engine.say(audio)  
      
    engine.runAndWait()

def check_day():
    d = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
    day = datetime.datetime.today().weekday() + 1
    today = d[day]
    answer = f"Today is {today}"
    return(answer)

def check_time():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]

    date = time[8:10]
    month = time[5:7]
    year = time[0:4]

    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    month = month_dict[int(month)]

    answer = f"Today is {date} of {month}, {year}. {hour}, {min}"
    return answer

def check_question(question):
    if question.lower() == "what day is it":
        answer = check_day()
        return answer
    elif question.lower() == "what time is it":
        answer = check_time()
        return answer
    elif ("search wiki" or "search wikipedia") in question.lower():
        query = question.split("wiki")[1].strip()
        if query.lower().startswith("pedia"):
            query = query[5:].strip()

        result = wikipedia.summary(query, sentences=4)
        speak("According to wikipedia")
        speak(result)

    else:
        query = ""
        question = question.split()
        for i in question:
            query += f"{i}+"
        url = f"https://www.google.com/search?q={query}"
        return "Not Found", url
