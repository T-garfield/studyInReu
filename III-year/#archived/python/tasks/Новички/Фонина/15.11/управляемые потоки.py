print("Task #1 - Проверка на True и False")
#задание1
if ((5*2)-1 == (8+1)):
    first = True
else: first = False

#задание2
if ((13-6)!=((3*2)+1)):
    second = True
else: second = False

#задание3
if ((3*(2-1))==(4-1)):
    third = True
else: third = False

#подводим итог наших выражений
print("First is", first)
print("Second is", second)
print("Third is", third)

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #2 - my_baby_bool")
#Создаем строковый элемент
my_baby_bool="true"
print(type(my_baby_bool))

#Создаем уже логическую переменную
my_baby_bool_two=True
print(type(my_baby_bool_two))

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #3 - Проверка user_name")
user_name_1 = "Дмитрий"
user_name_2 = "Ангелина"
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
user_check = "Добро пожаловать!"
if (user_name_1 == "Дмитрий"):
    print(Dmitriy_check)
if (user_name_2 == "Ангелина"):
    print(user_check)

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #4 ")
enter_number = 4
if (enter_number<3):
    print("Попробуйте еще раз! У вас осталось ",(3 -enter_number), "попыток")
if (enter_number>3):
    print ("Вы превысили максимальное число попыток! Ваша учетная запись заблокирвоана. Для разблокировки обратитесь в службу поддержки.")

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #5 ")
if ((2+2+2>=6) and (-1*-1<0)):
    statement_one=True
else: statement_one=False

if ((4*2<=8) and (7-1==6)):
    statement_two = True
else: statement_two = False

print("")

print("First:", statement_one)
print("Second:", statement_two)
print("")

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #3.1 ")
Dmitriy_ARM = 1
Angelina_ARM=2
Vasiliy_ARM=3
Kate_ARM=4
ARM=3

if (ARM==Dmitriy_ARM):
    print ("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
elif (ARM== Angelina_ARM):
    print ("Логин или пароль не верный! Попробуйте еще раз.")
elif (ARM== Vasiliy_ARM):
    print ("Добро пожаловать!")

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #4")
print ((2-1>3) or (-5*2 ==-10))
print((9+5<=15) or (7!=4+3))

print("" , "\n", "_____________________________________________",  "\n", "")

print("Task #5")
print("Введите Вашу оценку:")
grade = float(input())

if (grade>=4.0):
    print ("Ваша оценка A")
elif (grade>=3.0):
    print ("Ваша оценка B")
elif (grade>=2.0):
    print ("Ваша оценка C")
elif (grade>=1.0):
    print("Ваша оценка D")
elif (grade>=0.0):
    print ("Ваша оценка F")