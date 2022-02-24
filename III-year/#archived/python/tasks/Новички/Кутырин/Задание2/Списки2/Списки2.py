list1 = range (2, 20, 2)
list1_len = len(list1)
print(list1_len)

list1 = range (2, 20, 3)
list1_len = len(list1)
print(list1_len)

shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element, element5)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0: 2]

print(beginning)
print(len(beginning))

beginning = suitcase [0: 4]
print(beginning)

middle = suitcase [2: 4]
print(middle)

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 
         'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake','Jake', 'Cassie', 'Laurie']

jake_votes = votes.count("Jake")
print(jake_votes)

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place',
            '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
gemes_sorted = sorted(games)
print(gemes_sorted)


inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed',
'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'kingbed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:2]
twin_beds = inventory.count('twin bed')
inventory.sort
print(inventory)