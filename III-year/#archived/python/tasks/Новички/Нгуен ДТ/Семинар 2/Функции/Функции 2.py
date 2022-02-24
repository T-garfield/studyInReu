# 1
def input(x, y):
    if x ** y >= 5000:
        return True
    else:
        return False


print(input(10, 20))

# 2
print()
def test(x, y, z):
    if y <= x <= z:
        return True
    else:
        return False


print(test(3, 2, 1))

# 3
print()
def name(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False


print(name('Tim', 'Timmy'))

# 4
print()
def func(num):
    if num == 0 and num != 0:
        return True
    else:
        return False
print(func(6))
print(func(0))

#5
print()
def rate(rating):
    if rating <= 5:
        return "Избегать любой ценой!"
    elif rating < 9:
        return "Это было весело"
    else:
        return "Отлично!"
print(rate(7))

# 6
print()
def compare(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "Ничья!"
print(compare(50,63,63))

# 7
print()
def tenth_power(x):
    return 10**x
def square_root(y):
    return y**(1/2)

print(tenth_power(5))
print(square_root(16))

# 8
print()
def prop(win, lose):
    total = win + lose
    return win/total*100
print(prop(8,2))

# 9
print()
def avg(x,y):
    sum = x + y
    return sum / 2
print(avg(2,4))

# 10
print()
def re(num1,num2):
    return num1 % num2
print(re(5, 2))

# 11
print()
def inp(num):
    print(num)
    print(num*2)
    print(num*3)
inp(4)

# 11
print()
def tip(cost, percent):
    return cost*percent/100
print(tip(1000,20))

# 13
print()
def calc(num1,num2,op):
    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
calc(6, 5, '*')

# 14
print()
def rps(p1, p2):
    if p1 == 'scissors' and p2 == 'paper':
        print('Выиграл первый игрок!')
    elif p1 == 'scissors' and p2 == 'rock':
        print('Выиграл второй игрок!')
    elif p1 == 'paper' and p2 == 'rock':
        print('Выиграл первый игрок!')
    elif p1 == 'scissors' and p2 == 'rock':
        print('Выиграл второй игрок!')
    elif p1 == "paper" and p2 == "rock":
        print('Выиграл первый игрок!')
    elif p1 == "paper" and p2 == "scissors":
        print('Выиграл второй игрок!')
    else:
        print("Ничья")
rps('paper','rock')