import requests

#http://api.weatherapi.com/v1/current.json?key=d75527bd1cbe48f6b2f145909210512&q=Lobnya&aqi=no

def weather_now(city):

    API_Key = 'd75527bd1cbe48f6b2f145909210512'
    API_URL ='http://api.weatherapi.com/v1'
    API_method = '/current.json?'
    API_city='q=Lobnya'
    
    response=requests.get(API_URL+API_method+'key='+API_Key+'&'+API_city)
    
    print(response.content)

weather_now('Lobnya')


def weather_forecast(city):

    API_Key = 'd75527bd1cbe48f6b2f145909210512'
    API_URL ='http://api.weatherapi.com/v1'
    API_method = '/forecast.json?'
    API_city='q=Kostroma'

    response=requests.get(API_URL+API_method+'key='+API_Key+'&'+API_city)

    print(response.content)

weather_forecast('Kostroma')
