from abc import ABC , abstractmethod
import math 
class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass
  
  @abstractmethod
  def perimeter(self):
    pass
  
class Rectangle(Shape):
  def __init__(self , width , height):
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height
  
  def perimeter(self):
    return 2 * self.width + 2 * self.height
  
class Circle(Shape):
  
  def __init__(self , radius):
    self.radius = radius
    
  def area(self):
    return math.pi * pow(self.radius , 2)
    
  def perimeter(self):
    return 2 * math.pi * self.radius
  
def print_shape_details(shape):
  print(f"Area : {shape.area() :.2f}")
  print(f"Perimeter : {shape.perimeter() : .2f}")