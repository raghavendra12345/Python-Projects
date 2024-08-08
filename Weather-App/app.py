import datetime as dt
import requests

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius=kelvin-273.0
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit   

#create an account on openweather map and obtain your API key.
BASE_URL="http://api.openweathermap.org/data/2.5/weather?"

api_key='4eec62d032f2a79ed924d2e3ab12985a'

user_input=input("Enter your city: ")

url= BASE_URL+"appid="+api_key+"&q="+user_input

response=requests.get(url).json()

temp_kelvin=response['main']['temp']
temp_celsius, temp_fahrenheit=kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin=response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit=kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humidity= response['main']['humidity']
wind_speed=response['wind']['speed']
description=response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])


print(f"Temperature in {user_input}:{temp_celsius:.2f}.C or {temp_fahrenheit}.F")
print(f"Temperature in {user_input}:{feels_like_celsius:.2f}.C or {feels_like_fahrenheit}.F")
print(f"Humidity in {user_input}:{humidity}%")
print(f"Wind Speed in {user_input}:{wind_speed} m/s")
print(f"General weather in {user_input}:{description}")
print(f"Sun rises in {user_input} at {sunrise_time} local time.")
print(f"Sun sets in {user_input} at {sunset_time} local time.")






