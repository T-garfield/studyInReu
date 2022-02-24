dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
 print(breed)


board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
 print(game)
for sport in sport_games:
 print(sport)

promise = "I will not chew gum in class"

for i in range(5):
 print(promise)

student_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
student_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in student_period_A:
 student_period_B.append(student)
 print(student)

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
 print(dog)
 if dog == dog_breed_I_want:
  print("У них есть собака, которую я хочу!")
  break

#задание 1
scoops_sold = 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for data in sales_data:
 for d in data:
  scoops_sold = scoops_sold + d
print(scoops_sold)

#задание 2
single_digits = range(10)
squares = []
for digit in single_digits:
 print(digit)
 c = digit*digit
 squares.append(c)

print(squares)

cubes = [digit*digit*digit for digit in single_digits]
print(cubes)