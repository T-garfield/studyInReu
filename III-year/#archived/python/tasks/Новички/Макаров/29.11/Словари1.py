print("№1")
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["storeroom"] = 22
print(sensors)


num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(num_cameras)
print("............................................")

print("№2")
elvish = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(elvish)
print("...............................................")

print("№3")
animals_in_zoo = {}
animals_in_zoo["zebra"] = 8
animals_in_zoo["monkey"] = 12
animals_in_zoo["dino"] = 0
print(animals_in_zoo)
print("............................................")


print("№4")
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
print(".............................................")

print("№5")
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis", "Best Picture": "Moonlight"})
print(oscar_winners)
print("........................................................")

print("№6")
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
print("...........................................................")

print("№7")
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
plays.update({"Purple Haze": 1, "Respect": 5})
#print(plays)
library ={"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
print("............................................")