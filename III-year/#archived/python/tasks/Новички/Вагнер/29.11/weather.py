import requests

#http://api.weatherapi.com/v1/current.json?key=f1a7b81cffea4093b8062602212911&q=London&aqi=no
API_KEY = '7d2f27b0dae943aa9c6160304210412'
API_URL = 'http://api.weatherapi.com/v1'
API_method = '/current.json?'
API_city = 'q=' + input('Введите наименование города на английском: ')

response = requests.get(API_URL + API_method + 'key=' + API_KEY + '&' + API_city)
print(response.content)