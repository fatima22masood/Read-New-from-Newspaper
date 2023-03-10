import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=4b23075b6ebe4764a1435c10d599369a')
    data = r.text
    parsed = json.loads(data)
    for i in range(1,10):
        print(f"news number{i},{parsed['articles'][i]['title']}")
        speak(f"news number{i},{parsed['articles'][i]['title']}")

