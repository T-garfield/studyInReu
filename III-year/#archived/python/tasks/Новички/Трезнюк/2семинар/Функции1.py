#Задание 1
def create_spreadsheet(title, row_count = 1000):
    print(f"Создание электронной таблицы с название {title} with {str(row_count)} lines")
create_spreadsheet("Приложения", 10)
#Задание 2
def calc_age (current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)
print(f'Мне {my_age} лет, а моему отцу {dads_age}')
#Задание 3
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
print(f'Нижний предел: {low_limit}, верхний предел: {high_limit}')
#Задание 4
#1)Не работает тк не является глобальной пер. 
# 2)Не работает по той же причине
current_year = 2048
def calc_age(birth_year):
    age = current_year - birth_year
    return age
#6)Работает
print(calc_age(1970))
#Задание 5
def repeat_stuff(stuff, num_repeats = 10):
    return stuff*num_repeats
repeat_stuff("Row", 3)
lyrics = repeat_stuff("Row", 3) + "Your Boat."
song = repeat_stuff("stuff")
print(song)