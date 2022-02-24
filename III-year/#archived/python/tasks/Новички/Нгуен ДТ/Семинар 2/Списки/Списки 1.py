# 1
sam_height = ["Сзм", 67]

# 2
vika = ['Vika', 68]
age = [['Аарону', 15], ['Дхрути', 16]]

# 3
print()
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(Names, dogs_names)
print(list(names_and_dogs_names))

# 4
print()
orders = ['маргариткиэ', 'барвинок']
print(orders)
orders.append('тюльпаны')
print(orders)
orders.append('розы')
print(orders)

# 5
print()
orders= ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
broken_pieces = [5, 3, 4, 5, 4] + [4]

# 6
print()
list1 = range(10)
print(list(list1))
list2 = range(8)
print(list(list2))

# 7
print()
list1 = range(5, 16, 3)
print(list(list1))
list2 = range(0, 41, 5)
print(list(list2))

# 8
print()
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)
all_ages = [32, 41, 29]
all_ages = all_ages + age
name_and_age = zip(first_names, all_ages)
ids = range(4)
print(list(name_and_age))
print(list(ids))