#Матвеев
print('Введите возраст авто:')
age = int(input())
if age >=3:
	print('Введите объем двигателя:')
	V = int(input())
print('Введите количество куб. см.:')
kub = int(input())

if age <3:
	print('Введите стоимость авто:')
	cost = int(input())
	if cost < 8500:
		result_cost = 2.5*kub
	elif cost >= 8500 and cost < 16700:
		result_cost = 3.5*kub
	elif cost >= 16700 and cost < 42300:
		result_cost = 5.5*kub
	elif cost >= 42300 and cost < 84500:
		result_cost = 7.5*kub
	elif cost >= 84500 and cost < 169000:
		result_cost = 15*kub
	elif cost >= 169000:
		result_cost = 20*kub
elif age>=3:
	if V < 1000:
		result_cost = 1.5*kub
	elif V >= 1000 and cost < 1500:
		result_cost = 1.7*kub
	elif V >= 1500 and cost < 1800:
		result_cost = 2.5*kub
	elif V >= 1800 and cost < 2300:
		result_cost = 2.7*kub
	elif V >= 2300 and cost < 3000:
		result_cost = 3*kub
	elif V >= 3000:
		result_cost = 3.6*kub

print('Таможенные отчисления на ваш автомобиль составят', result_cost)