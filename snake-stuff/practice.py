"""length = float(input("Enter your length : "))
width = float (input("Enter your width : ")) 
print(f'Area :   {length * width}')"""

result = 0 
first_num = int(input("Enter your first number : "))
second_num = int(input("Enter your second number : "))

symbol = input("Enter your symbol of choice ( + - * / )")


if ( symbol == '+'):
  result = first_num + second_num
elif ( symbol == '-'):
  result = first_num - second_num
elif ( symbol == '*'):
  result = first_num * second_num
elif ( symbol == '/'):
  if ( second_num == 0):
      print('This is not allowed')
  result = first_num // second_num
  
print(f'The result of {first_num} {symbol} {second_num} is {result}')
