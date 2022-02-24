print("*** Задание 1 ***")
favour_word = "Hello world"
print(favour_word)


print("\n*** Задание 2 ***")
first_name = 'Родриго'
last_name = 'Вильянуэва'
new_account = last_name.lower()[:5]
temp_password = last_name[3:7]
print(new_account)
print(temp_password)

print("\n*** Задание 3 ***")
first_name = 'Родриго'
last_name = 'Вильянуэва'
new_account = last_name.lower()[:5]
account_generator = first_name.lower()[:3] + last_name.lower()[:3]
new_account = account_generator
print(new_account)

print("\n*** Задание 4 ***")
first_name = 'Родриго'
last_name = 'Вильянуэва'
temp_password = last_name[3:7]
password_generator = first_name.lower()[len(first_name)-3:] + last_name.lower()[len(last_name)-3:]
temp_password = password_generator
print(temp_password)

print("\n*** Задание 5 ***")
company_motto= "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)

print("\n*** Задание 6 ***")
first_name = 'Роб'
fixed_first_name = "R" + first_name[-(len(first_name)-1):]
print(fixed_first_name)

print("\n*** Задание 7 ***")
password = "theycallme\"crazy\"91"
print(password)

print("\n*** Задание 8 ***")
while True:
    def get_lenth(lenth):
        return len(lenth)
    string = input("Введите строку: ")
    print("Количество символов в строке:", get_lenth(string))
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задание 9 ***")
while True:
    def letter_check(word, letter):
        counter = 0
        for i in word:
            if i == letter:
                counter = counter + 1
        if counter == 0:
            print("Слово содержит букву: False")
        else: print("Слово содержит букву: True")
    word = input("Введите слово: ")
    letter = input("Введите тестироваемую букву: ")
    letter_check(word, letter)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задание 10.1 ***")
while True:
    def contains(big_string, little_string):
        if little_string in big_string:
            print("Слово содержит букву: True")
        else:
            print("Слово содержит букву: False")
    big_string = input("Введите слово: ")
    little_string = input("Введите тестироваемую букву: ")
    contains(big_string, little_string)
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задание 10.2 ***")
while True :
    def common_letters(string_one, string_two):
        list_one = []
        list_two = []
        for i in string_one:
            list_one.append(i)
            return list_one
        for i in string_two:
            list_two.append(i)
            return list_two
    string_one = input("Введите первую строку: ")
    string_two = input("Введите вторую строку: ")
    common_letters(string_one, string_two)
    common = []
    for a in string_one:
        for b in string_two:
            if a == b:
                common.append(b)
    def unique_common(fx):
        list = []
        for x in fx:
            if x not in list and not list.append(x):
                return list
    fx = common
    print("Общие буквы:", unique_common(fx))         
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break

print("\n*** Задание 11 ***")
while True: 
    def username_generator(first_name, last_name):
        if len(first_name) >= 3:
            for i in first_name:
                a = first_name[:3]
        else: 
            a = first_name
        if len(last_name) >= 4:    
            for i in last_name:
                b = last_name[:4]
        else:
            b = last_name
        user = a + b
        return user
    first_name = input("Имя пользователя: ")
    last_name = input("Фамилия пользователя: ")
    user = username_generator(first_name, last_name)
    print("Имя пользователя:", user)

    def password_generator(user):
        password = ""
        for i in range(len(user)):
            password += user[i-1]
        return password
    print("Временный пароль:", password_generator(user))
    again = input("Еще раз? (д/н): ")
    if again != "д":
        break
