#Задание 1
list1 = range (2, 20, 3)
list1_len = len(list1)
print(list1_len)

#Задание 2

Workers = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4 = Workers[4]

print(len(index4))
print(Workers[2])

#Задание 3

shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))

last_element = shopping_list[-1]
element5 = shopping_list[5]

print(last_element, element5)

#Задание 4
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0: 4]

print(beginning)

middle = suitcase[2:4]
print(middle)


suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']


start= suitcase[:3]

#Задание 5

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake',
'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

#Задание 6

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

#Задание 7

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)

print(games_sorted)
print(games)

#Задание 8
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed',
'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'kingbed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)

print(inventory_len)

first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]

twin_beds = inventory.count('twin bed')

inventory.sort()

print(first, last, inventory_2_6, twin_beds, inventory)
