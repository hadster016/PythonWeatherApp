import requests 
import re
def welcome():
    print("Welcome to the Weather app.")
 
def Thankyou():
    print("Thankyou for using weather forecast application")
 
welcome()
#Ask user for city
q1 = input("Please input the city you want weather for? ").capitalize()

#validate
def validate_input(answer, pattern):
    if re.match(pattern, answer):
        return True
    else:
        return False

pattern = r"^[A-Za-z]+$"
def is_valid_city(city_name):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=22b27f7b26f7cd943768098058bcb7b7")
    # print(response)
    return response.status_code == 200

#Return to user if invalid city
while not validate_input(q1, pattern) or not is_valid_city(q1):
    print("Invalid input. Please enter a valid city name.")
    q1 = input("Please input the city you want weather for? ").capitalize()

# Get weather data from API
def get_weather(city):
    api_key = "22b27f7b26f7cd943768098058bcb7b7"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

#Get weather data for ths input city
weather_data = get_weather(q1)

# Extract temperature from weather data
temperature = weather_data['main']['temp']
temp_convert_to_celcius = round(temperature - 273.15, 2)
description = weather_data['weather'][0]['description']
windspeed = weather_data['wind']['speed']
humidity = weather_data['main']['humidity']

# Print to screen
print(f"The temperature in {q1} is {temp_convert_to_celcius}\N{DEGREE SIGN}C")
print(f"The weather in {q1} is {description}")
print(f"The wind speed in {q1} is {windspeed}m/s")
print(f"The humidity in {q1} is {humidity}%")
Thankyou()

#?{'coord': {'lon': 2.3488, 'lat': 48.8534},
# ?'weather':  [{'id': 500, 'main': 'Rain',
# ? 'description': 'light rain', 'icon': '10n'}],
#?    'base': 'stations', 
# ? 'main': {'temp': 281.06, 'feels_like': 278.07, 'temp_min': 280.03, 'temp_max': 281.53, 'pressure': 1005, 'humidity': 96, 'sea_level': 1005, 'grnd_level': 995},
#?    'visibility': 10000,
# ?     'wind':  {'speed': 5.14, 'deg': 180}, 'rain': {'1h': 0.24}, 'clouds': {'all': 75}, 'dt': 1738171953,
#?        'sys': {'type': 2, 'id': 2012208, 'country': 'FR', 'sunrise': 1738135479, 'sunset': 1738168959},
#?        'timezone': 3600, 'id': 2988507, 'name': 'Paris', 'cod': 200}