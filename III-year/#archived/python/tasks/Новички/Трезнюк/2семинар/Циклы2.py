#Задание 1
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for data in sales_data:
    for i in data:
        scoops_sold += i 
print(scoops_sold)
#Задание 
single_digits = range(10) # 1.
print(single_digits)
squares = [] # 3.
for i in single_digits: # 2.
    squares.append(i**2) # 4.
    print(i)
print(squares) # 5.
cubes = [i**3 for i in single_digits] # 6.
print(cubes) # 7.