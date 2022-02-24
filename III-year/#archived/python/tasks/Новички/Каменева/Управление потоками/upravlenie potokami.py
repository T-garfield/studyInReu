my_baby_bool = "true"

print(my_baby_bool)

my_baby_bool_two = True

print(my_baby_bool_two)

#задание 2
user_name ="Ангелина"
greetings ="Добро пожаловать!" 

Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"


user_name ="Ангелина"
if user_name=="Ангелина":
   print(greetings)


user_name ="Дмитрий"
if user_name=="Дмитрий":
  print(Dmitriy_check)

#задание 3
  enter_number = 1

  if enter_number < 3:
      print("Попробуйте еще раз. У вас осталось ( ",3 - enter_number , "попыток)")

  enter_number = 4

  if enter_number >= 3:
      print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки")

#задание 4
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

print(statement_one)
print(statement_two)



APM = 1
user_name = "Ангелина"

ARM = APM == 1 and user_name == "Дмитрий" or APM == 2 and user_name =="Ангелина" or APM == 3 and user_name =="Василий" or APM == 4 and user_name =="Екатерина"

if ARM == True:
  print(" Добропожаловать!")

if  ARM != True and user_name != "Дмитрий":
  print("Логин или пароль не верный, попробуйте еще раз")

if  ARM != True and user_name == "Дмитрий":
  print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")  


#задание 5

stat1 = (2 - 1 > 3) or (-5 * 2 == -10)
stat2 =(9 + 5 <= 15) or (7 != 4 + 3)

print(stat1, stat2)

#задание 6

APM = 2
user_name = "Дмитрий"

ARM = APM == 1 and user_name == "Дмитрий" or APM == 2 and user_name =="Ангелина" or APM == 3 and user_name =="Василий" or APM == 4 and user_name =="Екатерина"

if ARM == True:
  print(" Добропожаловать!")
else:  print("Логин или пароль не верный, попробуйте еще раз")

if  ARM != True and user_name == "Дмитрий":
  print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")  


#задание 7  

grade = 2.1

if grade >=4:
  print("A")
elif grade >=3:
  print("B")
elif grade >=2:
  print("C")
elif grade >=1:
  print("D")  
else :
  print("F")      