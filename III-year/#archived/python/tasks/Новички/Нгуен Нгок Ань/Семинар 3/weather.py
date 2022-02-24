import requests

def get_weather(city):
    API_Key = '8195d40657814ef699992949212911'
    URL = f'http://api.weatherapi.com/v1/forecast.json?key={API_Key}&q={city}'
    r = requests.get(URL)
    res = r.json()
    country = res['location']['country']
    local_time = res['location']['localtime']
    condition_current = res['current']['condition']['text']
    temp_c_current = res['current']['temp_c']
    feelslike_c_current = res['current']['feelslike_c']
    wind_current = res['current']['wind_mph']
    humidity_current = res['current']['humidity']
    print(f"Country: {country}\nLocal time: {local_time}")
    print(f"Condition: {condition_current}\nTemperature: {temp_c_current}°C\nFeels like temperature: {feelslike_c_current}°C\nWind: {wind_current} mph\nHumidity: {humidity_current}%")
    
    print("\n   FORECAST    ")
    day_fore = res['forecast']['forecastday'][0]['date']
    condition_fore = res['forecast']['forecastday'][0]['day']['condition']['text']
    maxtemp_c_fore = res['forecast']['forecastday'][0]['day']['maxtemp_c']
    mintemp_c_fore = res['forecast']['forecastday'][0]['day']['mintemp_c']
    maxwind_fore = res['forecast']['forecastday'][0]['day']['maxwind_mph']
    daily_chance_of_rain_fore = res['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    daily_chance_of_snow_fore = res['forecast']['forecastday'][0]['day']['daily_chance_of_snow']
    print(f"Date: {day_fore}\nCondition: {condition_fore}\nMax Temperature: {maxtemp_c_fore}°C\nMin Temperature: {mintemp_c_fore}°C\nMax Wind: {maxwind_fore} mph\nChance of rain: {daily_chance_of_rain_fore}%\nChance of snow: {daily_chance_of_snow_fore}%")

    print("\n   HOURLY FORECAST ")    
    for i in range(24):
        hour = res['forecast']['forecastday'][0]['hour'][i]['time']
        condition_hour = res['forecast']['forecastday'][0]['hour'][i]['condition']['text'] 
        temp_c_hour = res['forecast']['forecastday'][0]['hour'][i]['temp_c']
        feelslike_c_hour = res['forecast']['forecastday'][0]['hour'][i]['feelslike_c'] 
        humidity_hour = res['forecast']['forecastday'][0]['hour'][i]['humidity'] 
        print(f"\nDate: {hour}\nCondition: {condition_hour}\nTemperature: {temp_c_hour}°C\nFeels Like Temperature: {feelslike_c_hour}°C\nHumidity: {humidity_hour}%")
city = input("City: ")
get_weather(city)