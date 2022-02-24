'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def create_spreadsheet(title,row_count=1000):
    print("Создание электронной таблицы с именем" + title)
    print("Создание электронной таблицы с именем" + title + str(row_count))
create_spreadsheet("Загрузки")
create_spreadsheet("Приложения", 10)

def calc_age (current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calc_age(2049,1993)
dads_age = calc_age(2049,1953)
print("Мне", my_age, "лет, а моему отцу", dads_age, "лет")

def get_boundaries(target,margin):
    low_limit = target - margin
    high_limit =  margin + target
    return low_limit,high_limit
low_limit, high_limit = get_boundaries(100,20)
print("Нижний предел:",low_limit,",верхний предел:",high_limit)

current_year = 2048
def calc_age (current_year,birth_year):
    age = current_year - birth_year
    print(age)
print(current_year)
calc_age(2048,1970)

def repeat_stuff(stuff,num_repeats=10):
    returnstatement = stuff * num_repeats
    print(returnstatement)  
repeat_stuff("Row",3)
lyrics = str(repeat_stuff("Row",3)) + "Your Boat"
song = repeat_stuff("Row")