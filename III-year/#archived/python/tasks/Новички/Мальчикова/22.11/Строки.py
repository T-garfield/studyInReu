#Списки 1
#Любимое слово
print("-_Любимое слово_-")
favour_word = "Самка"
print("Мое любимое слово -", favour_word)
print("")

#Скрипт
print("-_Скрипт_-")
first_name = "Родриго"
last_name = "Вильянуэва"

new_account = last_name[:5]
print(new_account)

temp_password = last_name[2:6]
print(temp_password)
print("")

#Генератор аккаунта
print("-_Генератор аккаунта_-")
first_name = "Родриго"
last_name = "Вильянуэва"

account_generator = first_name[:3] + last_name[:3]
#print(account_generator)

new_account = account_generator
print(new_account)
print("")

#Генератор пароля
print("-_Генератор пароля_-")
first_name = "Родриго"
last_name = "Вильянуэва"

length_fn=len(first_name)
length_ln=len(last_name)

temp_password = first_name[length_fn-3:] + last_name[length_ln-3:]
print(temp_password)
print("")

#Мечты сбываются
print("-_Мечты сбываются_-")
company_motto = 'Мечты сбываются'
second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)
print("")

#Иммутабельность
print("-_Иммутабельность_-")
first_name = 'Pob'
last_name = 'Daily'
#first_name[0] = "P"
#print(first_name)

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)
print("")

#Espcape-последовательности
print("-_Espcape-последовательности_-")
variable_password = "theycallme\"crazy\"91"
print(variable_password)
print("")

#Интеграция по строкам
print("-_Интеграция по строкам_-")
def get_length(str):
 return len(str)
print(get_length('88005553535'))
print("")

#Строки и условные выражения
print("-_Строки и условные выражения_-")
def letter_check(word, letter):
    if letter in word:
        return True
    else:
        return False  

print(letter_check('Гучи' , 'а'))

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
print(common_letters("Багровый и белый отброшен и скомкан " , 
"в зеленый бросали горстями дукаты ", "а черным ладоням сбежавшихся окон ", "раздали горящие желтые карты.")) 
print("")

#Заключение
print("-_Заключение_-")
def username_generator(first_name, last_name):
    username = first_name[0:3] + last_name[0:4]
    return username         
print(username_generator('Ledy', 'Gaga'))


def password_generator(username):
    username = username_generator('Ledy', 'Gaga')
    password= username[-1] + username[:-1] 
    return password
print(password_generator(username_generator('Ledy', 'Gaga')))
print("")
print("")
print("")

#Строки 2
#Задание
print("-_Выбор элементов списка_-")
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed, '\n', poem_author)
print("")