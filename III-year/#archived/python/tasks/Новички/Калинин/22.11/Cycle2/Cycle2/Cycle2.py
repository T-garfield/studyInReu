#Задание 1
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for data in sales_data:
    for i in data:
        scoops_sold += i 
print(scoops_sold)
#Задание 2
single_digits = range(10)
print(single_digits)
squares = []
for i in single_digits:
    squares.append(i**2)
    print(i)
print(squares)
cubes = [i**3 for i in single_digits]
print(cubes)
