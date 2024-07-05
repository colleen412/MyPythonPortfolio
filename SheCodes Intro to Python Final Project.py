import requests
from rich import print
from datetime import datetime

print('[green bold]Welcome to my weather app![/green bold]\n')
city = input('Enter a city: ')
city = city.strip()
city = city.capitalize()


def current_weather(city):
  api_key = '649bacd404ba629od0f5c308d505aat9'
  api_url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}'

  response = requests.get(api_url)
  response = response.json()
  response_city = response['city']
  response_current_temp = round(response['temperature']['current'])
  converted_current_temp = round((response_current_temp * 9 / 5) + 32)

  print(
      f'Today in {response_city} it\'s {response_current_temp}°C ({converted_current_temp}°F).'
  )


def forecast_weather(city):
  api_key = '649bacd404ba629od0f5c308d505aat9'
  forecast_api_url = f'https://api.shecodes.io/weather/v1/forecast?query={city}&key={api_key}'
  forecast_response = requests.get(forecast_api_url)
  forecast_response = forecast_response.json()

  for day in forecast_response['daily']:
    timestamp = day['time']
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime('%A')
    temp = round(day['temperature']['day'])
    converted_temp = round((temp * 9 / 5) + 32)

    if date.date() != datetime.today().date():
      print(f'{formatted_day}: {temp}°C ({converted_temp}°F).')


if city:
  current_weather(city)
  print('\n[green bold]Forecast:[/green bold]')
  forecast_weather(city)
  print('\nThis app was built by [green bold]Colleen O\'Leary[/green bold]!')

else:
  print('Please try again with a city.')

#It should not be so goddamned difficult to sent files to GitHub!
