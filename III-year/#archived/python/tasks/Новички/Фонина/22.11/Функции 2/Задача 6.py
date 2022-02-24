def numbers(num1, num2, num3):
    if num1>num2 and num1>num3:
        return print('Выиграло первое число, вот оно: ' + str(num1))
    elif num1<num2 and num2>num3:
        return print('Выиграло второе число, вот оно: ' + str(num2))
    elif num1<num3 and num2<num3:
        return print('Выиграло третье число, вот оно: ' + str(num3))
    #elif num1 == num2 or num1 == num3 or num2 == num3:
    else:
        return print('Ничья!')
numbers(234575724,234285724,234275724)