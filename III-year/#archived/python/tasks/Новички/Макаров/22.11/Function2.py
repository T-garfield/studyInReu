#1
def метод (основание, экспонента):
    степень = основание ** экспонента
    if степень >= 5000:
        return True
    else:
        return False
print(метод(25,3))
print("-------------------------------------------------------------")
#2
def range (num, low_limit, high_limit):
    if num >= low_limit and num <= high_limit:
        return True
    else:
        return False
print(range(2675672,2672342,26734272))
print("-------------------------------------------------------------")
#3
def names (your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
print(names('mike', 'nick'))

def len_names (your_name, my_name):
    if len(your_name) == len(my_name):
        return True
    else:
        return False
print(len_names('mickеy', 'nick'))
print("-------------------------------------------------------------")
#4
def z_4 (num):
    if num<8 and num>8:
        return True
    else: 
        return False
print(z_4(8))
print("-------------------------------------------------------------")
#5
def film (rating):
    if rating <= 5:
        return print("ИЗБЕГАТЬ ЛЮБОЙ ЦЕНОЙ!!!!!!!")
    elif rating < 9:
        return print("это было весело :)")
    else:
        return print("Отлично!")
(film(10))
print("-------------------------------------------------------------")
#6
def numbers(num1, num2, num3):
    if num1>num2 and num1>num3:
        return print('Выиграло первое число, вот оно: ' + str(num1))
    elif num1<num2 and num2>num3:
        return print('Выиграло второе число, вот оно: ' + str(num2))
    elif num1<num3 and num2<num3:
        return print('Выиграло третье число, вот оно: ' + str(num3))
    else:
        return print('Ничья!')
numbers(234575724,234285724,234275724)
print("-------------------------------------------------------------")
#7
def tenth_power(num):
    return num ** 10
import math
def square_root(num):
    return int(math.sqrt(num)) 
print(tenth_power(2), square_root(1024))
print("-------------------------------------------------------------")
#8
def games (win, lose):
    total = win + lose
    winning_ratio = (win/total)*100
    return winning_ratio
print ('Коэффициент выигрыша составляет ' + str(games(50,30)) + '%')
print("-------------------------------------------------------------")
#9
def намберс (num1, num2):
    намберс = (num1, num2)
    x = divmod(int(sum(намберс)), 2) 
    return x 
print(намберс(8.5,3))

def намберс (num1, num2):
    div = (num1 + num2)/2
    return div
print(намберс(3, 53))
print("-------------------------------------------------------------")
#10
def намберс (num1, num2):
    t = (num1 * 2)%(num2/2)
    return t
print(намберс(4.6,8))
print("-------------------------------------------------------------")
#11
def food(total, percent):
    return (total * percent)/100
print(food(1530, 20))
print("-------------------------------------------------------------")
#11(1)
def заголовок_функции(num):
    print(num, num*2, num*3)
    return print(num*3)
(заголовок_функции(4))
print("-------------------------------------------------------------")
#12
def calc (num1, num2, x):
        if x == "+":
            return print(num1+num2)
        elif x == "-":
            return print(num1-num2)
        elif x == "*":
                return print(num1*num2)
        elif x == "/":
            return print(num1/num2)
        else:
            return "вы ошибились! исправьтесь."
calc(3, 4, '/')
print("-------------------------------------------------------------")
#13
def game(pl1, pl2):
    if pl1 == "камень" and pl2 == "ножницы":
        return print("Игрок 1 победил")
    elif pl1 == "камень" and pl2 == "бумага":
        return print("Игрок 2 победил")
    elif pl1 == "ножницы" and pl2 == "бумага":
        return print("Игрок 1 победил")
    elif pl1 == "ножницы" and pl2 == "камень":
        return print("Игрок 2 победил")
    elif pl1 == "бумага" and pl2 == "ножницы":
        return print("Игрок 2 победил")
    elif pl1 == "бумага" and pl2 == "камень":
        return print("Игрок 1 победил")
    else:
        return print("Ничья")
game("ножницы", "бумага")
print("-------------------------------------------------------------")