#Задание_1
my_baby_bool = 'true'
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))
print()

#Задание_2
user_name = 'Дмитрий'
Dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
another_user = 'Добро пожаловать, '
if user_name =='Дмитрий':
    print(Dmitriy_check)
else:
    print(another_user)

user_name = 'Ангелина'
if user_name =='Дмитрий':
    print(Dmitriy_check)
else:
    print(another_user + user_name)
print()

#Задание_2
enter_number = 1
if enter_number < 3:
    print(f'Попробуйте еще раз. У вас осталось {3 - enter_number} попыток')
else:
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки')

#Задание_3
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_one)
print(statement_two)
print()

user_name = input('Ваше имя: ')
user_arm = int(input('Ваш АРМ: '))
if (user_name == 'Дмитрий' and user_arm == 1) or (user_name == 'Ангелина' and user_arm == 2) or (user_name == 'Василий' and user_arm == 3) or (user_name == 'Екатерина' and user_arm == 4):
    print('Добро пожаловать!')
elif (user_name == 'Ангелина' and user_arm != 2) or (user_name == 'Василий' and user_arm != 3) or (user_name == 'Екатерина' and user_arm != 4):
    print('Логин или пароль не верный, попробуйте еще раз')
elif (user_name == 'Дмитрий' and user_arm != 1):
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')

#Задание_4
print((2 - 1 > 3) or (-5 * 2 == -10))
print((9 + 5 <= 15) or (7 != 4 + 3))
print()

#Задание_5 Уже с else

#Задание_6
grade = float(input('Ваша оценка: '))
if grade >= 4.0:
    print ('A')
elif grade >= 3.0:
    print ('B')
elif grade >= 2.0:
    print ('C')
elif grade >= 1.0:
    print ('D')
elif grade >= 0.0:
    print ('F')
print()

#Задание_6
a = int(input('Число a: '))
b = int(input('Число b: '))

try:
 result = a / b
 print (result)
except ZeroDivisionError:
 print ("Can't divide by zero!")