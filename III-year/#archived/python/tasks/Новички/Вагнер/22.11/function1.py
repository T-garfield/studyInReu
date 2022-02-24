#1
def create_spreadsheet(title): print("Создание электронной таблицы с именем " + title + ".")
create_spreadsheet("Загрузки")
def create_spreadsheet(title, row_count = "1000"): row_count = str(row_count) and print("Создание электронной таблицы с именем " + title + ". Количество строк: " + str(row_count) + ".")
create_spreadsheet("Приложения", 10)
print()

#2
def calc_age(birth_year, current_year = 2049):
  return current_year - birth_year
my_age = str(calc_age(1993))
dads_age = str(calc_age(1953))
print("Мне " + my_age + " лет, а моему отцу - " + dads_age + ".")

#3
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)
low_limit = str(low_limit)
high_limit = str(high_limit)
print("Нижний предел: " + low_limit + " Верхний предел: " + high_limit + ".")

#4
current_year = 2048
def calc_age(birth_year):
  age = current_year - birth_year
  return age
print(calc_age(1970))


#5
def repeat_stuff(stuff, num_repeats = 10):
  return stuff * num_repeats
print(repeat_stuff("Row", 3))
lirycs = repeat_stuff("Row", 3) + " Your boat"
song = repeat_stuff(lirycs)
print(song)
