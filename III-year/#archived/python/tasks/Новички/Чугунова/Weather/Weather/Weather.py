import requests

city = input('Введите город, в котором вы хотите узнать текущую погоду и текущий прогноз: ')
def weather(city = 'Berlin'):
    API_method = '/current.json?'
    API_method2 = '/forecast.json?'
    API_Key = '38aa7b12be1b47f086990216212911'
    API_URL = 'http://api.weatherapi.com/v1'
    API_city = 'q=' + city
    response_curr = requests.get(API_URL + API_method + 'key= ' + API_Key + '&' + API_city)
    response_forecast = requests.get(API_URL + API_method2 + 'key= ' + API_Key + '&' + API_city)
    print('Текущая погода в ' + city + ": " + str(response_curr.content))
    print('Прогноз погоды для ' + city + ": " + str(response_forecast.content))
weather(city)
