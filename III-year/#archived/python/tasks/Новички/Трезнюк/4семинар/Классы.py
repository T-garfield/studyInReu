#Задание 1
print(type(5))
my_dict = {}
print(type(my_dict))
#Задание 2
class Rules:
    def wash_brain():
        return "Point bristles towards the basin while washing your brushes."
#Задание 3
class Circle:
    pi = 3.14
    def calc(self, radius):
        area = self.pi * radius ** 2
        return area
circle = Circle()
pizza_area = circle.calc(12)
training_table_area = circle.calc(36)
round_room_area = circle.calc(11460)
#Задание 4
class Store: 
    pass
Alternative_rocks = Store()
isabelles_ices = Store()
Alternative_rocks.store_name = 'Альтернативные камни'
isabelles_ices.store_name = "Isabelle's Ices"
#Задание 5
print(dir(5))
def this_fuction_is_an_object():
    pass
print(dir(this_fuction_is_an_object))
#Задание 6 
class Circle:
 pi = 3.14
 def __init__(self, diameter):
    self.radius = diameter / 2
 def __repr__(self):
    return self.radius
 
 def area(self):
    return self.pi * self.radius ** 2
 
 def circumference(self):
    return self.pi * 2 * self.radius
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza.area())
print(teaching_table.area())
print(round_room.area())
#Задание 7
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
    def add_grade(self, grade):
        if(type(grade) is Grade):
            self.grades.append(grade)
roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli",12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
    minimum_passing = 65
    def __init__(self,score):
        self.score = score


new_grade = Grade(100)
pieter.add_grade(new_grade)