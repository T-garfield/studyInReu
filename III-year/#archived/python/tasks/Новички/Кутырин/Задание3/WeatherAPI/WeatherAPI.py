import requests

def function(city):
    parameters = {}
    parameters["url"] = "http://api.weatherapi.com/v1/"
    parameters["method"] = "forecast.json?"
    parameters["key"] = "key=7c24095db2a54906a2f90357212911&q="
    parameters["city"] = city
    parameters["days_of_forecast"] = "&days=1"
    parameters["aqi"]= "&aqi=no" 
    parameters["alerts"] = "&alerts=no"
    string = parameters.values()
    response = requests.get("".join(str(x) for x in string))
    weather = response.json()

    print("Local time: "+str(weather["location"]["localtime"])+"\n"
      +str(weather["location"]["name"])+" "+"temperature: "+str(weather["current"]["temp_c"])+"\n"
      +"Feels like: "+str(weather["current"]["feelslike_c"])+"\n"
      +"Speed of wind: "+str(weather["current"]["wind_kph"])+"\n"
      +"Humidity: "+str(weather["current"]["humidity"])+"\n")

    print("Forecast on tomorrow: \n"
      "Max temperature: "+str(weather["forecast"]["forecastday"][0]["day"]["maxtemp_c"])+"\n"
      "Min temperature: "+str(weather["forecast"]["forecastday"][0]["day"]["mintemp_c"]))  
    # [0] СТОИТ ПОТОМУ, ЧТО www.weatherapi.com НРАВИТСЯ В СПИСОК ПОМЕЩАТЬ ОДИН СЛОВАРЬ С 10000 ЭЛЕМЕНТОВ -_-

function(input("What's the city?: "))


'''
parameters = {}
parameters["url"] = "http://api.weatherapi.com/v1/"
parameters["method"] = "forecast.json?"
parameters["key"] = "key=7c24095db2a54906a2f90357212911&q="
parameters["city"] = input("What's the city?: ")
parameters["days_of_forecast"] = "&days=1"
parameters["aqi"]= "&aqi=no" 
parameters["alerts"] = "&alerts=no"

string = parameters.values()
response = requests.get("".join(str(x) for x in string))
weather = response.json()

print("Local time: "+str(weather["location"]["localtime"])+"\n"
      +str(weather["location"]["name"])+" "+"temperature: "+str(weather["current"]["temp_c"])+"\n"
      +"Feels like: "+str(weather["current"]["feelslike_c"])+"\n"
      +"Speed of wind: "+str(weather["current"]["wind_kph"])+"\n"
      +"Humidity: "+str(weather["current"]["humidity"])+"\n")

print("Forecast on tomorrow: \n"
      "Max temperature: "+str(weather["forecast"]["forecastday"][0]["day"]["maxtemp_c"])+"\n"
      "Min temperature: "+str(weather["forecast"]["forecastday"][0]["day"]["mintemp_c"]))  
# [0] СТОИТ ПОТОМУ, ЧТО www.weatherapi.com НРАВИТСЯ В СПИСОК ПОМЕЩАТЬ ОДИН СЛОВАРЬ С 10000 ЭЛЕМЕНТОВ -_- 
'''


