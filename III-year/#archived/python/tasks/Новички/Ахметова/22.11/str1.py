#Задание_1
favour_word = "milk"
print(favour_word)
print()

#Задание_2
first_name = "Родриго"
last_name = "Вильянуэва"
new_account = last_name[:5]
print(new_account)
print()

#Задание_3
account_generator = first_name[0:3] + last_name[0:3]
new_account = account_generator
print(new_account)
print()

#Задание_4
length1 = len(first_name)
length2 = len(last_name)
password_generator = first_name[length1-3:] + last_name[length2-3:]
temp_password = password_generator
print(temp_password)
print()

#Задание_5
company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)
print()

#Задание_6
first_name = "об"
fixed_first_name = "Р" + first_name
print(fixed_first_name)
print()

#Задание_7
temp_password = "theycallme\"crazy\"91"
print(temp_password)
print()

#Задание_8
def get_length(password):
    print(len(password))
get_length('qwerty')
print()

#Задание_9
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False
let = letter_check('mango', 'm')
print (let)
print()

#Задание_10
def contains(big_string, little_string):
    if little_string in big_string:
        print(True)
    else:
        print(False)
contains('milk', "k")
print()

#Задание_10
def common_letters(string_one, string_two):
    for letter1 in string_one:
        for letter2 in string_two:
            if letter1 == letter2:
                print(letter1)
common_letters('milk', 'mango')
print()

#Задание_11
def username_generator(first_name, last_name):
    print(first_name[:3] + last_name[:4])
username_generator('John','Lennon') 
print()

#Задание_11
def passwordd_generator(password):
    i=-1
    for letter in password:
        print(password[i])
        i=i+1
    print(letter)
passwordd_generator('JohLen')