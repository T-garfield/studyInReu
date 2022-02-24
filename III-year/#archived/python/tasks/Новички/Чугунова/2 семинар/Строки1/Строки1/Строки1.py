favour_word = 'heh'
print(favour_word)
#Задание1
first_name = 'Родриго'
last_name = 'Вильянуэва'
new_account = last_name[:5]
print(new_account)
temp_password = last_name[2:6]
print(temp_password)
#Задание2
def account_generator(first_name,last_name):
    account = first_name[:3] + last_name[:3]
    return account
new_account = account_generator('Родриго','Вильянуэва')
print(new_account)
#Задание3
def password_generator(first_name,last_name):
    password = first_name[-3:] + last_name[-3:]
    return password
temp_password = password_generator('Родриго','Вильянуэва')
print(temp_password)
#Задание4
company_motto = 'Мечты сбываются'
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)
#Задание5
first_name = "Pob"
fixed_first_name  = "R" + first_name[1:]
print(fixed_first_name)
#Задание6
password = 'theycallme\"crazy\"91'
print(password)
#Задание7
def get_length(string):
    print(len(string))
get_length('hehehe')
#Задание8
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False
xxx = letter_check('hehe', 'h')
print(xxx)
#Задание9
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False
xxx2 = contains('watermelon', 'melon')
print(xxx2)
#Задание10
def common_letters(string_one, string_two):
    list = []
    for x in string_one:
        for z in string_two:
            if x == z:
                list.append(z)
    return list
xx = common_letters('banana', 'cream')
print(xx)
#Задание11
def username_generator(first_name, last_name):
    print(first_name[:3]+last_name[:4])
username_generator('Ekaterina', 'Chugunova')

def passwordd_generator(password):
    x=-1
    for letter in password:
        print(password[x])
        x=x+1
    print(letter)
passwordd_generator('EkatChug')
    
