import random

'''
lowest_number = 1 
highest_number = 100
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("Number Guessing Game!")
print(f'Guess a number between {lowest_number} and {highest_number}')

while is_running:
  
  guess = input("Enter your guess:")
  if guess.isdigit():
    guess = int(guess)
    guesses += 1
    if guess == answer:
      
      print(f'Congrats! {answer} is correct!')
      print(f'You took {guesses} number of guesses')
      break
    elif guess > answer:
      print(f'Your guess is higher than the answer')
    elif guess < answer:
      print(f'Your guess is lower than the answer')
    else:
      print("debug1")
    
    
  else:
    print("You can only input integer numbers!")
    guess = input("Enter your guess:")
'''

options = ("rock" , "paper" , "scissors")
comp_move = random.choice(options)


print(comp_move)
is_running = True
while is_running :
  print(f'Welcome to the RPS game!')
  print(f'Please choose your move options')
  print(f'A. Rock ')
  print(f'B. Paper ')
  print(f'C. Scissors')
  print(f'D. Quit')
  choice = input("Options : ").upper()
  
  
  if (choice == 'A' and comp_move == 'scissors') or   (choice == 'B' and comp_move == 'rock') or (choice == 'C'  and comp_move == 'paper'):
    print("You Win!")
  else:
    print("You Lose!")
  
  continue_selection = input("Do you still want to play? (y/n)").lower() 
  
  if(continue_selection == 'y'):
    continue
  else:
    break
  
    



