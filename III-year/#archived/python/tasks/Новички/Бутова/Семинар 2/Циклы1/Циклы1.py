#1
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for game in sport_games:
    print(game)

#2
phrase = "I will not chew gum in class"
for i in range(5):
    print(phrase) 
#3
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
print(students_period_B)
#4
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break