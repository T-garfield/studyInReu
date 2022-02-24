import requests
def temperature(city='Moscow'):
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7d75ea53a21e0e424391e9724ef253e4'
    json = requests.get(link).json()
    main_json = json['main']
    temp_k = main_json['temp']
    temp_c = round(temp_k - 273)
    print(f'Температура в {city} сейчас {temp_c}С')

#temperature()
temperature('london')
