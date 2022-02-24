#1
import math


def method (base, exhibitor):
    degree = base ** exhibitor
    if degree >= 5000:
        return True
    else:
        return False
print(method(15,2))

#2
def num_between(num, low_limit, high_limit):
    if num >= low_limit and num <= high_limit:
        print("True")
    else:
        print("False")
num_between(8,0,56)

#3
def name_check(your_name, my_name):
    if my_name==your_name:
        print("True")
    else:
        print("False")
name_check("Арина","Алина")

#4
def contradiction(num):
    if num<8 and num>8:
        print("True")
    else:
        print("False")
contradiction(8)

#5
def film_score(rating):
    if rating <= 5:
        print("Избегать любой ценой!")
    elif rating < 9:
        print("Это было весело")
    else:
        print("Отлично!")
film_score(8)

#6
def num(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    else:
        print("Ничья!")
num(4,8,8)

#7
def tenth_power(base,degree=10):
    num = math.pow(base,degree)
    print(num)
tenth_power(8)


def square_root(base):
    num = math.sqrt(base)
    print(num)
square_root(289)

#8
def games_won(wins,losses):
    total = wins + losses
    percent = wins/total
    print(percent)
games_won(10,40)

#9
def mean(num1,num2):
    return (num1+num2)/2
print(mean(25,8))

#10
def remainder(num1,num2):
   return num1%num2
print(remainder(13,5))

#11
def multiple(num):
    num1 = num
    num2 = num1 * 2
    num3 = num1 * 3
    print(num1," ",end="")
    print(num2," ",end="")
    print(num3)
multiple(4)

#11
def tips(total,tips_perc):
    return total*tips_perc/100
print(tips(2547,10))

#12
def f(x):
    if x <= -2:
        print(1-(math.pow(x+2,2)))
    elif x > -2 and x <= 2:
        print(-x/2)
    else:
        print((math.pow(x-2,2))+1)

#13
def calculator(num1,num2, operator):
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    else:
        print("wrong")
calculator(4,"+",3)

#14
def game(player1, player2):
    if player1=='ножницы':
        if player2=='бумага':
            return 'победил 1 игрок'
        else:
            return 'победил 2 игрок'
    elif player1=='бумага':
        if player2=='камень':
            return 'победил 2 игрок'
        else:
            return 'победил 1 игрок'
    elif player1=='камень':
        if player2=='ножницы':
            return 'победил 1 игрок'
        else:
            return 'победил 2 игрок'
print(game('бумага', 'ножницы'))