#task_1
print((5 * 2) - 1 == 8 + 1)
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)

#task_2
my_baby_bool = "true"
my_baby_bool_two = True
print(type(my_baby_bool))
print(type(my_baby_bool_two))

#task_3
user_name = input('Введите имя: ')
Dmitriy_check = 'Дмитрий'
greeting = 'Добро пожаловать'
if user_name == Dmitriy_check:
    print('Дмитрий, твое рабочее место находится в другой комнате.')
if user_name != Dmitriy_check:
    print(greeting)

#task_4
enter_number = int(input())
if enter_number < 3:
   print("Попробуйте еще раз. У вас осталось",3-enter_number,"попыток.")
else: print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

#task_5
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome = "Добро пожаловать "
user_name="Дмитрий"
АРМ1="Дмитрий"
АРМ2="Ангелина"
АРМ3="Василий"
АРМ4="Екатерина"
APM=АРМ4
if user_name=="Дмитрий" and APM!="Дмитрий":
    print(Dmitriy_check)
    if APM==user_name:
        print(welcome+user_name)
    else:
        print("Логин или пароль не верный, попробуйте еще раз")

#task_6
print((2 - 1 > 3) or (-5 * 2 == - 10))
print((9 + 5 <= 15) or (7 != 4 + 3))

#task_7
if user_name == Dmitriy_check:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
else:
    print(greeting)

#task_8
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