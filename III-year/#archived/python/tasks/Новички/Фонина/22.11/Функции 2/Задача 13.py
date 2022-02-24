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
            return "вы ошибились! исправьтесь."
calc(3, 4, '/')