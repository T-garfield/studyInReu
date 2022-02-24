import math
import statistics
#1
def method(x,y):
    if math.pow(x,y) > 5000:
        print("True")
    else:
        print("False")
method(7,4)
#2
def check_num(x,low,top):
    if (x >= low) and (x <= top):
        print("True")
    else:
        print("False")
check_num(6,1,20)
#3
def compare_names(your_name, my_name):
    if my_name==your_name:
        print("True")
    else:
        print("False")
compare_names("Саша","Маша")
#4
def function(num):
    if (num<=0) and (num>=-100):
        print("True")
    else:
        print("False")
function(-33)
#5
def rating_movie(rating):
    if rating <= 5:
        print("Избегать любой ценой!")
    elif rating < 9:
        print("Это было весело")
    else:
        print("Отлично!")
rating_movie(3)
#6
def compare_numbers(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        print(num1)
    elif (num2 > num1) and (num2 > num3):
        print(num2)
    elif (num3 > num1) and (num3 > num2):
        print(num3)
    else:
        print("Ничья!")
compare_numbers(6,7,3)
#7
def tenth_power(a,b=10):
    num = math.pow(a,b)
    print(num)
tenth_power(7)

def square_root(a):
    res = math.sqrt(a)
    print(res)
square_root(121)
#8
def win(wins,losses):
    sum = wins + losses
    perc = wins/sum*100
    print(perc)
win(45,40)
#9
def average(num1,num2):
    sum = num1 +num2
    average1 = sum/2
    print(average1)
average(1,5)
#10
def ostatok(numerator,denominator):
    a = numerator * 2
    b = denominator * 2
    print(a % b)
ostatok(3,2)
#11
def return_num(num):
    num1 = num
    num2 = num1 * 2
    num3 = num1 * 3
    print(num1," ",end="")
    print(num2," ",end="")
    print(num3)
return_num(6)
#11
def chai(total,percent):
    print(total*percent/100)
chai(60000,20)
#12
def f(x):
    if x <= -2:
        print(1-(math.pow(x+2,2)))
    elif x > -2 and x <= 2:
        print(-x/2)
    else:
        print((math.pow(x-2,2))+1)
#13
def calculator(num1,arifm,num2):
    if arifm == "+":
        print(num1+num2)
    elif arifm == "-":
        print(num1-num2)
    elif arifm == "*":
        print(num1*num2)
    elif arifm == "/":
        print(num1/num2)
    else:
        print("ошибка")
calculator(10,"/",2)
#14
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
        print("Ничья!")

rock_paper_scissors("rock","paper")