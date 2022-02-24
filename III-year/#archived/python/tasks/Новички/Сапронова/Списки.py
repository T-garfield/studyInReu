height = [['Sam', 67],['Vik', 68]]
age = [['Аарон', 15],['Дхрути', 16]]

Names=['Ben', 'Holly', 'Ann']
dogs_names= ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(Names, dogs_names)
print(list(names_and_dogs_names))

orders = ['маргаритки', 'барвинок']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)

orders =  ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
broken_prices = [5, 3, 4, 5, 4] + [4]

list1 = range(5, 16, 3)
list2 = range(0, 41, 5)
print(list(list2))

first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(0,4)

list1 = range (2, 20, 3)
list1_len = len(list1)
print(list1_len)

workers = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4 = workers[4]
print(len(workers))
print(workers[6])
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element,element5)

suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0: 4]
print(beginning)
middle = suitcase[2:4]

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed','dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'kingbed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[3:5]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()
