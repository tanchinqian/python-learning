import os


def main():
  file_path = 'plain.txt'
  if os.path.exists(file_path):
    print("File exists")
  else:
    print("File does not exist")
  

if __name__ == "__main__":
  main()