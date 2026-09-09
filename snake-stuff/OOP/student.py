from human import Human
class Student(Human): 
  student_class = "3TA1"
 
  def __init__(self , name="", matric="", age = 0):
    self.name = name 
    self.matric = matric
    self.age = age 
    
  def studying(self):
    print(f"{self.name} am studying")
  
