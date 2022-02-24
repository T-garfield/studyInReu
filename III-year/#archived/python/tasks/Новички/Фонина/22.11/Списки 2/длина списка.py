list1 = range (2, 20, 2)
print(list(list1))
list1_len = (len(list1))
#изменим range (2, 20, 2) на range (2, 20, 3)
new_list1 = range (2, 20, 3)
print(list(new_list1))
new_list1_len = (len(new_list1))
# длина списка сократилась на 3 единицы
print ('Длина списка изменилась на', list1_len-new_list1_len, "единицы")