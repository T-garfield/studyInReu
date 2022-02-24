# 1
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list(list1))
print(list1_len)

# 2
print()
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element, element5)

# 3
print()
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:2]
print(beginning)
beginning = suitcase[0:4]
middle = suitcase[2:4]
print(middle)

# 4
print()
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'L aurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

# 5
print()
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Ever green Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

# 6
print()
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

# 7
print()
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', ' pillow']
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:5]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()