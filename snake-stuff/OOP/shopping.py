class CartItem :
  
  def __init__(self , name , price , quantity):
    self.name = name 
    self.price = price 
    self.quantity = quantity
  
  def __str__(self):
    return f"{self.quantity} * {self.name} ($ {self.price} each )"
  
  def __eq__(self, other):
    return self.name == other.name and self.price == other.price
  
  def __lt__(self , other):
    return self.price * self.quantity < other.price * other.quantity
  
  def __gt__(self , other):
    return self.price * self.quantity > other.price * other.quantity
  
  def __add__(self, other):
    return self.price * self.quantity +  other.price * other.quantity
  
  def __contains__(self, item):
    return item.lower() in self.name.lower()
  
  def __getitem__(self, key):
    if key == "total" :
      return self.price * self.quantity
    elif key == "unit_price" : 
      return self.price
    else :
      return f"{key} was not found"
    