import math
import random

def spin_row():
  spin_list =['☀️', '✂️' , '👽' , '🌧️']
  return [random.choice(spin_list) for _ in range(3)]

def print_row(row):
  print("********************")
  print((" | ").join(row))
  print("********************")
  

def get_payout( bet, row ):
  if row[0] == row [1] and row[1] == row[2]:
    print("CONGRATULATIONS YOU HIT THE JACK POT!")
    bet *= 2
    return bet
  else:
    print("NO WINNINGS :[ Try again next time")
    return 0
  
def main():
  balance = 1000
  
  while balance > 0 : 
    print("********************")
    print("*    Slot Machine  *")
    print("********************")
    print(f'Current Balance: ${balance}')
    bet_amount = input("Enter Bet Amount:")
    
    if not bet_amount.isdigit():
      print("You can only input numeric amount! ")
      continue
    
    bet_amount = int(bet_amount)
    
    if bet_amount > balance or bet_amount <= 0  :
      print(f'You can only bet within your balance of {balance}')
      continue
    
    
    balance -= bet_amount
    row = spin_row()
    print_row(row)
    balance += get_payout(bet_amount,row)
  
  print("You are all out of balance")
if __name__ == '__main__':
  main()