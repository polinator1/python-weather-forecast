import requests
import json

city = input("Enter the city: ")

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

# get the data about the temperature
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
# print the info
print('It is now', str(temperature), '°C in', city)
print('If feels like', str(temperature_feels), '°C')