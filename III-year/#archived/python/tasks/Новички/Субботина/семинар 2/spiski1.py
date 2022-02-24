#1 
sam_height = ["Сэм", 67]

#2
heights = [ ["Сэм", 67], ["Вик", 68]]
age = [["Арон", 15], ["Дхрути", 16]]

#3
names = ["Ben", "Holly", "Ann"]
dogs_names = ["Sharik", "Gab", "Beethoven"]
names_and_dogs_names = zip(names, dogs_names)
print(list(names_and_dogs_names))

#4
orders = ["маргаритки", "барвинок"]
print(orders)
orders.append("тюльпаны")
orders.append("розы")
print(orders)

#5
orders = ["маргаритки", "лютик", "львиный зев", "гардения", "лилия"]
new_orders = orders +['сирень', 'ирис']
broken_prices = [5, 3, 4, 5, 4] + [4]
print(new_orders, broken_prices)

#6
list1 = range(9)
print(list(list1))
list2 = range(8)
print(list(list2))

#7
list1 = range (5, 15, 3)
print(list(list1))
list2 = range (0, 40, 5)
print(list(list2))

#8
first_names = ["Эйнсли", "Бен", "Чани", "Депак"]
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range (4)
name_and_age_and_ids = zip(first_names, all_ages, ids)
print(list(name_and_age_and_ids))
