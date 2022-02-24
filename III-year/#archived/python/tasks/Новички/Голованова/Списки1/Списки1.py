'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

...

sam_height = ["Sam", 67]

heights = [["Sam", 67], ["Wick",68]]
age = [["Aron", 15], ["Judy", 16]]

names = ["Ben", "Holly", "Ann"]
dogs_names = ["Sharik", "Gab", "Beethoven"]
names_and_dogs_names = zip(Names,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names) 
print(list_of_names_and_dogs_names)

orders = ["маргаритки", "барвинок"]
print(orders)
orders.append("тюльпаны")
orders.append("розы")
print(orders)

orders = ["маргаритка", "лютик", "львиный зев", "гардения", "лилия"]
new_orders = orders + ["сирень", "ирис"]
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]

list1 = range(9)
list2 = range(8)
print(list(list1))

list1 = range(5,15,3)
list2 = range(0,40,5)
print(list(list2))

first_names = ["Эйнсли", "Бен", "Чани", "Депак"]
age = []
age.append(42)
all_ages = [32, 41, 29] + age
ids = range(0,4)
name_and_age = zip(first_names, all_ages, ids)
print(list(name_and_age))