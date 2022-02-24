def func1(x):
    if x <= -2:
        return print(1-pow(x+2, 2))
    if x > -2 and x <= 2:
        return print(-(x/2))
    if x > 2:
        return print((pow(x-2, 2) + 1))
func1(-5)
