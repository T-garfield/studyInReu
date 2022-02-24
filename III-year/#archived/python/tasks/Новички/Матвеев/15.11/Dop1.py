#Матвеев
print('Введите средний расход в час: ')
kol = int(input())
print('Введите количество дней: ')
dney = int(input())
print('У вас электрическая плита? Да/нет:')
El = input()
if El == 'Да':
	El = True
else: 
	El = False
#Средний объем электроэнергии в час
ET1 = 6.18
ET3 = 5.15
ET2 = 1.74
GT1 = 6.18
GT3 = 5.92
GT2 = 7.10
#T1 7часов T3 9часов T2 8часов
if (dney == 28) and El == True:
	result_calc = kol*28*(ET1*7+ET3*9+ET2*8)
elif (dney == 28) and El == False:
	result_calc = kol*28*(GT1*7+GT3*9+GT2*8)
elif (dney == 29) and El == True:
	result_calc = kol*29*(ET1*7+ET3*9+ET2*8)
elif (dney == 29) and El == False:
	result_calc = kol*29*(GT1*7+GT3*9+GT2*8)
elif (dney == 30) and El == True:
	result_calc = kol*30*(ET1*7+ET3*9+ET2*8)
elif (dney == 30) and El == False:
	result_calc = kol*30*(GT1*7+GT3*9+GT2*8)
elif (dney == 31) and El == True:
	result_calc = kol*31*(ET1*7+ET3*9+ET2*8)
elif (dney == 31) and El == False:
	result_calc = kol*31*(GT1*7+GT3*9+GT2*8)

print('Сумма оплаты за электроэнергию составила:', result_calc) 
