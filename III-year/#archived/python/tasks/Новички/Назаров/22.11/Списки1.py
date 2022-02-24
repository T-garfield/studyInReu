#1
sam_height=['Сэм', 67]
#2
height=[['Сэм', 67], ['Вик', 68] ]
student=[['Аарону', 15] , ['Дхрути',16]]
#3
names=['Ben', 'Holly', 'Ann'] 
dogs_names= ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names=zip(names, dogs_names)
list_of_names_and_dogs_names=list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
#4
orders = ['маргаритки', 'барвинок']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)
#5
orders=['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders=orders+['сирень', 'ирис']
print(new_orders)
broken_prices =[5, 3, 4, 5, 4]+[4]
#6
list1 = range(0,9)
print(list(list1))
list2 = range(0,7)
print(list(list2))
#7
list1 = range(5,15,2)
print(list(list1))
list2 = range(0,40,5)
print(list(list2))
#8
first_names=['Эйнсли', 'Бен', 'Чани', 'Депак']
age=[]
age.append(42)
all_ages=[32, 41, 29]+age
name_and_age=zip(first_names,all_ages)
ids=range(0,4)
print(list(name_and_age))
print(list(ids))