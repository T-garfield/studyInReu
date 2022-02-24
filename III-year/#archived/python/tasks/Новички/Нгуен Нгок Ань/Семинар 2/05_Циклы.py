print("*** Задание 1 ***")
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)

print("\n*** Задание 2 ***")
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for game in sport_games:
    print(game)

print("\n*** Задание 3 ***")
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)

print("\n*** Задание 4 ***")
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for i in students_period_A:
    students_period_B.append(i)
    print(students_period_B)

print("\n*** Задание 5 ***")
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for i in dog_breeds_available_for_adoption:
    print(i)
dog_breed_I_want = 'dalmatian'
for i in dog_breeds_available_for_adoption:
    if i == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break