import requests

#prompt user to input valid city name
location  = input('Please enter a city name: (Example: Dallas or Seattle)')

#my API from OpenWeatherMap.org
full_api_link = 'https://api.openweathermap.org/data/2.5/weather?appid=3110c63d8ecf6fc2f60a46d243c8533a'

api_link = requests.get(full_api_link)
api_data = api_link.json()

#if invalid city it input, prompt user to input valid city
if api_data['cod'] == '404':
    print('Invalid city. {},  Please enter a valid city name: '.format(location))

#once valid city is input, API returns forecast
else:
    #display specific weather data from OpenWeatherMap API return
    temp_city = ((api_data['main']['temp']) ('temp' - 273.15) * 9/5 + 32 # formula for kelvin to F'
    weather_description = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    #date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p') (not sure I need this)

#print forecast in readable form to the user
    print('weather stats for - {}  ||  {}'.format(location.upper(), date_time))

    print('Current temperature is     : deg F'.format(temp_city))
    print('Current weather description:', weather_description)
    print('Current Humidity           :', humidity, '%')
    print('Current Wind speed         :', wind_speed, 'mph')