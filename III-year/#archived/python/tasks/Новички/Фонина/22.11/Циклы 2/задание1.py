sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for x in sales_data:
    for y in x:
        print(y)
        scoops_sold = y + scoops_sold
print("Сумма:", scoops_sold)