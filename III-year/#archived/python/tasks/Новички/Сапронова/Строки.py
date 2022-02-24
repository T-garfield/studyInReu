favour_word = "independence"
print(favour_word)

first_name = "Родриго"
last_name = "Вильянуэва"
new_account = last_name[:5]
temp_password = last_name[3:7]

def account_generator (first, second):
    new_account = first[:3] + second[:3]
    print(new_account)
account_generator(first_name, last_name)

def  password_generator(first, second):
    length1 = len(first)
    length2 = len(second)
    temp_password = first[length1-3:] + second[length2-3:]
    print(temp_password)
password_generator(first_name, last_name)

company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

first_name = "Роб Дейли"
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

rob_password = "theycallme\"crazy\"91"
print(rob_password)

def get_length(line):
    length = len(line)
    print(length)

def letter_check(word, letter):
    for ltr in word:
        if ltr == letter:
            print(True)
        else:
            print(False)
letter_check("abcde", "d")

def contains(big_string, little_string):
    print(little_string in big_string)
contains("watermelon", "melon")

def common_letters(string_one, string_two):
    for ltr in string_one:
        for ltr1 in string_two:
            if ltr == ltr1:
                print(ltr)

common_letters("cream", "banana")

def username_generator(first_name, last_name):
    if len(first_name) > 3 and len(last_name) > 4:
        use_n = first_name[:3] + last_name[:4]
    elif len(first_name) <= 3:
        use_n = first_name + last_name[:4]
    elif len(last_name) <= 4:
        use_n = first_name[:3] + last_name
    print(use_n)

def  password_generator(use_n):
        password = use_n[-1] + use_n[0:-1]
        print(password)

username_generator("Elena", "Romanova")
password_generator("EleRoma")

poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)
