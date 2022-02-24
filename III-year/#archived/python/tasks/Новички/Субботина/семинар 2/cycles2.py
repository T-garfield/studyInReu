#1
scoops_sold = 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for data in sales_data:
 for d in data:
  scoops_sold = scoops_sold + d
print(scoops_sold)

#2
single_digits = range(10)
squares = []
for digit in single_digits:
 print(digit)
 c = digit*digit
 squares.append(c)
print(squares)
cubes = [digit*digit*digit for digit in single_digits]
print(cubes)