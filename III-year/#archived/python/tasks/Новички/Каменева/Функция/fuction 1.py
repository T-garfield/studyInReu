#Задание 1

def create_spreadsheet ( title, row_count):
    print("«Создание электронной таблицы с именем", title,"with", str(row_count), "lines")

create_spreadsheet("Загрузки", 1000)

create_spreadsheet(title = "Приложения", row_count = 10)

#Задание 2
def calc_age (current_year, birth_year):
    return current_year-birth_year

age = calc_age(2021,2001)  

my_age = calc_age(2049,1993)

dads_age = calc_age(2049,1953)

print("Мне", my_age,"лет, а моему отцу", dads_age, "лет")

#Задание 3

def get_boundaries (target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit

low_limit, high_limit = get_boundaries(100,20)

print("Нижний предел:", low_limit," верхний предел:", high_limit)

#Задание 4

current_year = 2048 

def calc_age (birth_year):
 age = current_year - birth_year
 return age

print(calc_age(2000))

#Задание 5
num_repeats = 10
def  repeat_stuff(stuff, num_repeats):
    returnstatement = stuff * num_repeats
    
    lyrics = repeat_stuff("Row", 3), "Your Boat."
    song = repeat_stuff(stuff="")
    print(returnstatement,lyrics,song)

repeat_stuff("Row", 3)



