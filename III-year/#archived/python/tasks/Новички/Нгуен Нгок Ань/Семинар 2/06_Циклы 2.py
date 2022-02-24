print("*** Задание 1 ***")
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for i in sales_data:
    print(i)
    for x in i:
        scoops_sold += x
print("Общее количество проданных сортов:", scoops_sold)

print("\n*** Задание 2 ***")
single_digits = range(10)
squares = []
for i in single_digits:
    squares = i**2
    print(i)
    print(squares)
cubes = []
for i in single_digits:
    cubes.append(i)
print(cubes)
