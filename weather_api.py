
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        weather = response['weather'][0]['description']
        temp = response['main']['temp']
        return weather, temp
    except:
        return "Error", "N/A"
