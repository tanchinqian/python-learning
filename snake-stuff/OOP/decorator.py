def add_whipped_cream(func):
  def wrapper(*args, **kwargs):
    print("Adding whipped cream 🍦")
    func(*args, **kwargs)
  return wrapper

def add_syrup(func):
  def wrapper(*args, **kwargs):
    print("Drizzling caramel syrup")
    func(*args,**kwargs)
  return wrapper
    
@add_syrup
@add_whipped_cream
def make_coffee(size):
  print(f"Serving a {size} coffee ☕")

def main():
  make_coffee(3)

if __name__ == "__main__":
  main()
