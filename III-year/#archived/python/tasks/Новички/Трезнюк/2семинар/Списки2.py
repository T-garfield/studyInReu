#Задание 1
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)
#Задание 2
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
#Задание 3
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0:2]
print(len(beginning))
beginning = suitcase [0:4]
middle = suitcase[2:4]
#Задание 4
votes = ['Jake', 'Jake', 'Laurie','Laurie','Laurie','Jake','Jake','Jake','Laurie','Cassie','Cassie','Jake','Jake','Cassie','Laurie','Cassie','Jake','Jake','Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)
#Задание 5
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)
#Задание 6
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)
#Задание 7
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed',
'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:7]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()
