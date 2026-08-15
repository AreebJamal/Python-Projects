#----------------NEWS READER----------------

import requests
import json

def speak(str):
    from win32com.client  import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    speak("NEWS FOR TODAY......  LETS START")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4ec9342adf184dc49f8544ebef7d64f8"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["status"])
    arts = news_dict["articles"]
    i = 0
    for article in arts:
        speak(article["title"])
       
        i = i+1
        if i==5:
            speak("THESE ARE TODAY'S NEWS..  THANKS FOR LISTENING")
            break
        
        speak("MOVING TO THE NEXT NEWS ..... LISTEN CAREFULLY")