# 1
print((5 * 2) - 1 == 8 + 1)
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)
# 2
print()
my_baby_bool = "true"
print(my_baby_bool)
my_baby_bool_two = True
print(my_baby_bool_two)
# 3
print()
user_name = 'Ангелина'
Dmitriy = 'Дмитрий'
if user_name == Dmitriy:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
if user_name != Dmitriy:
    print('Добро пожаловать')
# 4
print()
enter_number = 2
if enter_number < 3:
    print('Попробуйте еще раз. У вас осталось', enter_number, 'попыток')
if enter_number >= 3:
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки')
# 5
print()
statement_one = (2 + 2 + 2) >= 6 and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

user_name = 'Дмитрий'
APM = 2
ARM = APM == 1 and user_name == "Дмитрий" or APM == 2 and user_name == "Ангелина" or APM == 3 and user_name == "Василий" or APM == 4 and user_name == "Екатерина"
if ARM == True:
    print('Добро пожаловать!')
if user_name != 'Дмитрий' and ARM == False:
    print('Логин  или пароль не верный, попробуйте еще раз')
if user_name == 'Дмитрий' and ARM == False:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
# 6
print()
print((2 - 1 > 3) or (-5 * 2 == - 10))
print((9+5 <= 15) or (7 != 4 + 3))
# 7
print()
user_name = 'Ангелина'
Dmitriy = 'Дмитрий'
if user_name == Dmitriy:
    print('Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
else:
    print('Добро пожаловать')
# 8
print()
score = 4
if score >= 4:
    print('A')
elif score >= 3:
    print('B')
elif score >= 2:
    print('C')
elif score >= 1:
    print('D')
elif score >= 0:
    print('F')

