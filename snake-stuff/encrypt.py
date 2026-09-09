import string
import random
chars = string.ascii_letters  + string.digits + string.punctuation
chars = list(chars)

key = chars.copy()

random.shuffle(key)



plain_text = input("Please enter text : ")
encrypted_text = ""

for char in plain_text:
  encrypted_text += key[plain_text.index(char)]
  

print(f"Plain Text : {plain_text}")
print(f"Encrypted Text : {encrypted_text}")