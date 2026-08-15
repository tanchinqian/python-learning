
'''
questions = ("What is 1 + 1 ?", "What is 2 + 2")

options = (("A. 2 ","B. 3", "C. 4"),("A. 3", "B. 4" , "C. 5"))
answers = ("A" , "B")
guesses = []
score = 0 
question_num = 0 

for question in questions:
  print("----------------------------------")
  print(question)
  for option in options[question_num]:
    print(option)
  
  guess = input("Enter your answer : ").upper()
  guesses.append(guess)
  
  if guess == answers[question_num]:
    print("Correct!")
    score += 1
  else:
    print("Incorrect!")
  question_num += 1
  
  
print(f'Final Score : {score}')


print(f'--------------------------')
print(f'        YOUR RESULT       ')
print(f'--------------------------')

print("Answers:" , end = " ")

for answer in answers:
  print(answer , end = " ")
  
print()

print("Guesses:" , end = " ")

for guess in guesses:
  print(guess, end = " ")

'''

menu = {"pizza" : 500, 
        "nachos" : 600,
        "fries" : 800}

cart = []


print('------------------------')
print(f'          MENU         ')
print('------------------------')

for key , value in menu.items():
  print(f'{key:10}: ${value:.2f}' )


while True:
  choice = input("Enter your choice of food (Press q to quit): ").lower()
  
  if choice == "q":
    break
  elif choice in menu is not None:
    cart.append(choice)
    
total = 0 
for food in cart:
  total += menu[food]
  

print(f'Total : {total}')