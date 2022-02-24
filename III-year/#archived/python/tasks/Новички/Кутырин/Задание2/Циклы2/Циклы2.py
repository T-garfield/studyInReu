import math
scoops_sold=0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for number1 in sales_data:
    for number2 in number1:
        print(number2)
        scoops_sold = scoops_sold + number2
print("Сумма:",scoops_sold)     

single_digits = [print(num,end=" ",) for num in range(10)]

print("\n")
single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
for num in single_digits:
    if num == 0:
        num1=0
    else:
        num1 = math.pow(num,2)
    squares.append(num1)
print(squares)

cubes = []
for num in single_digits:
    if num == 0:
        num1=0
    else:
        num1 = math.pow(num,3)
    cubes.append(num1)
print(cubes)

