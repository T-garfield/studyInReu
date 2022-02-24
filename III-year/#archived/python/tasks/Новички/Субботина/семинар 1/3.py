#1 задание (true/false)
answer1 =  (5 * 2) - 1 == 8 + 1
print (answer1)
answer2 = 13 - 6 != (3 * 2) + 1 
print (answer2)
answer3 = 3 * (2 - 1) == 4 - 1
print (answer3)

#2 задание 
my_baby_bool = True
print (type(my_baby_bool))
my_baby_bool_two = True
print (type(my_baby_bool_two))

#3 задание (if)
user_name = input()
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
check = "Добро пожаловать!"
if user_name == "Дмитрий":
    print (Dmitriy_check)
if user_name == "Ангелина":
    print (check)

#4 задание (больше/меньше)
enter_number = 3
if enter_number <= 3:
    print ( f'Попробуйте еще раз. У вас осталось {3-enter_number} попыток.')
if enter_number > 3:
    print ("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

#5 задание (and)
ans1 = (2 - 1 > 3) or (-5 * 2 == -10)
print (ans1)

#5 задание (and)
ARM = input()
user_name = input()
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
check = "Добро пожаловать!"
if (user_name == "Дмитрий") and (ARM == 1): print (check)
if (user_name == "Ангелина") and (ARM == 2): print (check)
if (user_name == "Василий") and (ARM == 3): print (check)
if (user_name == "Екатерина") and (ARM == 4): print (check)
if (user_name == "Дмитрий") and (ARM > 1): print (Dmitriy_check)
else : print("Логин или пароль не верный, попробуйте еще раз")

answer = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print (answer)
answer1 = (4 * 2 <= 8) and (7 - 1 == 6)
print (answer1)

#6 задание (or)
ans1 = (2 - 1 > 3) or (-5 * 2 == -10)
print (ans1)
ans2 = (9 + 5 <= 15) or (7 != 4 + 3)
print (ans2)

#7 задание (else)
user_name = input()
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
check = "Добро пожаловать!"
if user_name == "Дмитрий":
    print (Dmitriy_check)
else:
    print (check)
    
#8 задание (else/if)
grade = input()
if grade >= 4: 
    print("A")
elif grade >= 3: 
    print("B")
elif grade >= 2: 
    print("C")
elif grade >= 1: 
    print("D")
else: print("F")


