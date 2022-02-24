def create_spreadsheet(title, row_count=1000):
    print("Создание электронной таблицы с именем " + title + " из " + str(row_count) + " строк")
create_spreadsheet("Приложения", 10)

def calculate_age(current_year1, birth_year1):
    return current_year1-birth_year1
my_age = calculate_age(2049,1993)
dads_age = calculate_age(2049, 1953)
print("мне " + str(my_age) + " лет, а моему отцу " + str(dads_age) + " лет")

current_year = 2048
def calc_age(current_year, birth_year):
    return current_year - birth_year
print(current_year)
print(calc_age(current_year, 1970))

def repeat_stuff(stuff, num_repeats):
    statement = stuff * num_repeats
    return statement
num_repeats = 10
print(repeat_stuff("Row ",3)+"Your Boat")
lyrics = repeat_stuff("Row ",3)+"Your Boat"
print(lyrics)

#Задача1
def M_1(a,b):
    c = a**b
    return c
num = M_1(5,4)
if num>5000:
    print(True)
else:
    print(False)

#2
n=7
def M_2(a,b,c):
    if n>=a and n<=b:
        print(True)
    else:
        print(False)
M_2(4,8,16)

#3
def M_3(your_name, my_name):
    if your_name==my_name:
        print(True)
    else:
        print(False)
M_3("A","K")
M_3("N","N")

#5
def M_5(a):
    if a<=5:
        print("Избегать любой ценой")
    elif a<9 and a>5:
        print("Это было весело")
    else:
        print("Отлично")
M_5(8)

#6
def M_6(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2>num3:
        print(num2)
    elif num3>num1 and num3>num2:
        print(num3)
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Ничья")
M_6(0,8,4)

#7
def tenth_power(a):
    return a**10

def square_root(b):
    return b**(0.5)

#8
def M_8(a,b):
    c = a+b
    d = (a/c)*100
    return print("процент побед равен " + str(d) + "%")
M_8(4,6)

#9
def M_9(num1, num2):
    c = (num1+num2)/2
    return c
print(M_9(4,8))

#10
def M_10(a,b):
    d = a*2
    e = b/2
    c = d%e
    return c
print(M_10(20,16))

#11
def M_11(num):
    print(num)
    print(num*2)
    print(num*3)
    return num*3
M_11(4)

#12
def M_12(x):
    if x<=(-2):
        f=1-((x+2)**2)
    elif x>(-2) and x<=2:
        f=-x/2
    elif x>2:
        f=((x-2)**2)+1
    return f
print(M_12(1))

#13
def M_13(a, n, b):
    if n == "+":
        print(a+b)
    elif n == "-":
        print(a-b)
    elif n == "*":
        print(a*b)
    elif n == "/":
        print(a/b)
    else:
        print("выбрано неизвестное действие")
M_13(3, "*", 4)

#14
def M_14(a,b):
    if a =="Камень" and b == "Бумага":
        print("Побеждает " + b)
    elif a =="Бумага" and b == "Камень":
        print("Побеждает " + a)
    elif a =="Ножницы" and b == "Камень":
        print("Побеждает " + b)
    elif a =="Камень" and b == "Ножницы":
        print("Побеждает " + a)
    elif a =="Ножницы" and b == "Бумага":
        print("Побеждает " + a)
    elif a =="Бумага" and b == "Ножницы":
        print("Побеждает " + b)
    elif a==b:
        print("Ничья")
M_14("Ножницы", "Камень")

