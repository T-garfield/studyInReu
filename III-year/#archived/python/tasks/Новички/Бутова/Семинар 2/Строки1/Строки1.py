#1
first_name='Родриго' 
last_name='Вильянуэва'
new_account=last_name[:5]
temp_password=last_name[2:6]
print(new_account, temp_password)
#2
def temp_password(first_name,last_name):
    new_account=first_name[:3]+last_name[:3]
    return new_account
print(temp_password('Родриго', 'Вильянуэва'))
#3
def password_generator(first_name,last_name):
    temp_password=first_name[-3:]+last_name[-3:]
    return temp_password
print(password_generator('Родриго', 'Вильянуэва'))

#4
company_motto='Мечты сбываются'
second_to_last=company_motto[-2]
final_word=company_motto[-4:]
print(second_to_last,final_word)

#5
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
#6
counter=0
def get_length(str):
    return len(str)
print(get_length('dsafewqgrewg'))

#7
def letter_check(word,letter):
    if letter in word:
        return True
    else:
        return False
print(letter_check('rock','l'))
#8
def contains(big_string,little_string, ):
    if little_string in big_string:
        return True
    return False
print(contains("watermelon", "melon"))

def common_letters(string_one, string_two):
    for i in range(0, len(string_one)):
        if string_one[i] in string_two:
             print(string_one[i])
print(common_letters('qwewe','3213fw'))

#9
def username_generator(first_name,last_name):
    if len(first_name)<3 or len(last_name)<4:
        return last_name, first_name
    else:
        return first_name[:3]+last_name[:4]
print(username_generator("Abe","Simpson"))

def password_generator(password):
    i=-1
    for letter in password:
        print(password[i],end="")
        i=i+1
password_generator("AbeSimp")