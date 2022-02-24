print("*** Задание 1 ***")
sam_height = ['Сэм', 67]
print(sam_height)

print("\n*** Задание 2 ***")
vik = ['Вик', 68]
age = [['Аарон', 15], ['Дхруть', 16]]
print(vik)
print(age)

print("\n*** Задание 3 ***")
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

print("\n*** Задание 4 ***")
orders = ['маргаритки', 'барвинок']
orders.append('тюльпаны')
orders.append('розы')
print(orders)

print("\n*** Задание 5 ***")
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

print("\n*** Задание 6 ***")
list1 = range(9)
print(list(list1))
list2 = range(8)
print(list(list2))

print("\n*** Задание 7 ***")
list1 = range(5, 15 ,3)
print(list(list1))
list2 = range(0, 40, 5)
print(list(list2))

print("\n*** Задание 8 ***")
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(4)
name_and_age_and_id = zip(first_names, all_ages, ids)
print(list(name_and_age_and_id))
