import requests

city = input("Enter the city you would like to get current weather and forecast for: ")
def current_weather_and_forecast(city ="London"):
    API_Key = '73ed798ec2fc4296af6212121210112'
    API_city='q=' + city
    API_URL ='http://api.weatherapi.com/v1'
    API_method = '/current.json?'
    API_forecast_method = '/forecast.json?'
    response_current=requests.get(API_URL+API_method+'key='+API_Key+'&'+API_city)
    response_forecast=requests.get(API_URL+API_forecast_method+'key='+API_Key+'&'+API_city)
    print('Current weather in ' + city + ": " + str(response_current.content))
    print('')
    print('Weather forecast for ' + city + ": " + str(response_forecast.content))


current_weather_and_forecast(city)
