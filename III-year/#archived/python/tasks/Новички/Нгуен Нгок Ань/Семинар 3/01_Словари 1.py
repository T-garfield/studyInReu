print("*** Задание 1 ***")
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors["pantry"] = 22
print(sensors)
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(num_cameras)

print("\n*** Задание 2 ***")
eng_to_sin = {'mountain':'orod','bread':'bass','friend':'mellon','horse':'roch'}
print(eng_to_sin)

print("\n*** Задание 3 ***")
animals_in_zoo = {}
animals_in_zoo['зебры'] = 8
animals_in_zoo['обезьяны'] = 12
animals_in_zoo['динозавров'] = 0
print(animals_in_zoo)

print("\n*** Задание 4 ***")
ser_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
ser_ids.update({'theLooper': 138475, 'stringQueen': 85739})
print(ser_ids)

print("\n*** Задание 5 ***")
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners['Supporting Actress'] = 'Viola Davis'
oscar_winners['Best Picture'] = 'Moonlight'
print(oscar_winners)

print("\n*** Задание 6 ***")
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

print("\n*** Задание 7 ***")
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs,playcounts)}
print(plays)
plays['Purple Haze'] = 1
plays['Respect'] = 5
library = {'The Best Songs':plays, 'Sunday Fellings':{}}
print(library)