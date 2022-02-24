
print(type(5))
my_dict = {}
print(type(my_dict))
my_list =[]
print(type(my_list))

class Rules:
    def wash_brush(self):
        print("Point bristles towards the basin while washing your brushes.")
instance = Rules()
instance.wash_brush()

class Circle:
    pi = 3.14
    def area(self,radius):
       area = self.pi * radius ** 2
       return area
circle = Circle()
pizza_area = circle.area(12)
training_table_area = circle.area(36)
round_room_area = circle.area(11460)
print(pizza_area)
print(training_table_area)
print(round_room_area)

class Store:
    pass
Alternative_rocks = Store()
isabelles_ices = Store()
Alternative_rocks.store_name = "Альтернативные камни"
isabelles_ices.store_name = "Isabelle's Ices"
print(Alternative_rocks.store_name)
print(isabelles_ices.store_name)


can_we_count_it = [{"s": False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
class NoCustomAttributes:
    pass
can_we_count_it = NoCustomAttributes() 
for element in [{"s": False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]: 
    if hasattr(can_we_count_it,"count")==True:
        print(str(type(element))+"имеет атрибут count!")
    else:
        print(str(type(element))+"не имеет атрибута count(")
  
print(dir(5))
print("\n")
def this_function_is_an_object():
    print(dir(this_function_is_an_object))
this_function_is_an_object()

class Circle:
    pi = 3.14
    def __init__(self, diameter):
        self.radius = diameter / 2
    def __repr__(self):
        return self.pi * self.radius ** 2
    def circumference(self):
        return self.pi * 2 * self.radius
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(pizza_area)
print(training_table_area)
print(round_room_area)


class Student:
    def __init__(self,name,year):
        self.name = name
        self.year = year
        self.grades = []
    def __repr__(self):
        return self.name+", year "+str(self.year)
    def add_grade(self,grade):
        if isinstance(grade,Grade) == True:
            self.grades.append(grade)
            return self.grades
        else:
            pass
    def __repr__(self):
        return self.grades


class Grade:
    minimum_passing = 65
    def __init__(self,score):
        self.score = score

roger = Student("Roger van der Weyden",10)
sandro = Student("Sandro Botticelli",12)
pieter = Student("Pieter Bruegel the Elder",8)
print(roger)
print(sandro)
print(pieter)

grade = Grade(100)
pieter.add_grade(grade)
