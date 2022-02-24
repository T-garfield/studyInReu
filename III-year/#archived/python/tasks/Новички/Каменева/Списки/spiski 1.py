#Задание 1

sam_height = ['Сэм', 67, ['Вик', 68 ]]

age = [['Аарон', 15], ['Дхрути', 16]]

#Задание 2
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names )

print (list_of_names_and_dogs_names)

#Задание 3

orders = ['маргаритки', 'барвинок']

orders.append('тюльпаны')
orders.append('розы')

print(orders)


#Задание 4
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']

new_orders = orders + ['сирень', 'ирис']

broken_prices = [5, 3, 4, 5, 4] + [4]

#Задание 5
list1=range(9)
list2= range(8)

print(list(list2))

#Задание 6

list1 = range(5, 15, 3)
list2 = range(0, 40, 5)

print(list(list2))


#Задание 6

first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']

age = []

age.append( 42)

all_ages = [32, 41, 29] + age

name_and_age = zip(first_names, all_ages)

ids = range(0, 4)

print(list(name_and_age))