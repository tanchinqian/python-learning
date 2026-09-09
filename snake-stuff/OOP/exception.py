class AlreadyRetiredError(Exception):## inherits from the exception class
  
  pass
  
def process_age(age_str):
  try: 
    age = int(age_str)
    if age > 65:
      raise AlreadyRetiredError("Already Retired")
    else:
      years_left = 65 - age
      print(f"Years until retirement: {years_left}")
  except (TypeError , ValueError):
    print("Invalid input! Please enter a number")
  except AlreadyRetiredError as e:
    print(f"{e}")
  except Exception:
    print("An unexpected error occurred.")
  finally:
    print("Processing Complete")
    
    

def main():
  
  # Test 1: Normal input
  process_age("25")
  # Output:
  # Years until retirement: 40
  # Processing complete.

  # Test 2: Invalid string
  process_age("abc")
  # Output:
  # Invalid input! Please enter a number.
  # Processing complete.

  # Test 3: Age over retirement
  process_age("70")
  # Output:
  # Already retired!
  # Processing complete.
      
  
    

if __name__ == "__main__":
  main()