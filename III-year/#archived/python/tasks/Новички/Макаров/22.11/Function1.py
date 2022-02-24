#1
def create_spreadsheet(title="Загрузки", row_count=1000):
    print("Создание электронной таблицы с названием " + title + str(row_count) + " строк.")
create_spreadsheet(title="Приложения ", row_count=10)

print("-------------------------------------------------------------")

#2
def calc_age(current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)
print("Мне " + str(my_age) + " лет, а моему отцу "+ str(dads_age) +" лет")

print("-------------------------------------------------------------")


#3
def get_boundaries (target, margin):
    low_limit = target-margin
    high_limit = margin+target
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100,20)
print("Нижний предел: "+ str(low_limit) +", Верхний предел: "+ str(high_limit))

print("-------------------------------------------------------------")
#4
def repeat_stuff (stuff, num_repeats = 10):
    statement= stuff*num_repeats
    return statement
repeat_stuff("Row ", 3)
lyrics = repeat_stuff("Row ", 3) + "Your Boat "
song = repeat_stuff (lyrics)
print (song)
