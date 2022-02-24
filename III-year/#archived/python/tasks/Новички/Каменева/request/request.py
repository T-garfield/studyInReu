import requests
print(requests.__version__)

API_URL = ' http://api.weatherapi.com/v1'
API_Key = '48f186cea116491c87b90544212911'
#http://api.weatherapi.com/v1/current.json?key=&q=London&aqi=no

API_metod='/current.json?'
API_city='q=London'

response = requests.get(API_URL+API_metod+'key='+API_Key+'&' + API_city)

#вывести дсон файл

print(response) # 401 - не правильно , 201 - верно

print(response.content)