# CS-1030 Foundations of Computing  
# 7-6 Challenge: Control Structures
# Author: Linda Volquez  
# 1 of 2 - Name Pyramid 

def print_name_pyramid(name):
  for i in range(1, len(name) + 1):
      print(name[:i])

def main():
  name = input("Enter your name: ")
  print_name_pyramid(name)

if __name__ == "__main__":
  main()