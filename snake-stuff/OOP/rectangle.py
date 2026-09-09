class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height

  @property
  def width(self): ## This is not a function call 
    return f"{self._width: .1f} cm"

  @property
  def height(self):
    return f"{self._height: .1f} cm"
  
  @width.setter
  def width(self , new_width):
    if new_width < 0 :
      print("New width must be larger than or equal 0")
    else:
      self._width = new_width
      
  @height.setter
  def height(self , new_height):
    if new_height < 0 :
      print("New heigth must be larger than or equal to 0")
    else: 
      self._height = new_height
  
  @width.deleter
  def width(self):
    del self._width
    print("width deleted")
    
  @height.deleter
  def height(self):
    del self._height
    print("height deleted")

def main():
  r1 = Rectangle(3,4)
  
  print(r1.width)
  del r1.width
  r1.width = 3 
  print(r1.width)
  
if __name__ == "__main__":
  main()
