import requests

def get_weather(city):
    API_Key = '8195d40657814ef699992949212911'
    URL = f'http://api.weatherapi.com/v1/forecast.json?key={API_Key}&q={city}'
    r = requests.get(URL)
    res = r.json()
    
    print("\n   FORECAST    ")
    day_fore = res['forecast']['forecastday'][0]['date']
    condition_fore = res['forecast']['forecastday'][0]['day']['condition']['text']
    maxtemp_c_fore = res['forecast']['forecastday'][0]['day']['maxtemp_c']
    mintemp_c_fore = res['forecast']['forecastday'][0]['day']['mintemp_c']
    maxwind_fore = res['forecast']['forecastday'][0]['day']['maxwind_mph']
    daily_chance_of_rain_fore = res['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    daily_chance_of_snow_fore = res['forecast']['forecastday'][0]['day']['daily_chance_of_snow']
    print(f"Date: {day_fore}\nCondition: {condition_fore}\nMax Temperature: {maxtemp_c_fore}°C\nMin Temperature: {mintemp_c_fore}°C\nMax Wind: {maxwind_fore} mph\nChance of rain: {daily_chance_of_rain_fore}%\nChance of snow: {daily_chance_of_snow_fore}%")

city = input("City: ")
get_weather(city)