#Matveev
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed',
             'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'kingbed', 
             'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()

print(inventory)
print(first, last, inventory_2_6, first3, twin_beds)
