
#Задание 1
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
 print(breed)
#Задание 2
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket'
]
for game in board_games:
    print(game)
for item in sport_games:
    print(item)
#Задание 3
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)
#Задание 4
student_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
student_period_B =  ["Dora", "Minerva", "Alexa", "Obie"]
for i in student_period_A:
    student_period_B.append(i)
#Задание 5
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
    if dog == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break