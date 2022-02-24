print("*** Задача 1 ***")
while True:
    def exponent(a,n):
        result = a**n
        return result
    a = input("Введите основание степени: ")
    a = int(a)
    n = input("Введите показатель степени: ")
    n = int(n)
    result = exponent(a,n)
    print(f"Результат возведения в степень: {result}")
    if result > 5000:
        print("Результат больше 5000:", True)
    else: 
        print("Результат больше 5000:", False)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 2 ***")
while True:
    def test(x, a, b):
        if x>=a and x<=b:
            print("Число в определенный диапазон:", True)
        else: 
            print("Число в определенный диапазон:", False)
    x = input("Введите тестируемое число: ")
    x = int(x)
    a = input("Введите нижнюю границу: ")
    a = int(a)
    b = input("Введите верхнюю границу: ")
    b = int(b)
    test(x, a, b)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break


print("\n*** Задача 3 ***")
while True:
    def test_name(your_name, my_name):
        if your_name == my_name:
            print("Имена равны:", True)
        else: 
            print("Имена равны:", False)
    your_name = input("Твое имя: ")
    your_name = your_name.upper()
    my_name = input("Мое имя: ")
    my_name = my_name.upper()
    test_name(your_name, my_name)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 4 ***")
while True:
    def test_4(num):
        if num < 2 and num > 4:
            print(True)
        else: 
            print(False)
    num = input("Тестируемое число: ")
    num = int(num)
    test_4(num)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 5 ***")
while True:
    def film(rate):
        if rate <= 5: 
            print("Избегать любой ценой!")
        elif rate < 9: 
            print("Это было весело.")
        else: 
            print("Отлично!")
    rate = input("Введите рейтинг фильма: ")
    rate = int(rate)
    film(rate)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 6 ***")
while True:
    def max(num1, num2, num3):
        if num1 > num2 and num1 > num3:
            print("Наибольшое число:", num1)
        elif num2 > num1 and num2 > num3:
            print("Наибольшое число:", num2)
        elif num3 > num1 and num3 > num2:
            print("Наибольшое число:", num3)
        else:
            print("Наибольшое число: Ничья!")
    num1 = input("Введите первое число: ")
    num1 = int(num1)
    num2 = input("Введите второе число: ")
    num2 = int(num2)
    num3 = input("Введите третье число: ")
    num3 = int(num3)
    max(num1, num2, num3)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 7 ***")
import math
print("--- Число в десятую степень ---")
while True:
    def tenth_power(a):
        result_7a = a**10
        return result_7a
    a = input("Введите число: ")
    a = int(a)
    result_7a = tenth_power(a)
    print(f"{a} в десятую степень: {result_7a}")
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break
print("--- Извлечение квадратного корня ---")
while True:
    def square_root(b):
        result_7b = math.sqrt(b)
        return result_7b
    b = input("Введите число: ")
    b = int(b)
    result_7b = square_root(b)
    print(f"Корень квадратный из {b}: {result_7b}")
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 8 ***")
while True:
    def game(win, lost):
        number = win + lost
        percent_win = win/number
        return '{percent:.2%}'.format(percent=percent_win)
    win = input("Количество выигрышей: ")
    win = int(win)
    lost = input("Количество проигрышей: ")
    lost = int(lost)
    percent_win = game(win, lost)
    print("Процент выигранных игр:", str(percent_win))
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 9 ***")
while True:
    def avg(a,b):
        return (a+b)/2
    a = input("Введите первое число: ")
    a = int(a)
    b = input("Введите второе число: ")
    b = int(b)
    c = avg(a,b)
    print(f"Среднее значение двух чисел {a} и {b}: {c}")
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 10 ***")
while True:
    def ex_10(a,b):
        x = a*2
        y = b/2
        return x%y
    a = input("Введите первое число: ")
    a = int(a)
    b = input("Введите второе число: ")
    b = int(b)
    c = ex_10(a,b)
    print("Остаток от деления:", c)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 11a ***")
while True:
    def ex_11(num):
        print(num, "в 1 раз:", num**1)
        print(num, "в 2 раз:", num**2)
        print(num, "в 3 раз:", num**3)
        return num**3
    num = input("Введите число: ")
    num = int(num)
    ex_11(num)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break


print("\n*** Задача 11b ***")
while True:
    def tip(total, percent):
        money = (total*percent)/100
        return money
    total = input("Общую стоимость еды: ")
    total = int(total)
    percent = input("Процент чаевых: ")
    percent = int(percent)
    money = tip(total, percent)
    print("Сумма чаевых:", money)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 12 ***")
while True:
    def f_x(x):
        if x<=-2:
            f = 1-(x+2)**2
        elif x>-2 and x<=2:
            f = -x/2
        else:
            f = (x-2)**2 +1
        return f
    x = input("x = ")
    x = int(x)
    f = f_x(x)
    print("f(x) =", f)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 13 ***")
while True:
    def plus(a, b):
        return a + b
    def minus(a, b):
        return a - b
    def multiple(a, b):
        return a * b
    def divide(a, b):
        return a / b
    print("Операции:")
    print("1.Сложить")
    print("2.Вычесть")
    print("3.Умножить")
    print("4.Делить")
    f = input("Выберите операцию: ")
    f = int(f)
    if f != 1 and f != 2 and f != 3 and f != 4:
        print("Ошибка! Попробуйте еще раз!")
    else:
        a = input("Первое число: ")
        a = int(a)
        b = input("Второе число: ")
        b = int(b)
        if f == 1:
            c = plus(a,b)
            print(f"Ответ: {a} + {b} = {c}")
        if f == 2:
            c = minus(a,b)
            print(f"Ответ: {a} - {b} = {c}")
        if f == 3:
            c = multiple(a,b)
            print(f"Ответ: {a} x {b} = {c}")
        if f == 4:
            c = divide(a,b)
            print(f"Ответ: {a} : {b} = {c}")
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задача 14 ***")
import random
while True:
    player_1 = input("Сделайте выбор — камень, ножницы или бумага: ")
    actions = ["камень", "бумага", "ножницы"]
    if player_1 != actions[0] and player_1 != actions[1] and player_1 != actions[2]:
        print("Ошибка!")
    else:
        player_2 = random.choice(actions)
        print("Первый игрок", player_1 + ",", "второй игрок", player_2,".")
        if player_1 == player_2:
            print("Оба пользователя выбрали", player_1 + ".", "Ничья!")
        elif player_1 == "камень":
            if player_2 == "ножницы":
                print("Камень бьет ножницы! Первый игрок победили!")
            else:
                print("Бумага оборачивает камень! Второй игрок победили!")
        elif player_1 == "бумага":
            if player_2 == "камень":
                print("Бумага оборачивает камень! Первый игрок победили!")
            else:
                print("Ножницы режут бумагу! Второй игрок победили!")
        elif player_1 == "ножницы":
            if player_2 == "бумага":
                print("Ножницы режут бумагу! Первый игрок победили!")
            else:
                print("Камень бьет ножницы! Второй игрок победили!")
        again = input("Еще раз? (д/н): ") 
        if again != "д": 
            break 