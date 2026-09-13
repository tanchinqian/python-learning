import requests
import os , json
base_url = 'https://pokeapi.co/api/v2/pokemon/'
file_path = ''
pokemon_name = input("Enter a valid pokemon name : ")
pokemon_name = pokemon_name.lower()



def fetch_pokemon_data(name):
  
  url = f'{base_url}{name}'
  response = requests.get(url)
  
  if (response.status_code == 200 ):
    pokemon_data = response.json()
    
    with open(file=file_path , mode="w") as file : 
      pass
    
    return pokemon_data

  else:
    print(f"Failed to retrieve data :  {response.status_code}")
  

pokemon_info = fetch_pokemon_data(pokemon_name)

print(pokemon_info['id'])