if (((5*2) -1) == (8+1)):
    first = True
else:
    first = False

if ((13 - 6) != ((3*2) + 1)):
    second = True
else:
    second = False

if ((3*(2-1)) == (4-1)):
    third = True
else:
    third = False

print("first statement: ",first)
print("second statement: ",second)
print("third statement: ",third)
print("---------------------------------------------------------------------")

my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))
print("---------------------------------------------------------------------")

user_name_1 = "Дмитрий"
user_name_2 = "Ангелина"
Dmitry_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
user_check = "Добро пожаловать!"
if (user_name_1 == "Дмитрий"):
    print(Dmitry_check)
if (user_name_2 == "Ангелина"):
    print(user_check)
print("---------------------------------------------------------------------")

enter_number = 4
if (enter_number < 3):
    print("Попробуйте еще раз. У вас осталось", 3-enter_number, "попыток.")
if (enter_number >=3):
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")
print("---------------------------------------------------------------------")

if ((2+2+2>=6)and(-1*-1<0)):
    statement_one = True
else:
    statement_one = False

if (4*2<=8)and(7-1==6):
    statement_two = True
else:
    statement_two = False

print("Первое:",statement_one)
print("Второе:",statement_two)
print("---------------------------------------------------------------------")

Dmitry_ARM = 1
Angelina_ARM = 2
Vasily_ARM = 3
Ekaterina_ARM = 4
current_ARM = 3

if (current_ARM == Dmitry_ARM):
    print("Дмитрий, твоерабочее место находится в другой комнате. Отойди от чужого компьютера и займисьработой!")
elif (current_ARM == Angelina_ARM):
    print("Добро пожаловать!")
elif (current_ARM != Angelina_ARM):
    print("Логин или пароль не верный, попробуйте еще раз")
print("---------------------------------------------------------------------")

print((2-1>3)or(-5*2==-10))
print((9+5 <=15)or (7!=4+3))
print("---------------------------------------------------------------------")

print("Введите вашу оценку:")
grade = float(input())
if (grade >= 4.0):
    print("Your grade is A")
elif (grade >= 3.0):
    print("Your grade is B")
elif (grade >= 2.0):
    print("Your grade is C")
elif (grade >= 1.0):
    print("Your grade is D")
else:
    print("Your grade is F")