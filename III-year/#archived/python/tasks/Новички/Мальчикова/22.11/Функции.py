#Функции 1

#Ключевые аргументы
print("-_Ключевые аргументы_-")
def create_spreadsheet(title = "Загрузки ", row_count = 1000):
    print("Создание электронной таблицы с именем "+ title + 'c ' + str(row_count) + " строк" )
create_spreadsheet(title = "Приложения ", row_count = 10)
print("")

#Возвращаемые значения
print("-_Возвращаемые значения_-")
def calc_age (current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)
print('Мне '+ str(my_age) + ' лет, а моему отцу ' + str(dads_age) + ' лет' )
print("")

#Несколько возвращаемых значений
print("-_Несколько возвращаемых значений_-")
def get_boundaries (target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
print('Нижний предел: ' + str(low_limit) + '\nВерхний предел: ' + str(high_limit))
print("")

#Области видимости
print("-_Области видимости_-")
print("")

#Заключение
print("-_Заключение_-")
def repeat_stuff (stuff, num_repeats = 10):
    statement = stuff * num_repeats
    return statement
lyrics = repeat_stuff ("Row ", 3) + "Your boat \n"
song = repeat_stuff(lyrics)
print(song) 
print("")
print("")
print("")

#Функции 2
#1
print("-_№1_-")
def метод (основание, экспонента):
    степень = основание ** экспонента
    if степень >= 5000:
        return True
    else:
        return False
print(метод(76,8))
print("")

#2
print("-_№2_-")
def range (num, low_limit, high_limit):
    if num >= low_limit and num <= high_limit:
        return True
    else:
        return False
print(range(67548594,875384587,5647586))
print("")

#3
print("-_№3_-")
def names (your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
print(names('Woody', 'Bazz'))
print("")

#4
print("-_№4_-")
def z_4 (num):
    if num<8 and num>3:
        return True
    else: 
        return False
print(z_4(10))
print("")

#5
print("-_№5_-")
def film (rating):
    if rating <= 5:
        return print("Избегать любой ценой")
    elif rating < 9:
        return print("Это было весело")
    else:
        return print("Отлично!")
(film(10))
print("")

#6
print("-_№6_-")
w = "Победитель - "
def numbers(num1, num2, num3):
    if num1>num2 and num1>num3:
        return print(w + str(num1))
    elif num1<num2 and num2>num3:
        return print(w + str(num2))
    elif num1<num3 and num2<num3:
        return print(w+ str(num3))
    #elif num1 == num2 or num1 == num3 or num2 == num3:
    else:
        return print('Пат')
numbers(43567,54367,32456)
print("")

#7
print("-_№7_-")
def tenth_power(num):
    return num ** 10
def square_root(num):
    return num ** 1/2
print(tenth_power(2), square_root(1024))
print("")

#8
print("-_№8_-")
def games (win, lose):
    total = win + lose
    winning_ratio = (win/total)*100
    return winning_ratio
print ('Коэффициент выигрыша составляет ' + str(games(67,66)) + '%')
print("")

#9
print("-_№9_-")
def num (num1, num2):
    div = (num1 + num2)/2
    return div
print(num(5, 35))
print("")

#10
print("-_№10_-")
def _num_ (num1, num2):
    y = (num1 * 2)%(num2/2)
    return y
print(_num_(8.4,6))
print("")

#11
print("-_№11_-")
def tips(total, percent):
    return (total * percent)/100
print(tips(1530, 20))

def заголовок(num):
    print(num, num*2, num*3)
    return print(num*3)
(заголовок(8))
print("")

#12
print("-_№12_-")
def func1(x):
    if x <= -2:
        return print(1-pow(x+2, 2))
    if x > -2 and x <= 2:
        return print(-(x/2))
    if x > 2:
        return print((pow(x-2, 2) + 1))
func1(-5)
print("")

#13
print("-_№13_-")
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
            return "Ошибка"
calc(4, 5, '*')
print("")

#14
print("-_№14_-")
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
game("камень", "ножницы")
print("")


