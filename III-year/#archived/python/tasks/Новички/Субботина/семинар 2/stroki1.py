#1
favour_word = "треш"
print(favour_word)

#2
first_name = 'Родриго'
last_name = 'Вильянуэва'
new_account = last_name[:5]
print(new_account)
temp_password = first_name[2:6]
print(temp_password)

#3
account_generator = first_name[0:3] + last_name[0:3]
new_account = account_generator
print(new_account)

#4
account_generator = first_name[0:3] + last_name[0:3]
temp_password = str(account_generator)
print(temp_password) 

#5
company_motto = "мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)

#6
first_name = 'Pob'
last_name = 'Daily'
#first_name[0] = "P"
#print(first_name)
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

#7
Rob_password = "theycallme\"crazy\"91"
print(Rob_password)

#8
def get_length(str):
    length = len(str)
    print(length)

#9
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False  
print(letter_check('мир' , 'и'))

#10
def common_letters(string_one, string_two):
    for letter in string_one:
        for letter2 in string_two:
            if letter == letter2:
                print(letter)
common_letters("banana", "cream")

#11
def username_generator(first_name, last_name):
    print(first_name[:3]+last_name[:4])
username_generator("Abe","Simpson") 


def password_generator(password):
    i=-1
    for letter in password:
        print(password[i],end="")
        i=i+1
    print("\n")
password_generator("AbeSimp")
