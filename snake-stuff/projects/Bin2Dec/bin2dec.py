def main():
  
  invalid_num = []
  for i in range (2 , 10):
    invalid_num.append(str(i))

  while True:
    bin_digit = input("Enter your binary digits or press x to quit: ")

    if bin_digit == "x":
      print("bye bye")
      break
    
    elif not bin_digit.isdigit():
      print(f'{bin_digit} is not valid')
      print(f'You gotta enter binary digits only ')
      continue
    
    elif any(i in bin_digit for i in invalid_num):
      print("That is not a binary string , a binary string only contains 0 or 1s")
      continue

    ## hehe we can use len to determine the length of the digit string
    length = len(bin_digit)
    bin_digit = int(bin_digit)
    
    result = 0 
    for i in range(1 , length + 1):
      result += (bin_digit % 10) * pow(2 , i - 1)
      bin_digit //= 10

    print(result)
      
if __name__ == "__main__":
  main()