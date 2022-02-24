#1
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for x in sales_data:
    for y in x:
        print(y)
        scoops_sold = y + scoops_sold
print("Сумма:", scoops_sold)
print("..................................")
#2
single_digits = range(10)
squares = []
for digits in single_digits:
    print(digits)
    x = digits**2
    squares.append(x)
print(squares)
cubes = [digits**3 for digits in single_digits]
print(cubes)
print("..................................")