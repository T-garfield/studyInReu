print('Задание 1')
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for data1 in sales_data:
    for data2 in data1:
        print(data2)
scoops_sold = 0
scoops_sold = scoops_sold + data2
print(scoops_sold)
print()

print('Задание 2')
squares = []
single_digits = range(10)
for num1 in single_digits:
    if num1 == 0:
        num2 = 0
    else:
        num2 = num1**2
    squares.append(num2)
print(squares)
cubes = []
for num1 in single_digits:
    if num1 == 0:
        num2 = 0
    else:
        num2 = num1**3
    cubes.append(num2)
print(cubes)