# 1
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
# 2
print()
dic = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# 3
print()
animals_in_zoo = {}
animals_in_zoo["Зебры"] = 8
animals_in_zoo["Обезьяны"] = 12
animals_in_zoo["Динозавров"] = 0
print(animals_in_zoo)

# 4
print()
ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
ser_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(ser_ids)

# 5
print()
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

# 6
print()
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)
print(list(zipped_drinks))

# 7
print()
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs,playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays["Respect"] = 5
library = {"The Best Song": plays, "Sunday Fellings": {}}
print(library)
