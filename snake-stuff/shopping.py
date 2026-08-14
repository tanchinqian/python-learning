foods = []
prices = [] 
total = 0 

while True:
  food = input(f'Enter the name of your food (Press q to quit) : ')
  
  if food.lower() == 'q':
    break
  foods.append(food)
  
  price_inputFlag = True
  price = int(input(f'Enter the price of the food : '))
  
  while price_inputFlag:
    
    if price < 0 :
      print(f'Prices below 0 are not allowed!')
      price = int(input(f'Enter the price of the food : '))
    else:
      price_inputFlag = False
      
    prices.append(price)
    total += price
  
  
print("----- YOUR CART -----")
for food in foods:
  print ( food , end=" ")
print(' ')
print (f'Total cost : {total}')

    
    
  

  