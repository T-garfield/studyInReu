#Задание 1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["storeroom"] = 22
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
#Задание 2
translate = {"mountain": "orod", "bread": "bass", "friend":"mellon", "horse": "roch"}
#Задание 3
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurus"] = 0
#Задание 4
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
#Задание 5
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
"Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
#Задание 6
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = dict(zipped_drinks)
#Задание 7
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs, playcounts)}
plays["Purple Haze"] = 1
plays["Respect"] +=5
library = {"The Best Song": plays, "Synday Feelings": {}}
print(f"This is library {library}")