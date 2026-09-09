class Temperature : 
  unit_system = "Celsius"
  
  def __init__(self , degrees):
    self.degrees = degrees
  
  def display(self):
    print(f"{self.degrees}° in system : {self.unit_system}")
    
    
  @staticmethod
  def celsius_to_fahrenheit(c):
    return f"{c * 1.8 + 32 : .1f}"
  
  @classmethod
  def set_unit_system(cls , new_system):
    cls.unit_system = new_system