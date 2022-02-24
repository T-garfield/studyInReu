#Задача1

def fun(osn, exp):
    global step
    step = osn**exp
    print(step)
    return step 

fun(2,2)

if step > 5000:
    print(True)
else:
   print(False)

#Задача2
def fun2(par1, par2, par3):
    
    if (par1 >= par2) and (par1 <= par3):
        return True
    else:
        return False
print(fun2(5, 5, 7))
 
  
#Задача3
def fun3(your_name, my_name):
    for i in your_name:
        if i not in my_name:
            return True
        
    return False
print(fun3("Kate", "Kate"))

#Задача4
def fun4(num):
    if 1 < num and 1 > num:
        return True
    return False

#Задача5
def reit(num):
    if num <= 5:
        print('Избегать любой ценой!')
    elif 5 < num < 9:
        print('Это было весело')
    else:
        print( 'Отлично!')
reit(4)

#Задача6
def fun6(num1, num2 ,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num3 < num2 and num2 > num1:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
print(fun6(1,3,4))

#Задача7
def tenth_power(number):
    power = number**10
    return power
power = tenth_power(2)
print(power)
def square_root(number):
    root = number**0.5
    return root
root = square_root(32)
print(root)
#Задание8
def game(win, lose):
    games = win + lose
    k = (win/games) * 100
    return (k)
k = game(50, 10)
print(k)
#Задание9
def fun9(num1, num2):
    sum = num1 + num2
    av = sum / 2
    return (av)
av = fun9(2, 10)
print(av)
#Задание10
def ost(num1, num2):
    new_num1 = num1 * 2
    new_num2 = num2 * 2
    return (new_num1% new_num2)
ostatok = ost(11, 2)
print(ostatok)
#Задание11(1)
def heading(num):
    print(num)
    print(num * 2)
    print(num * 3)
    print( num * 3)
#Задание11(2)
def fun11(total, percent):
     print(total*percent / 100)
fun11(500, 15)
#Задание12
def f(x):
    return x**2
def f(x):
    if x <= -2:
        return 1 - (x + 2) * 2
    elif -2 < x <= 2:
        return -(x / 2)
    else: 
        return (x - 2) * 2 + 1
#Задание13
def fun13(num1, num2, operator):
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
fun13(3, 2, '+')
#Задание14
def rock_paper_scissors(player1, player2):
    if player1 == 'scissors' and player2 == 'paper':
        print('Выиграл первый игрок!')
    elif player1 == 'scissors' and player2 == 'rock':
        print('Выиграл второй игрок!')
    elif player1 == 'paper' and player2 == 'rock':
        print('Выиграл первый игрок!')
    elif player1 == 'scissors' and player2 == 'rock':
        print('Выиграл второй игрок!')
    elif player1 == "paper" and player2 == "rock":
        print('Выиграл первый игрок!')
    elif player1 == "paper" and player2 == "scissors":
        print('Выиграл второй игрок!')
    else:
        print("Ничья")
rock_paper_scissors('scissors','rock')
