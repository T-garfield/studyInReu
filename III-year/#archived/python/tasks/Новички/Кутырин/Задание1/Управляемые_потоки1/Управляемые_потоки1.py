

print((5 * 2) - 1 == 8 + 1)
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)


my_baby_bool= True
print(my_baby_bool)
my_baby_bool_two= True
print(my_baby_bool_two)

user_name="Дмитрий"
Dmitriy_check= "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome="Добро пожаловать "
if user_name=="Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome+user_name)

user_name="Ангелина"
if user_name=="Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome+user_name)



enter_number=3
if enter_number<=3:
    print("Попробуйте еще раз. У вас осталось", (3- enter_number), "попыток")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки")


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


APM=АРМ4
user_name="Екатерина"

if user_name=="Дмитрий" and APM!="Дмитрий":
    print(Dmitriy_check)
    if APM==user_name:
        print(welcome+user_name)
    else:
        print("Логин или пароль не верный, попробуйте еще раз")


print((2 - 1 > 3) or (-5 * 2 == -10))
print((9 + 5 <= 15) or (7 != 4 + 3))

grade=3
if grade >=4:
    print("A")
elif grade>=3:
    print("B")
elif grade>=2:
    print("C")
elif grade>=1:
    print("D")
elif grade>=0.0:
    print("F")