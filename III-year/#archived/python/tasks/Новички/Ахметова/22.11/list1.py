#Задание_1
sam_height = ['Сэм', 67]
print(sam_height)
print()

#Задание_2
heights = [['Сэм', 67], ['Вик', 68]]
ages = [['Аарон', 15], ['Дхрути', 16]]
print(heights, ages)
print()

#Задание_3
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(Names, dogs_names)
print(list(names_and_dogs_names))
print()

#Задание_4
orders = ['маргаритки', 'барвинок']
orders.append('тюльпаны')
orders.append('розы')
print(orders)
print()

#Задание_5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
broken_prices = [5, 3, 4, 5, 4] + [4]
print(new_orders)
print(broken_prices)
print()

#Задание_6
list1 = range(10)
print(list(list1))
list2 = range(8)
print(list(list2))
print()

#Задание_7
list1 = range(5, 15, 3)
print(list(list1))
list2 = range(0,40,5)
print(list(list2))
print()

#Задание_8
first_names = ["Эйнсли","Бен","Чани","Депак"]
age = []
age.append(42)
all_ages = [32,41,29] + age
ids = range(0,4)
name_and_age = zip(first_names, all_ages, ids)
print(list(name_and_age))