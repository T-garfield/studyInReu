#1
favour_word = "КРИНЖ"
print("Мое любимое слово -", favour_word)
print("...................................")
#2
first_name = "Родриго"
last_name = "Вильянуэва"

new_account = last_name[:5]
print(new_account)

temp_password = last_name[2:6]
print(temp_password)
print("...................................")
#3
first_name = "Родриго"
last_name = "Вильянуэва"

account_generator = first_name[:3] + last_name[:3]
#print(account_generator)

new_account = account_generator
print(new_account)
print("...................................")
#4
first_name = "Родриго"
last_name = "Вильянуэва"

length_fn=len(first_name)
length_ln=len(last_name)

temp_password = first_name[length_fn-3:] + last_name[length_ln-3:]
print(temp_password)
print("...................................")
#5
company_motto = 'Мечты сбываются'
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)
print("...................................")
#6 
first_name = 'Pob'
last_name = 'Daily'
#first_name[0] = "P"
#print(first_name)

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
print("...................................")
#7
variable_password = "theycallme\"crazy\"91"
print(variable_password)
print("...................................")
#8
def get_length(str):
 return len(str)
print(get_length('PAPA'))
print("...................................")
#9
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False  

print(letter_check('уга-буга' , 'е'))
print("...................................")
#10
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False 
#print(contains("watermelon", "melon")) True
#print(contains("watermelon", "berry")) False


def common_letters(string_one, string_two):
    list= []
    for letter in string_one:
        if letter in string_two and not letter in list:
            list.append(letter)
    return list
#11
def username_generator(first_name, last_name):
    username = first_name[0:3] + last_name[0:4]
    return username         
print(username_generator('SERG', 'GAY'))


def password_generator(username):
    username = username_generator('SERG', 'GAY')
    password= username[-1] + username[:-1] 
    return password
print(password_generator(username_generator('SERG', 'GAY')))
