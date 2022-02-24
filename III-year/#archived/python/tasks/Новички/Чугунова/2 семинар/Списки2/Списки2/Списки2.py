#Задание1
list1 = range (2, 20, 2)
list1_len = len(list1)
print(list1_len)
list1 = range (2, 20, 3)
list1_len = len(list1)
print(list1_len)
#Задание2
employees = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4 = employees[4]
print(len(employees))
print(employees[6])

#Задание3
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5)
print(last_element)

#Задание4
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0: 2]
print(beginning)
print(len(beginning))
beginning = suitcase [0: 5]
middle = suitcase[2:4]
print(middle)

#Задание5
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
print(start)

#Задание6
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

#Задание7
ddresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
ddresses.sort()
print(ddresses)
#Задание8
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)
#Задание9
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
print(inventory_len)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:7]
print(inventory_2_6)
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()
