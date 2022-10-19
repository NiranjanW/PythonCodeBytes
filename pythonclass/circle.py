from math import pi
from random import random , seed
import math

class Circle:

    __slots__ = ['diameter']
    version = '0.1' #class variable

    def __init__(self,radius):
        self.radius = radius
    
    # def __init__(self):
    #     return self
    #     # self.radius = radius


    @property
    def radius(self, radius): 
      return radius
    
    @radius.setter
    def radius( self, radius): 
        self.radius = radius


    def  perimeter (self) :
        return  2 * pi* self.radius

    def area(self) : 
        return pi * self.radius ** 2.0

    @staticmethod # attach function to classes
    def angle_to_grade(angle):
        return math.tan(math.radians(angle))  * 100.0

        __perimeter = perimeter #class local reference ( self refers to you not you and your children)
    @classmethod
    def from_bbd(cls,bbd):
        radius = bbd/2.0/math.sqrt(2.0)
        return cls(radius)

class Tire(Circle):

    def perimeter(self): 
        return Circle.perimeter(self) * 1.25

def main():
    # seed(8675309)
    # n =10
    # circles = [ Circle(random()) for i in range(n)]
    # average = sum( c.area() for c in circles)
    # print(f'avg is  {average:.1f}')
    # t = Tire(22)
    # print(t.perimeter())
    c = Circle(10)
    print(c.perimeter())
    c.radius *= 1.1
    print(c.perimeter())

if __name__ == '__main__':
    main()


# 1. Inherit from object()
# 2. Instance Variables for information unique to an instance.
# 3. Class Variables for data shared among all instances.
# 4. Regular Methods need "self" to operate on instance data.
# 5. Class Methods implement alternate constructors. They need "cls" so they can create subclass instances as well.
# 6. Static Methods attach functions to classes. They don't need either "self" or "cls". Static methods improve discoverabiity and require context to be specified.
# 7. @property lets getter and setter methods be invoked automatically by attribute access. This allows Python classes to freely expose their instance variables.
# 8. _slots_ variable implements the Flyweight Design Pattern by suppressing instance dictionaries.
# 9. _DoubleUnders_ for class level references.