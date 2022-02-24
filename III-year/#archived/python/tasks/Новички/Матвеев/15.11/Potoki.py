#Матвеев
#Вопрос. '7' == 7 неверно, потому что первое строковый тип, а второе целочисленный
print('Задание 1')
a = (5*2)-1 == 8+1
print(a)
b = 13-6 != (3*2)+1
print(b)
c = 3*(2-1) == 4-1
print(c)
print()
print('Задание 2')
my_baby_bool = "true"
print( my_baby_bool)
my_baby_bool_two = True
print( my_baby_bool_two)
print()
print('Задание 3')
user_name = "Дмитрий"
dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
all_check = "Добро пожаловать"
if user_name == "Дмитрий":
	print(dmitriy_check)
else:
   print(all_check)
print()
print('Задание 3')
enter_number = 3
if enter_number < 3:
	print('Попробуйте еще. У вас осталось', 3 - enter_number, 'попыток')
else:
	print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки')
print()
print('Задание 4')
a = (2-1>3) or (-5*2 == -10)
print(a)
a = (9+5<=15) or (7 != 4+3)
print(a)
print()
print('Задание 5')
grade = 2.3
if grade >= 4.0:
	print("A")
elif grade >= 3.0:
	print("B")
elif grade >= 2.0:
	print("C")
elif grade >= 1.0:
	print("D")
elif grade >= 0.0:
	print("F")







