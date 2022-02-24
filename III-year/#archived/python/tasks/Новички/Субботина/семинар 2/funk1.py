#1
def create_spreadsheet(title,row_count=1000):
    print("Создание электронной таблицы с именем" + title)
    print("Создание электронной таблицы с именем" + title + str(row_count))
create_spreadsheet("Загрузки")
create_spreadsheet("Приложения", 10)

#2
def calc_age (current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calc_age(2049,1993)
dads_age = calc_age(2049,1953)
print("Мне", my_age, "лет, а моему отцу", dads_age, "лет")

#3
def get_boundaries(target,margin):
    low_limit = target - margin
    high_limit =  margin + target
    return low_limit,high_limit
low_limit, high_limit = get_boundaries(100,20)
print("Нижний предел:",low_limit,",верхний предел:",high_limit)

#4
current_year = 2048
def calc_age(current_year, birth_year):
    return current_year - birth_year
print(current_year)
print(calc_age(current_year, 1970))

#5
def repeat_stuff(stuff,num_repeats=10):
    returnstatement = stuff * num_repeats
    print(returnstatement)  
repeat_stuff("Row",3)
lyrics = str(repeat_stuff("Row",3)) + "Your Boat"
song = repeat_stuff("Row") 