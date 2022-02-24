import math
#для 7 задачи
# Задача 1
def exp(base_num, exp_num):
    num = base_num**exp_num
    if num > 5000:
        return True
    return False 
# Задача 2
def interval(num, lower_lim, upper_lim):
    if lower_lim <= num <= upper_lim:
        return True
    return False
# Задача 3
def name_check(your_name, my_name):
    if your_name == my_name:
        return True
    return False
# Задача 4
def func(num):
    if 1 < num and 1 > num:
        return True
    return False
# Задача 5
def rate(rating):
    if rating <= 5:
        return "Избегать любой ценой!"
    elif 5 < rating < 9:
        return "Это было весело."
    else:  
        return "Отлично!"

# Задача 6
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num3 < num2 and num2 > num1:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
# Задача 7
def tenth_power(num):
    return num**10
def square_root(num):
    return math.sqrt(num)
# Задача 8
def win_rate(win, loss):
    sum = win + loss
    return str(win / sum * 100) + "%"

# Задача 9
def mid(num1, num2):
    sum = num1 + num2
    return sum / 2
# Задача 10
#В данной задаче необходимо вычислить остаток от деления.
# Для этого нужно умножить
#числитель на 2 и разделить знаменатель на 2.(Но тогда же изменится сама дробь) После изменения двух значений мы
#разделим их и вернем остаток.
#Решение по заданию:
def remain(num1, num2): #num1 = 5 num2 = 4
    num1 = num1 * 2 # num1 = 10
    num2 = num2 / 2 # num2 = 2
    return num1 / num2 # result = 0
#мое решение
def remain1(num1, num2): #num1 = 5 num2 = 4
    return num1 % num2  # result = 1 - на мой взлаг - это считается отстакома
# Задача 11.1
def heading(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3
# Задача 11.2
def tips_calc(total, tips_pr):
    return total * tips_pr / 100
# Задача 12
    #A.
def f(x):
    return x**2
    #B.
def f(x):
    if x <= -2:
        return 1 - (x + 2) * 2
    elif -2 < x <= 2:
        return -(x / 2)
    else: 
        return (x - 2) * 2 + 1
# Задача 13
def calculate(num1, num2, oper):
    if oper == "+":
        return sum(num1, num2)
    elif oper=="-": 
        return num1 - num2
    elif oper=="*":
        return num1 * num2
    elif oper==":":
        return num1 / num2
    else: 
        return "Invalid operator"
# Задача 14
def rock_paper_scissors(player1, player2):
    if player1=="Rock":
        if player2=="Paper":
            return "Player2 won"
        else:
            return "Player1 won"
    elif player1=="Paper":
        if player2=="Scissors":
            return "Player2 won"
        else:
            return "Player1 won"
    elif player1=="Scissors":
        if player2=="Rock":
            return "Player2 won"
        else:
            return "Player1 won"