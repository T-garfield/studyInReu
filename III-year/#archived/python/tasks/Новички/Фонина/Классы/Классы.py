print("#задание 1\n")
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = ""
print(type(my_list))
#my_list1 = []
#print(type(my_list1))
#my_tuple = ()
#print(type(my_tuple)) 
# терминал скажет что это кортеж (неизменная последовательность)
print("\n")

print("#задание 2\n")
class Rules():
  def wash_brush(self):
    return "Point bristles towards the basin while washing your brushes."
wash_brushes = Rules()
print(wash_brushes.wash_brush())
print("\n")

print("#задание 3\n")

class Circle():
  pi = 3.14
  def area(self, diameter):
    return self.pi * (diameter/2) ** 2
  
circle = Circle()

pizza_radius = 12
teaching_table_radius = 36
round_room_radius = 11460

pizza_area = print(circle.area(pizza_radius))
teaching_table_area = print(circle.area(teaching_table_radius))
round_room_area = print(circle.area(round_room_radius))
print("\n")

print("#задание 4\n")
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

working_string = "{} \n{}".format(alternative_rocks.store_name, isabelles_ices.store_name)
print(working_string)

print("\n")

print("#задание 5\n")
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  if hasattr(element, "count"):
    print (str (type (element)) + "имеет атрибут count!")
  else:
    print (str (type (element)) + "не имеет атрибута count :(")
print("\n")

print("#задание 6\n")
print(dir(5))
print("\n")
def this_function_is_an_object(self):
  return self
print("\n")
print(dir(this_function_is_an_object))
print("\n")

print("#задание 7\n")
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
print("\n")

print("#задание 8\n")
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

print("\n")