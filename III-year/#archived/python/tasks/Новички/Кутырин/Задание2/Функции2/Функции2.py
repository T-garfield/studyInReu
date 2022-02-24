import math
import statistics
def power_exceed5000(x,power):
    if math.pow(x,power) > 5000:
        print("True")
    else:
        print("False")
     
power_exceed5000(10,2)


def num_between(num,bot,top):
    if num >= bot and num <= top:
        print("True")
    else:
        print("False")
num_between(10,0,100)


def are_names_equal(your_name, my_name):
    if my_name==your_name:
        print("True")
    else:
        print("False")
are_names_equal("Игорь","Егор")


def contradiction(num):
    if num<10 and num>10:
        print("True")
    else:
        print("False")
contradiction(10)


def film_rating(rating):
    if rating <= 5:
        print("Избегать любой ценой!")
    elif rating < 9:
        print("Это было весело")
    else:
        print("Отлично!")
film_rating(10)


def num_comparison(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    elif num3 > num1 and num3 > num2:
        print(num3)
    else:
        print("Ничья!")
num_comparison(3,10,10)

def tenth_power(base,power=10):
    num = math.pow(base,power)
    print(num)
tenth_power(5)

def square_root(base):
    num = math.sqrt(base)
    print(num)
square_root(256)

def winrate(wins,losses):
    total = wins + losses
    percent = wins/total
    print(percent)
winrate(30,30)

def average(num1,num2):
    set_of_num = [num1,num2]
    print(statistics.mean(set_of_num))
average(2,4)

def remainder(numerator,denominator):
    numerator1 = numerator * 2
    denominator1 = denominator * 2
    print(numerator1 % denominator1)
remainder(11,10)

def multiple(num):
    num1 = num
    num2 = num1 * 2
    num3 = num1 * 3
    print(num1," ",end="")
    print(num2," ",end="")
    print(num3)
multiple(5)

def tips(total,percent):
    print(total*percent/100)
tips(5000,10)

def f(x):
    if x <= -2:
        print(1-(math.pow(x+2,2)))
    elif x > -2 and x <= 2:
        print(-x/2)
    else:
        print((math.pow(x-2,2))+1)

def calculator(num1,sign,num2):
    if sign == "+":
        print(num1+num2)
    elif sign == "-":
        print(num1-num2)
    elif sign == "*":
        print(num1*num2)
    elif sign == "/":
        print(num1/num2)
    else:
        print("Error")
calculator(1,"+",3)

def rock_paper_scissors(player1,player2):
    if player1 == "rock" and player2 == "scissors":
        print("player1 wins")
    elif player1 == "rock" and player2 == "paper":
        print("player2 wins")
    elif player1 == "scissors" and player2 == "paper":
        print("player1 wins")
    elif player1 == "scissors" and player2 == "rock":
        print("player2 wins")
    elif player1 == "paper" and player2 == "rock":
        print("player1 wins")
    elif player1 == "paper" and player2 == "scissors":
        print("player2 wins")
    else:
        print("Ничья")

rock_paper_scissors("scissors","scissors")