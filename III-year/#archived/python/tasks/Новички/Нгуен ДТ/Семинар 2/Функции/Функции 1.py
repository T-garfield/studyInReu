# 1
def create_spreadsheet(title):
    print("Создание электронной таблицы с именем " + title)


create_spreadsheet("Загрузки")


def create_spreadsheet(title, row_count="1000"):
    print("Создание электронной таблицы с названием " + title + " with " + row_count + " lines")


create_spreadsheet("Приложения", str(10))
# 2
print()
def calc_age(current_year, birth_year):
    return current_year - birth_year


my_age = calc_age(2049, 1993)
dad_age = calc_age(2049, 1953)
print('Мне ' + str(my_age) + ' лет, а моему отцу ' + str(dad_age) + ' лет')
# 3
print()
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit


low_limit, high_limit = get_boundaries(100, 200)
print('Нижний предел: ' + str(low_limit))
print('Верхний предел: ' + str(high_limit))
# 4
print()
current_year = 2048
def calc_age(birth_year):
    age = current_year - birth_year
    return age


print(calc_age(1970))
# 5
print()
def repeat_stuff(stuff, num_repeats=10):
    returnstatement = stuff * num_repeats
    return returnstatement


lyrics = repeat_stuff('Row', 3) + " Your boat"
song = repeat_stuff('Stuff')

print(lyrics)
print(song)