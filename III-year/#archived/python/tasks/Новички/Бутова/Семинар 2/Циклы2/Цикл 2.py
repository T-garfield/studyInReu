
#1

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold=0
for i in sales_data:
    for j in i:
        scoops_sold+=j
print(scoops_sold)

#2
squares=[]
single_digits=range(10)
for i in single_digits:
    print(i)
    squares.append(i**2)
print(squares)   
cubes=[i**3 for i in single_digits]
print(cubes)