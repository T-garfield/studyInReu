#Задание 1


favour_word = "Фенечка"
print(favour_word)

#Задание 2
first_name = 'Родриго'
last_name = 'Вильянуэва'

new_account = last_name[:5]

print(new_account)

temp_password = first_name[2:6]

print(temp_password)

#Задание 3

def account_generator(first_name, last_name):
    first  = first_name[0:3]
    last  = last_name[0:3]

    new_account = first + last

    print(new_account)

account_generator(first_name, last_name)   

#Задание 4

def  password_generator(first_name, last_name):
    length = len(first_name)
    length1 = len(last_name)
    temp_password = first_name[length-3:] + last_name[length1-3:]

    print(temp_password)
password_generator(first_name, last_name)


#Задание 5

company_motto= 'Мечты сбываются'

second_to_last = company_motto[-2] 

final_word = company_motto[-4:]

print(second_to_last)
print(final_word)

#Задание 6
first_name = 'gob'

fixed_first_name = 'R' + first_name[-2:]

print(fixed_first_name)

#Задание 7

password  = "theycallme\"crazy\"91"

#Задание 8

def get_length (word):
    count = len(word)
    print(count)

get_length('word')     

#Задание 9

def letter_check( word, letter):
    for count in word:    
        if count == letter:
            print(True) 
          
     
letter_check('word', 'o')                    
