single_digits = range(10)
squares = []
for digits in single_digits:
    print(digits)
    x = digits**2
    squares.append(x)
print(squares)
cubes = [digits**3 for digits in single_digits]
print(cubes)