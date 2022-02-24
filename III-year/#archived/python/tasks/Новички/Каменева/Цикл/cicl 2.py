#Задание 1
scoops_sold= 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

for taste in sales_data:
    #print(taste)
    for tastein in taste:
       #print(tastein)   
        scoops_sold  = tastein + scoops_sold

print(scoops_sold)

#Задание 2

single_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for list in single_digits:  
    print(list)
    squares.append(list**2)
print(squares)    

cubes = [new**3 for new in single_digits]

print(cubes)