#Задание1
def  create_spreadsheet (title, row_count = 1000):    
    print('Создание электронной таблицы с именем ' + title + ' with ' + str(row_count) + ' lines ')
create_spreadsheet('"Загрузки"')
create_spreadsheet ('«Приложения»', row_count = 10)
#Задание2
def calc_age (current_year, birth_year):
    return current_year - birth_year
my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)

print("Мне ", my_age, " лет, а моему отцу " ,dads_age, "лет")
#Задание3
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100,20) 
print('Нижний предел: ', low_limit,' верхний предел: ', high_limit)
#Задание4
current_year = 2048
def calc_age (birth_year):
 age = current_year - birth_year
 return age
print(calc_age(1970))

print(current_year)
#Задание5

def repeat_stuff(stuff, num_repeats = 10):
    returnstatement = stuff * num_repeats
    return returnstatement
lyrics = repeat_stuff('Row', 3) + " Your Boat."
print(lyrics)
song = repeat_stuff('Row')
print(song)







