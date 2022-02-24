#Задание1
sam_height = ['Сэм', 67];
#Задание2
v_heights = ['Вик', 68];
heights = [['Аарон', 15],['Дхрути', 16]]
#Задание3
names = ['Ben', 'Holly', 'Ann'];
dogs_names = ['Sharik','Gab','Beethoven'];
names_and_dogs_names = zip(names, dogs_names);
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
#Задание4
orders = ['маргаритки', 'барвинок']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)
#Задание5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень','ирис']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
#Задание6

list1 = range(10)
list1 = [x for x in list1 if not 1 <= x <= 8]
print(list(list1))
list2 = range(8)
print(list(list2))
#Задание7

list1 = range(6,15,3)
list2 = range(0,40,5)
#Задание8
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
print(list(all_ages))
name_and_age = zip(first_names, all_ages)
ids = range(4)


