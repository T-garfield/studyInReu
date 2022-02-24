#Задание1
print((5 * 2) - 1 == 8 + 1);
print(13 - 6 != (3 * 2) + 1);
print(3 * (2 - 1) == 4 - 1);

#Задание2
my_baby_bool = 'true';
print(type(my_baby_bool));
my_baby_bool_two = True;
print(type(my_baby_bool_two));

#Задание3
user_name = 'Дмитрий';
Dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!';
hey = 'Добро пожаловать';
user_name = 'Ангелина';
if user_name: print(Dmitriy_check);
if user_name != 'Дмитрий' : print(hey);

#Задание4
enter_number = 2;
if enter_number < 3:print( 'Попробуйте еще раз. У вас осталось', ( 3- enter_number),' попыток');
if enter_number >= 3:print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки')

#Задание5
print((2 + 2 + 2 >= 6) and (-1 * -1 < 0));
print((4 * 2 <= 8) and (7 - 1 == 6));
statement_one = False;
statement_two = True;

#Задание6
APM = 1
user_name = 'Екатерина'

ARM = APM == 1 and user_name == "Дмитрий" or APM == 2 and user_name =="Ангелина" or APM == 3 and user_name =="Василий" or APM == 4 and user_name =="Екатерина"

if ARM == True:
    print("Добро пожаловать!")

if ARM != True and user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")

if ARM != True and user_name == "Дмитрий":
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

#Задание7
print((2 - 1 > 3) or (-5 * 2 == -10));
print((9 + 5 <= 15) or (7 != 4 + 3));

#Задание8
user_name = 'Дмитрий'
if user_name == 'Дмитрий':
   print( 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!')
else: 
   print( "Добро пожаловать!")

#Задание9
grade = 5.0
if grade >= 4.0:
    print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0: 
    print("C")
elif grade >= 1.0: 
    print("D")
elif grade >= 0.0: 
    print("D")