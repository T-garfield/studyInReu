
first_name = "Родриго"
last_name = "Вильянуэва"
new_account = last_name[:5]
print(new_account)
temp_password =last_name[2:6]
print(temp_password)

account_generator = first_name[0:3] + last_name[0:3]
new_account = account_generator
print(new_account)

account_generator = first_name[0:3] + last_name[0:3]
temp_password = str(account_generator)
print(temp_password)

company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)

first_name = "ob"
fixed_first_name = "R" + first_name
print(fixed_first_name)

temp_password = "theycallme\"crazy\"91"
print(temp_password)
for letter in temp_password:
    print(letter, end="")

print("\n")
def get_length(password):
    print(len(password))
get_length("asdfaggtr")


def letter_check(word):
        if word.isalpha() == True:
            print("True")
        else:
            print("False")
letter_check("hjkhh")

def contains(big_string, little_string):
    if little_string in big_string:
        print(True)
    else:
        print(False)
contains("asdf", "df")

def common_letters(string_one, string_two):
    for letter in string_one:
        for letter2 in string_two:
            if letter == letter2:
                print(letter)
common_letters("banana", "cream")

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

