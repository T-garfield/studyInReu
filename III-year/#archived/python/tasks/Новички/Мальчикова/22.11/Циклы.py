#Цикл 1
#Задача №1
print("-_№1_-")
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
 print(breed)
print("")

#Задача №2
print("-_№2_-")
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in sport_games:
    print(game)
print("")

#Задача №3
print("-_№3_-")
#promise = "I will not chew gum in class"
for promice in range(5):
    print ("I will not chew gum in class")
    
print("")


#Задача №4
print("-_№4_-")
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
    print(students_period_B)
print("")

#Задача №5
print("-_№5_-")
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print('Я бы хотела одну из этих собачек')
        break
print("")
print("")
print("")


#Цикл 2
#Задача №1
print("-_№1_-")
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for x in sales_data:
    for y in x:
        print(y)
        scoops_sold = y + scoops_sold
print("Сумма:", scoops_sold)
print("")

#Задача №2
print("-_№2_-")
single_digits = range(10)
squares = []
for digits in single_digits:
    print(digits)
    x = digits**2
    squares.append(x)
print(squares)
cubes = [digits**3 for digits in single_digits]
print(cubes)