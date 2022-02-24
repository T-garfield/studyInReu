#1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["storeroom"] = 22
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

#2
dictionary = {"mountain" : 'orod', "bread": 'bass', "frieind" : 'mellon', "horse" : 'roch'}

#3
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurus"] = 0
print(animals_in_zoo)

#4
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#5
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = 'Viola Davis'
oscar_winners['Best Picture'] = 'Moonlight'

#6
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

#7
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key: value for key, value in zip(songs,playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays['Respect'] = 5
library = {'The Best Songs' : plays, "Sunday Feelings" : {}}
print(library)