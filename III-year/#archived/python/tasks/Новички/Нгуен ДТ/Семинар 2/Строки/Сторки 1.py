# 1
flavour_word = 'love'
print(flavour_word)

# 2
print()
first_name = 'Родриго'
last_name = 'Вильянуэва'
new_account = last_name[:5]
temp_password = last_name[3:7]

# 3
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]
new_account = account_generator('Nguyen', 'DucT')
print(new_account)

# 4
print()
def password_generator(first_name, last_name):
    return first_name[-3:] + last_name[-3:]
temp_password = password_generator('Nguyen', 'DucT')
print(temp_password)

# 5
print()
company_motto = 'Мечты сбываются'
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# 6
print()
first_name = "Р"
fixed_first_name = first_name + 'об'
print(fixed_first_name)

# 7
print()
new_password = 'theycallme\'crazy\'91'
print(new_password)

# 8
print()
def get_length(num):
    return print(len(num))
get_length('qwerty')

# 9
print()
def letter_check(word, letter):
    for words in word:
        if letter == words:
            return True
print(letter_check('abc', 'c'))

# 10
print()
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False
def common_letters(string_one, string_two):
    for words in string_one:
       if words in string_two:
           print(words)
print(common_letters("banana", "cream"))

# 11
print()
def username_generator(first_name, last_name):
    if len(first_name) >= 3 and len(last_name) >= 4:
        return first_name[:3] + last_name[:4]
    else:
        return first_name + last_name
print(username_generator('Abe', 'Simpson'))
print()
password = []
def password_generator(username):
    i=-1
    for letter in username:
        password.append(username[i])
        i -= 1
    print(password)
password_generator('AbeSimp')
