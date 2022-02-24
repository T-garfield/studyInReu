print("*** Задание 1 ***")
print((5 * 2) - 1 == 8 + 1)
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)

print("\n*** Задание 2 ***")
my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

print("\n*** Задание 3 ***")
print("Пользователь: ")
user_name = str(input())
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
welcome = "Добро пожаловать!"
if user_name == "Дмитрий" :
   print(Dmitriy_check)
else: print(welcome)

print("\n*** Задание 4 ***")
enter_number = int(input())
if enter_number < 3:
   print("Попробуйте еще раз. У вас осталось",3-enter_number,"попыток.")
else: print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

print("\n*** Задание 5.1 ***")
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_one)
print(statement_two)

print("\n*** Задание 5.2 ***")
print("Пользователь: ")
user_name = str(input())
print("APM: ")
APM = int(input())
if user_name == "Дмитрий" and APM == 1:
   print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
elif user_name == "Ангелина" and APM == 2:
   print("Добро пожаловать!")
elif user_name == "Василий" and APM == 3:
   print("Добро пожаловать!")
elif user_name == "Екатерина" and APM == 4:
   print("Добро пожаловать!")
else: print("Логин или пароль не верный, попробуйте еще раз.")

print("\n*** Задание 6 ***")
print((2 - 1 > 3) or (-5 * 2 == -10))
print((9 + 5 <= 15) or (7 != 4 + 3))

print("\n*** Задание 7 ***")
print("Пользователь: ")
user_name = str(input())
print("APM: ")
APM = int(input())
if user_name == "Дмитрий" and APM == 1:
   print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
elif user_name == "Ангелина" and APM == 2:
   print("Добро пожаловать!")
elif user_name == "Василий" and APM == 3:
   print("Добро пожаловать!")
elif user_name == "Екатерина" and APM == 4:
   print("Добро пожаловать!")
else: print("Логин или пароль не верный, попробуйте еще раз.")

print("\n*** Задание 8 ***")
print("Средний балл: ")
grade = float(input())
if grade >= 4.0:
   print("Грейд: A")
elif grade >= 3.0:
   print("Грейд: B")
elif grade >= 2.0:
   print("Грейд: C")
elif grade >= 1.0:
   print("Грейд: D")
else: print("Грейд: F")