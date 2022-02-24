# 1
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for scoops in sales_data:
    for sold in scoops:
        scoops_sold = scoops_sold + sold
print(scoops_sold)

# 2
print()
single_digits = range(10)
squares = []
for loop in single_digits:
    print(loop)
    squares = [square**2 for square in single_digits]
print(squares)
cubes = [cube**3 for cube in single_digits]
print(cubes)

