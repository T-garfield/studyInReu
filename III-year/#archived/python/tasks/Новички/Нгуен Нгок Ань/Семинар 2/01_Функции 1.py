print("*** Задание 1 ***")
def creat_spreadsheet(title, row_count = 1000):
    print("Создание электронной таблицы с именем", title, "with", str(row_count), "lines.")
creat_spreadsheet("Загрузки")
creat_spreadsheet("Загрузки", "10")

print("\n*** Задание 2 ***")
def calc_age(current_year, birth_year):
    return current_year - birth_year
my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)
print("Мне", my_age, "лет, а моему отцу", dads_age, "лет.")

print("\n*** Задание 3 ***")
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
print("Нижний предел:", str(low_limit) + ",", "верхний предел:", str(high_limit))

print("\n*** Задание 4 ***")
current_year = 2048
def calc_age(birth_year):
    age = current_year - birth_year
    return age
age = calc_age(1970)
print("Мне", age, "лет.")

print("\n*** Задание 5.1 ***")
def repeat_stuff(stuff, num_repeats = 10):
    statement = stuff * num_repeats
    return statement
statement = repeat_stuff("Row", 3)
lyrics = statement + " Your Boat."
print(statement)
print(lyrics)

print("\n*** Задание 5.2 ***")
num_repeats = 10
def repeat_stuff(stuff):
    return stuff * num_repeats
song = repeat_stuff("Row")
print(song)