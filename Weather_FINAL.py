import requests
import datetime

#prompt user to input valid city name
location  = input('Please enter a city name: (Example: Dallas or Seattle)')

#my API from OpenWeatherMap.org
full_api_link = 'https://api.openweathermap.org/data/2.5/weather?q={0}&appid=3110c63d8ecf6fc2f60a46d243c8533a&q='.format(location)

api_link = requests.get(full_api_link)
api_data = api_link.json()

temp_city = None
weather_description = None
humidity = None
wind_speed = None

data_time = datetime.datetime
#if invalid city it input, prompt user to input valid city
if api_data['cod'] == '404':
    print('Invalid city. {0},  Please enter a valid city name: '.format(location))

#once valid city is input, API returns forecast
else:
    #display specific weather data from OpenWeatherMap API return
    temp_city = (((api_data['main']['temp'])- 273.15) * 9/5 + 32) # formula for kelvin to F'
    weather_description = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    
#print forecast in readable form to the user
print('weather stats for - {0}'.format(location.upper()))

print('Current temperature is {0}    : deg F'.format(temp_city))
print('Current weather description:', weather_description)
print('Current Humidity           :', humidity, '%')
print('Current Wind speed         :', wind_speed, 'mph')