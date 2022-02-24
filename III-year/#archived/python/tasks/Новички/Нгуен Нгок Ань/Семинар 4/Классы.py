print("*** Задание 1 ***")
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

print("\n*** Задание 2 ***")
class Rules:
    wash_brush = "Point bristles towards the basin while washing your brushes."
    print(wash_brush)

print("\n*** Задание 3 ***")
class Circle:
    pi = 3.14
    def square(self, radius):
        self.radius = radius
        area = self.pi*(self.radius**2)
        return area
circle = Circle()
pizza_area = 12
training_table_area = 36
round_room_area = 11460
pizza = circle.square(pizza_area)
table = circle.square(training_table_area)
room = circle.square(round_room_area)
print(f"Площадь средней пиццы 12 дюймов в диаметре: {pizza}")
print(f"Площадь учебного стола размером 36 дюймов: {table}")
print(f"Площадь зрительного зала Круглой комнаты, 11460 дюймов в диаметре: {room}")

print("\n*** Задание 4 ***")
class Store:
    pass
alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Альтернативные камни"
isabelles_ices.store_name = "Isabelle's Ices"
print(f"{alternative_rocks.store_name}, {isabelles_ices.store_name}")

print("\n*** Задание 5 ***")
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for i in range(len(can_we_count_it)):
    if hasattr(can_we_count_it[i],'count') == True:
        print(str(type(can_we_count_it[i])) + " имеет атрибут count!")
    if hasattr(can_we_count_it[i],'count') == False:
        print(str(type(can_we_count_it[i])) + " не имеет атрибут count!")

print("\n*** Задание 6 ***")
print(dir(5))
this_function_is_an_object = [1,2,3]
print(this_function_is_an_object)
print(dir(this_function_is_an_object))

print("\n*** Задание 7 ***")
pi = 3.14
class Circle:
    def __init__(self, diameter):
        self.radius = diameter/2
    def __repr__(self):
        return self.radius
    def area(self):
        return pi*self**2
    def circumference(self):
        return pi*2*self
medium_pizza = Circle.area(12)
teaching_table = Circle.area(36)
round_room = Circle.area(11460)
print(f"Площадь средней пиццы 12 дюймов в диаметре: {medium_pizza}")
print(f"Площадь учебного стола размером 36 дюймов: {teaching_table}")
print(f"Площадь зрительного зала Круглой комнаты, 11460 дюймов в диаметре: {round_room}")

print("\n*** Задание 8 ***")
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grade = {}
    def __repr__(self):
        return self.name + self.year
roger = Student("Roger van der Weyden, ", "year 10")
sandro = Student("Sandro Botticelli, ", "year 12")
pieter = Student("Pieter Bruegel the Elder, ", "year 8")
print(roger)
print(sandro)
print(pieter)
class Grade(Student):
    minimun_passing = 65
    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
    def __repr__(self):
        return self.name + self.year + self.score
roger = Grade("Roger van der Weyden, ", "year 10, ", "grade 100")
print(roger)