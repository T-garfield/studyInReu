#Задание 1

num = 5

print(type(num))

my_dict = {'key' : 'value'}
print(type(my_dict))

my_list = ['one', 'two']
print(type(my_list))

#Задание 2


class Rules:
    def wash_brush(self):
        print ("Point bristles towards the basin while washing your brushes.")
pag = Rules()
pag.wash_brush()

#Задание 3

class Circle:
   pi = 3.14
   def area(self, radius):
        return  radius ** 2 * self.pi
    
circle = Circle()
pizza_area = circle.area(12)
training_table_area = circle.area(36)
round_room_area = circle.area(11460)

print(pizza_area, training_table_area, round_room_area)

#Задание 4

class Store:
    pass
Alternative_rocks = Store()
isabelles_ices = Store()

Alternative_rocks.store_name = "Альтернативные камни"
isabelles_ices.store_name = "Isabelle's Ices"

one = '{} {}'.format(Alternative_rocks.store_name, isabelles_ices.store_name)

print(one)

#Задание 5
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
    if hasattr (element, 'count'):
        print (str (type (element)) + "имеет атрибут count!")
    else: print (str (type (element)) + "не имеет атрибута count :(")    
 
#Задание 6

num = 5
print(dir(5))

def this_function_is_an_object():
    pass
this_function_is_an_object()

print(dir(this_function_is_an_object))

#Задание 7




class Circle:
 pi = 3.14


 def __init__(self, diameter):
      self.radius = diameter / 2

 def area(self):
      return self.pi * self.radius ** 2

 def circumference(self):
      return self.pi * 2 * self.radius

 def __repr__(self):
     return self.radius 
 

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

#print(medium_pizza, teaching_table, round_room)


#Задание 8

class Student():
    def ___init__(self, name,year):
        self.name = name
        self.year = year
        self.grades = []
    def add_grade (self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)


roger = Student('Roger van der Weyden' ,10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


grade = 100

pieter.grades.add_grade(grade)