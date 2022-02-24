favour_word = "кукушка"
print(favour_word)
#1
first_name = "Родриго"
last_name = "Вильянуэва"
new_account = last_name[:5]
print(new_account)
temp_password =last_name[2:6]
print(temp_password)
#2
password_generator = first_name[0:3] + last_name[0:3]
new_account = password_generator
print(new_account)
password_generator = first_name[0:3] + last_name[0:3]
temp_password = str(password_generator)
print(temp_password)
#3
company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)
#4
first_name = "ob"
fixed_first_name = "R" + first_name
print(fixed_first_name)
#5
password = "theycallme\"crazy\"91"
print(password)

def get_length(line):
    length = len(line)
    print(length)
#6
def letter_check(word, letter):
    for a in word:
        if a == letter:
            print(True)
        else:
            print(False)
letter_check("jddkdk", "k")

#7
def contains(big_string, little_string):
    if little_string in big_string:
        print(True)
    else:
        print(False)
contains("melon", "lon")

def common_letters(string_one, string_two):
    for letter in string_one:
        for letter1 in string_two:
            if letter == letter1:
                print(letter)
common_letters("banana", "cream")
#8
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