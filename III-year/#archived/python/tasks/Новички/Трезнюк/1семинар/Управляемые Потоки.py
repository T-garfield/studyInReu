#Задача 1
print((5 * 2) - 1 == 8 + 1)
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 -1)
#Задача 2
my_baby_bool = "true"
my_baby_bool_two = True
print(type(my_baby_bool))
print(type(my_baby_bool_two))
#Задача 3
user_name = input('Введите имя: ')
Dmitriy_check = 'Дмитрий'
greeting = 'Добро пожаловать'
if user_name == Dmitriy_check:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
if user_name != Dmitriy_check:
    print(greeting)
#Задача 4
enter_number = 1
if enter_number < 3:
    print(f'Попробуйте еще раз. У вас осталось {3 - enter_number} попыток')
else:
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.')
#Задача 5
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statemetn_two = (4 * 2 <= 8) and (7 - 1 == 6)
num = 0 
ARM = num == 1 and user_name == "Дмитрий" or num == 2 and user_name == "Ангелина" or num == 3 and user_name == "Василий" or num == 4 and user_name == "Екатерина"
if ARM:
    print(greeting)
elif not(ARM) and user_name == "Дмитрий":
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
elif not(ARM) and user_name != "Дмитрий":
    print('Логин или пароль неверный, попробуйте еще раз')
#Задача 6
print((2 - 1 > 3) or (-5 * 2 == - 10))
print((9 + 5 <= 15) or (7 != 4 + 3))
#Задача 7
if user_name == Dmitriy_check:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
else:
    print(greeting)
#Задача 8
grade = float(input('Enter grade: '))
if grade >= 4:
    print('A')
elif grade >= 3 and grade < 4:
    print('B')
elif grade >= 2 and grade < 3:
    print('C')
elif grade >= 1 and grade < 2:
    print('D')
elif grade >= 0 and grade < 1:
    print('F')
else:
    print('неверный grade')