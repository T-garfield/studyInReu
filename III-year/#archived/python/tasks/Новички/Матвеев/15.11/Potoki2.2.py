#Матвеев
manager_num = 1
kol = 2
one = True
two = True
three = True
boss = True

if (one == True) and (two == True) and (three == True) and (boss == True):
	manager_num = 1
elif (one == False) and (two == True) and (three == True) and (boss == True):
	manager_num = 2
elif (one == True) and (two == False) and (three == True) and (boss == True):
	manager_num = 3
elif (one == False) and (two == False) and (three == True) and (boss == True):
	manager_num = 3
elif (one == True) and (two == False) and (three == False) and (boss == True):
	manager_num = 1
elif (one == False) and (two == True) and (three == False) and (boss == True):
	manager_num = 2
elif (one == True) and (two == True) and (three == False) and (boss == True):
	manager_num = 1
elif (one == False) and (two == False) and (three == False) and (boss == True) and (kol<2):
	manager_num = "Ожидание оператора"
elif (one == False) and (two == False) and (three == False) and (boss == True) and (kol >= 2):
	manager_num = "Главный менеджер"

print('Ваш менеджер -', manager_num)

