import math

#1
my_dict = {}
my_list = []

print(type(5))
print(type(my_dict))
print(type(my_list))
#2
class Rules:
    def wash_brush(self):
        return "Point bristles towards the basin while washing your brushes."
pravila = Rules()

print(pravila.wash_brush())
#3
class Circle: 
    pi = math.pi
    def square(self, radius):
        area = self.pi*radius**2
        return area

circle = Circle()
pizza_area = circle.square(12)
training_table_area = circle.square(36)
round_room_area = circle.square(11460)

print(pizza_area)
print(training_table_area)
print(round_room_area)

#4
class Store:
    pass
alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = 'Альтернативные камни'
isabelles_ices.store_name = "Isabelle's Ices"
#5
def this_function_is_an_object(obj):
    return obj
print(dir(5))
print(dir (this_function_is_an_object))
#6
class Circle:
    pi = math.pi
    def __init__(self, diameter):
        self.radius = diameter / 2
    def area(self):
        return self.pi * self.radius ** 2
    def circumference(self):
        return self.pi * 2 * self.radius
    def __repr__ (self):
        return str(f'круг с радиусом {self.radius}') 

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
print(medium_pizza.area())
print(teaching_table.area())
print(round_room.area())
#7
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
    def add_grade(self, grade):
            if type(grade) == Grade:
                self.grades.append(grade)
    def __repr__ (self):
        return str(f'{self.name} year {self.year} {self.grades}')
    
class Grade:
    minimum_passing = 65
    def __init__(self, score):
        self.score = score

roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

grade = Grade(100)
pieter.add_grade(grade)

print(pieter)


 