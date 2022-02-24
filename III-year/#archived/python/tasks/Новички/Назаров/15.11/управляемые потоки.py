import random #для посл задачи
#1
b=(5*2)-1==8+1
b1=13-6!=(3*2)+1
b2=3*(2-1)==4-1
print(b, b1, b2)
#2
my_baby_bool_two=True
print(type(my_baby_bool_two))
#3
user_name=input()
Dmitry_check='Дмитрий, твое рабочее место находится в другойкомнате. Отойди от чужого компьютера и займись работой!'
welcome='Добро пожаловать'
if user_name=='Дмитрий':
    print(Dmitry_check)
if user_name!='Дмитрий':
    print(welcome)
#4
enter_number=int(input())
if enter_number<3:
    print(f'«Попробуйте еще раз. У вас осталось {3-enter_number} попыток»')
else: 
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.')
#5
statement_one=(2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two=(4 * 2 <= 8) and (7 - 1 == 6)

user_name=input('Введите имя:Дмитрий, Ангелина, Василий, Екатерина')
arm=int(input('Введите ARM от 1 до 4'))
Dmitry_check='Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
welcome='Добро пожаловать!'
error='Логин или пароль не верный, попробуйте еще раз'
if user_name=='Дмитрий' and arm==1:
    print(welcome)
if user_name=='Дмитрий' and arm!=1:
    print(Dmitry_check)
if user_name=='Ангелина' and arm==2:
    print(welcome)
if user_name=='Ангелина' and arm!=2:
    print(error)
if user_name=='Василий' and arm==3:
    print(welcome)
if user_name=='Василий' and arm!=3:
    print(error)
if user_name=='Екатерина' and arm==4:
    print(welcome)
if user_name=='Екатерина' and arm!=4:
    print(error)

print(statement_one, statement_two)

#6
x=((2 - 1 > 3) or (-5 * 2 == -10))
y=((9 + 5 <= 15) or (7 != 4 + 3))
print(x, y)

#7
user_name=input('Введите имя:Дмитрий, Ангелина, Василий, Екатерина')
arm=int(input('Введите ARM от 1 до 4'))
Dmitry_check='Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
welcome='Добро пожаловать!'
error='Логин или пароль не верный, попробуйте еще раз'
if user_name=='Дмитрий' and arm==1 or user_name=='Ангелина' and arm==2 or user_name=='Василий' and arm==3 or user_name=='Екатерина' and arm==4 :
    print(welcome)
elif user_name=='Дмитрий' and arm!=1:
    print(Dmitry_check)
else: 
    print(error)

#8


grade=random.uniform(0.0,5.0)
print(grade)
if grade>=4.0:
    print('Студент получил А')
elif grade>=3.0:
    print('Студент получил B')
elif grade>=2.0:
    print('Студент получил С')
elif grade>=1.0:
    print('Студент получил D')
else:
    print('Студент получил F')


