import os
import json
import csv
def main():
  employee = { 
            "name":"Spongebob",
            "age" :30,
            "job":"cook"
            }
  employees = [["Name","Age","Job"],
               ["Spongebob",30,"Cook"],
               ["Patrick",37,"Unemployed"],
               ["Sandy",27,"Scientist"],
               ]
  file_path = "snake-stuff/file-stuff/output.csv"
  try:
    with open(file=file_path , mode="w" ,newline ="") as file:
      writer = csv.writer(file)
      #json.dump
      #file.write
      for row in employees:
        writer.writerow(row)
      print(f"csv file {file_path} was created")
      
      
      
  except FileExistsError:
    print("File already exists")
  finally:
    print("Processing done")

if __name__ == "__main__":
  main()