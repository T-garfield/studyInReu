#1
list1 = range (2, 20, 2)
print(len(list1))
list1 = range (2, 20, 3) #len изменится на 3
print(len(list1))
#2
calls=['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4=calls[4]
print(len(calls))
print(calls[5]) 
#3
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья'] 
print(len(shopping_list))
last_element=shopping_list[-1]
element5=shopping_list[5]
print(element5,last_element)
#4
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги'] 
beginning = suitcase [0: 2]
print(beginning)
beginning = suitcase [0: 4]
print(beginning)
middle = suitcase [2: 4]
print(middle)
#5
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake',
 'Jake', 'Cassie', 'Laurie'] 
jake_votes=votes.count('Jake')
print(jake_votes)
#6
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.'] 
addresses.sort()
print(addresses)
#7
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon'] 
games_sorted=sorted(games)
print(games)
print(games_sorted)
#8
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed',
 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'kingbed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len=len(inventory)
first=inventory[0]
last=inventory[-1]
inventory_2_6= inventory[2:6]
first_3=inventory[:3]
twin_beds=inventory.count('twin bed')
inventory.sort()
print(inventory)
print(twin_beds)