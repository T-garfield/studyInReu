# 1
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))


# 2
class Rules:
    def wash_brush(self):
        print("Point bristles towards the basin while washing your brushes.")


# 3
class Circle:
    def square(self, radius):
        pi = 3.14
        area = pi * radius ** 2
        print(area)


circle = Circle()
pizza_area = circle.square(12)
training_table_area = circle.square(36)
round_room_area = circle.square(11460)


# 4
class Store:
    pass


Alternative_rocks = Store()
isabelles_ices = Store()
Alternative_rocks.store_name = "Альтернативные камни"
isabelles_ices.store_name = "Isabelle's Ices"


# 5
class FakeDict:
    pass


fake_dict = FakeDict()
fake_dict.attribute = "Cool"
dir(5)


# 6
class Circle:
    pi = 3.14

    def init(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def repr(self, radius):
        print("Круг с радиусом " + radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# 7
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        def add_grade(self, grade):
            if type(grade) is Grade:
                self.grades.append(grade)

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
    minimum_passing = 65
    def __init__(self, score):
        self.score = score

pieter.add_grade(Grade(100))


