#Задание 1
favour_word = "python"
print(favour_word)
#Задание 2
first_name = "Родриго"
last_name = "Вильянуэва"
new_account = last_name[:5]
temp_password = last_name[2:6]
#Задание 3
def account_geneartor(first_name, last_name):
    acc = first_name[:3] + last_name[:3]
    return acc
new_account= account_geneartor(first_name, last_name)
#Задание 4
def password_generator(first_name, last_name):
    pas = first_name[-3:] + last_name[-3:]
    return pas
temp_password = password_generator(first_name, last_name)
#Задание 5
company_motto= "Мечты сбываются"
second_to_last = company_motto[-1]
final_word = company_motto[-4:]
#Задание 6
first_name = "Rob"
fixed_first_name  = "P" + first_name[1:]
#Задание 7
robs_pass = """theycallme"crazy"91"""
#Задание 8
def get_length(my_string):
    counter = 0
    for i in my_string:
        counter +=1
    return counter
#задание 9
def letter_check(word, char):
    if char in word:
        return True
    return False
#Задание 10
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    return False
def common_letters(string_one, string_two):
    common_list = []
    for i in string_one:
        for j in string_two:
            if i == j:
                common_list.append(j)
    return common_list
#Задание 11
def username_generator(first_name, last_name):
    if len(first_name) < 3 or len(last_name) < 4:
        nickname = first_name + last_name
    else:
        nickname = first_name[:3] + last_name[:4]
    return nickname
def password_generator(nickname):
    password = ""
    first_part = ""
    second_part = ""
    for char in nickname:
        if char != nickname[-1]:
            first_part += char
        else:
            second_part += char
    password = second_part + first_part
    return password
