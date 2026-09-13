
import os
import json
import csv
file_path = 'snake-stuff/file-stuff/output.csv'

try:
  with open(file=file_path,mode='r') as file:
    #content = json.load(file)
    
    content = csv.reader(file)
    for row in content:
      print(row[2])
    
except FileNotFoundError as e :
  print(f'{e}')