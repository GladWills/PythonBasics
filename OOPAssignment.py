#ASSIGNMENT 1
""" specifically implement a base class called shape, and child classes for
Circle, Rectangle and Triangle.
...........
Provide methods to initialise each class, and methods to return the area 
and perimeter of each class.
...........
Write some test code for each shape, printing out the properties and calculated area
and perimeter.
"""

       
import math                              #need this for Pi

class shape:
    def __init__(self):
        self.size = 0      
        pass                              #skip for now
    def area(self):
        return 0                          #just putting 0 for now
    def perimeter(self):
        return 0

#Circle Class Using Shape........
class Circle(shape):
    def __init__(self, radius):                
        self.radius = radius
    def area(self):                         #Pi*r*r
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

#test run shape
circle = Circle(7)
print("Circle - Radius:", circle.radius)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())



#Rectangle Class
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length               #storing length and width
        self.width = width
        self.total = length + width
    def area(self):                        #area = L*W  
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

#Test the Shape
#length = 2, width = 4
rectangle = Rectangle(2,4)  
print("Rectangle - Length:", rectangle.length, "Width:", rectangle.width)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


    
#triangle Class Shape......   #this is a bit more complex for me; 
class Triangle(shape):         #Recall Triangle has 3 sides (s=sides)
    def __init__(self):
        self.size = 0          #maybe size
        pass
    def area(self):            #area = 1/2 * base * height
        return 0               #just putting 0 for now
    def perimeter(self):       #perimeter = a + b + c
        return 0

# Test the Triangle shape
triangle = Triangle(4, 6)      #base = 4, height = 6
print("Triangle - base:", triangle.base, "height:", triangle.height)
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())
