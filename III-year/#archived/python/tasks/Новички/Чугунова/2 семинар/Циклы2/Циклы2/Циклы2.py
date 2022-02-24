#Задание1
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for sales in sales_data:
    for data in sales:
        scoops_sold += data
print(scoops_sold)
#Задание2
single_digits = range(10)
squares = []
for digits in single_digits:
    print(digits)
for z in single_digits:
    squares.append(z**2)
    print(z)
print(squares)
cubes = [x**3 for x in single_digits]
print(cubes)
