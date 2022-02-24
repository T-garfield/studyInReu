#task_1
sam_height = ["Сэм", 67]

#task_2
my_list = [['Вик', 68], ['Аарону', 15],['Дхрути',16]]

#task_3
Names=['Ben', 'Holly', 'Ann']
dogs_names= ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names =zip(Names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)

#task_4
orders = ['маргаритки', 'барвинок']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)

#task_5
new_orders= orders + ['сирень', 'ирис']
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
broken_prices = [5, 3, 4, 5, 4] + [4]

#task_6
list1 = range(9)
print(list(list1))
list2 = range(8)
print(list(list2))

#task_7
list1 = range(5, 15, 2)
list2 = range(0, 40, 5)
print(list(list1))
print(list(list2))

#task_8
first_names= ["Эйнсли", "Бен", "Чани", "Депак"]
age =[]
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(0, 4)
print(list(name_and_age))
print(list(ids))
