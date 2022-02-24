#task_1
def stepen(x,power):
    if x**power > 5000:
        return True
    else:
        return False
y = stepen(5,10)
print (y)
print()

#task_2
def range(num, low, high):
    if num >= low and num <= high:
        return True
    else:
        return False
new_num = range(16, 3, 15)
print (new_num)
print()

#task_3
def names(your_name, my_name):
    if your_name == my_name:
         return True
    else:
        return False
fr = names('Hai', 'Lina')
print (fr)
print()

#task_4
def func(num):
    if num > 5 and num < 5:
         return True
    else:
        return False
check = func(3)
print (check)
print()

#task_5
def film(rating):
    if rating <= 5:
         return 'Избегать любой ценой!'
    elif rating < 9:
        return 'Это было весело'
    else:
         return 'Отлично!'
new_film = film(6)
print (new_film)
print()

#task_6
def big(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return 'Ничья!'
numbers = big (6, 6, 3)
print (numbers)
print()

#task_7
def tenth_power(num):
    power = num**10
    return power
power = tenth_power(2)
print(power)
print()

def square_root(num):
    root = num**0.5
    return root
root = square_root(4)
print(root)
print()

#task_8
def gDis(win, lose):
    games = win + lose
    percent = (win / games)*100
    return (percent)
percent = gDis(40, 10)
print(percent)
print()

#task_9
def avr(num1, num2):
    sum = num1 + num2
    average = sum / 2
    return (average)
average = avr(1, 17)
print(average)
print()

#task_10
def ost(num1, num2):
    new_num1 = num1 * 2
    new_num2 = num2 * 2
    return (new_num1 %  new_num2)
ostatok = ost(10, 5)
print(ostatok)
print()

#task_11
def food(total, percent):
     print(total * percent / 100)
food(5000, 10)
print()

#task_12
def calc(num1, num2, op):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
calc(10, 5, '/')
print()

#task_14
def rps(player1, player2):
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
rps('paper','rock')


