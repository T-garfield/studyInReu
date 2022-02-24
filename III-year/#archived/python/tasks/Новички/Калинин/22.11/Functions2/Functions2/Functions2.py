#Задача 1
def метод (основание, экспонента):
    степень = основание ** экспонента
    if степень >= 5000:
        return True
    else:
        return False
print(метод(36,4))
#Задание 2
def range (num, low_limit, high_limit):
    if num >= low_limit and num <= high_limit:
        return True
    else:
        return False
print(range(35298,32873,37654))
#Задание 3
def names (your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
print(names('Jack', 'John'))
#Задание 4
def function (num):
    if num<6 and num>6:
        return True
    else: 
        return False
print(function(6))
#Задание 5 
def film (rating):
    if rating <= 5:
        return print("ИЗБЕГАТЬ ЛЮБОЙ ЦЕНОЙ!!!!!!!")
    elif rating < 9:
        return print("это было весело :)")
    else:
        return print("Отлично!")
film(11)
#Задание 6
def numbers(num1, num2, num3):
    if num1>num2 and num1>num3:
        return print('Самое большое число - 1-ое: ' + str(num1))
    elif num1<num2 and num2>num3:
        return print('Самое большое число - 2-ое:  ' + str(num2))
    elif num1<num3 and num2<num3:
        return print('Самое большое число - 3-е:  ' + str(num3))
numbers(4937,3085,2046)
#Задание 7
def tenth_power(num):
    return num**10
def square_root(num):
    return math.sqrt(num)
print(tenth_power(5), square_root(36))
#Задание 8
def games (win, lose):
    total = win + lose
    winning_ratio = (win/total)*100
    return winning_ratio
print ('Коэффициент выигрыша составляет ' + str(games(50,30)) + '%')
# Задача 9
def numero (num1, num2):
    sum = num1 + num2
    return sum / 2
# Задача 10
def numero (num1, num2):
    t = (num1 * 2)%(num2/2)
    return t
print(намберс(4.6,8))
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
    if player1=="камень":
        if player2=="бумага":
            return "Player2 won"
        else:
            return "Player1 won"
    elif player1=="бумага":
        if player2=="ножницы":
            return "Player2 won"
        else:
            return "Player1 won"
    elif player1=="ножницы":
        if player2=="камень":
            return "Player2 won"
        else:
            return "Player1 won"