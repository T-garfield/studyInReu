#1
list1 = range (2, 20, 2)
print(list(list1))
list1_len = (len(list1))
#изменим range (2, 20, 2) на range (2, 20, 3)
new_list1 = range (2, 20, 3)
print(list(new_list1))
new_list1_len = (len(new_list1))
# длина списка сократилась на 3 единицы
print ('Длина списка изменилась на', list1_len-new_list1_len, "единицы")
print("...................................................")
#2
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(index4)
print(len(employees))
print(employees[2])
print("...................................................")
#2(1)
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
last_element = print(shopping_list[-1])
element5 = print(shopping_list[5])
print("...................................................")
#4
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 
'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake','Jake', 'Cassie', 'Laurie']
num_i = print(votes.count('Jake'))
print("...................................................")
#5(1)
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)
print("...................................................")
#5(2)
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
sorted_games = sorted(games)
print(sorted_games)
print("...................................................")