#Матвеев
print('Какой вес посылки? В футах')
fut = int(input())
if fut <= 2:
	cost_lite = 20+fut*1.50
	cost_prem = 60
	cost_dron = fut*4.50

elif fut > 2 and fut <= 6:
	cost_lite = 20+fut*3
	cost_prem = 60
	cost_dron = fut*9	

elif fut > 6 and fut <=10:
	cost_lite = 20+fut*4
	cost_prem = 60
	cost_dron = fut*12

elif fut > 10:
	cost_lite = 20+fut*4.75
	cost_prem = 60
	cost_dron = fut*14.25
	
	
if cost_lite < cost_prem and cost_lite < cost_dron:
	final_cost = cost_lite
	name = "Обычная"
elif cost_dron < cost_lite and cost_dron < cost_prem:
	final_cost = cost_dron
	name = "Дрон"
elif cost_prem < cost_dron and cost_prem < cost_lite:
	final_cost = cost_prem
	name = "Премиум"
print(name)
print(final_cost)



