def names (your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False
print(names('mike', 'nick'))

#если кол-во символов совпадает
def len_names (your_name, my_name):
    if len(your_name) == len(my_name):
        return True
    else:
        return False
print(len_names('mickеy', 'nick'))