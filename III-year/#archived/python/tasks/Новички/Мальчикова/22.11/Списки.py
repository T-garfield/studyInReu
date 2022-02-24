#Списки 1
print("*Списки 1*")
print("")
#Что такое списки
print("-_Что такое списки_-")
sam_height = ['Сэм', 67]
print("")

#Список списков
print("-_Список списков_-")
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
age = [['Aaron', 15], ['Dhruti', 16]]
print("")

#zip
print("-_zip_-")
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(names, dogs_names)
print(list(names_and_dogs_names))
print("")


#Расширение списка_append
print("-_Расширение списка_append_-")
orders = ['маргаритки', 'барвинок']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)
print("")

#Расширение списка_плюс
print("-_Расширение списка_плюс_-")
orders = ['маргаритки', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders +['сирень', 'ирис']
broken_prices = [5, 3, 4, 5, 4] + [4]
print(new_orders, broken_prices)
print("")

#Range
print("-_Range_-")
list1 = range(1,9)
print(list(list1))
list2 = range(8)
print(list(list2))
print("")

list1 = range (5, 16, 3)
print(list(list1))
list2 = range (0, 41, 5)
print(list(list2))
print("")

#Заключительное задание
print("-_Заключительное задание_-")
first_names = ['Ainsley', 'Ben', 'Chani', 'Deepak']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range (4)
name_and_age_and_ids = zip(first_names, all_ages, ids)
print(list(name_and_age_and_ids))
print("")
print("")
print("")


#Списки 2
print("*Списки 2*")
#Выбор элементов списка
print("-_Выбор элементов списка_-")
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(index4)
print(len(employees))
print(employees[2])
print("")

shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
last_element = print(shopping_list[-1])
element5 = print(shopping_list[5])
print("")

#Длинна списка
print("-_Длинна списка_-")
list1 = range (2, 20, 2)
print(list(list1))
list1_len = (len(list1))
#изменим range (2, 20, 2) на range (2, 20, 3)
new_list1 = range (2, 20, 3)
print(list(new_list1))
new_list1_len = (len(new_list1))
#длина списка уменьшилась на 3 единицы
print ('Длина списка уменьшилась на', list1_len-new_list1_len, "единицы")
print("")

#Заключение
print("-_Заключение_-")
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed',
'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'kingbed', 
'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = print(len(inventory))
first = print(inventory[:1])
last = print(inventory[-1:])
inventory_2_6 = print(inventory[2:6])
first3 = print(inventory[:3])
twin_beds = print(inventory.count("twin bed"))
sorted_inventory = (inventory.sort())
print("")

#Подсчёт элементов в списке
print("-_Подсчёт элементов в списке_-")
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 
'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake','Jake', 'Cassie', 'Laurie']
num_i = print(votes.count('Jake'))
print("")

#Сортировка списков
print("-_Сортировка списков_-")
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)
print("")

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
sorted_games = sorted(games)
print(sorted_games)
print("")