from student import Student
from temperature import Temperature
from shopping import CartItem
def main():
   item1 = CartItem("Wireless Mouse", 25.0, 2)
   item2 = CartItem("Gaming Monitor", 300.0, 1)
   item3 = CartItem("Wireless Mouse", 25.0, 5)

   # Test string representation
   print(str(item1))
   # Output: 2 x Wireless Mouse ($25.0 each)

   # Test equality
   print(item1 == item3)
   # Output: True

   # Test ordering (Total cost comparison)
   print(item1 < item2)
   # Output: True (50.0 < 300.0)

   # Test addition
   print(item1 + item2)
   # Output: 350.0

   # Test membership (case-insensitive)
   print("mouse" in item1)
   # Output: True

   # Test key lookup
   print(item1["total"])
   # Output: 50.0

   print(item1["unit_price"])
   # Output: 25.0
if __name__ == "__main__":
  main()