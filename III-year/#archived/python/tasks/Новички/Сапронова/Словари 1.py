import requests

api_key = "4d3f311d52e247c583592817212911"
api_url = "http://api.weatherapi.com/v1"
api_method1 = "/current.json?"
api_city = "q=London"
api_method2 = "/forecast.json?"
api_days = "1"

response = requests.get(api_url+api_method1 +"key="+api_key+"&"+api_city+api_method2+"key="+api_key+"&"+api_city+api_days)
print(response.content)

#1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["ware"]=22
print(sensors)
#2
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
#3
language = {"mountain": "orod", "bread": "bass", "friend ": "mellon", "horse": "roch"}
#4
animals_in_zoo = {}
animals_in_zoo["zebra"]=8
animals_in_zoo["monkey"]=12
animals_in_zoo["dino"]=0
print(animals_in_zoo)
#5
ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
ser_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(ser_ids)
#6
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"]="Viola Davis"
oscar_winners["Best Picture"]="Moonlight"
#7
zipped_drinks = {key:value for key, value in zip(drinks, caffeine)}
print(zipped_drinks)
#8
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays["Purple Haze"]=1
plays["Respect"]=5
lib = {}
library = {"The Best Songs": plays, "Sunday Feelings": lib}
print(library)


