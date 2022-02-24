import requests

API_KEY = '6514806ed97440f1949195123210512'
API_URL = 'http://api.weatherapi.com/v1'
API_method = '/current.json?'
API_city = 'q=' + input('Введите название города: ')
response = requests.get(API_URL + API_method + 'key=' + API_KEY + '&' + API_city)
print(response.content)