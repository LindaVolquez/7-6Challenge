# CS-1030 Foundations of Computing  
# 7-6 Challenge: Control Structures
# Author: Linda Volquez  
# 2 of 2 - Guidance Counselor

# Convert the first letter of the last name to uppercase
def find_counselor(lastName):
  
  firstLetter = lastName[0].upper()

  # Compare the first letter within specified ranges and return the counselor accordingly
  if 'A' <= firstLetter <= 'D':
      return "Marci Thomas"
  elif 'E' <= firstLetter <= 'K':
      return "Robert Hancock"
  elif 'L' <= firstLetter <= 'R':
      return "John Caine"
  elif 'S' <= firstLetter <= 'Z':
      return "Lacy Peterson"
  else:
      return "Last Name out of ranges"

def main():
  # Print the program header
  print("Boneville High School Counselor")

  # Prompt the user to enter their last name
  lastName = input("Enter your last name: ")

  # Find and print the counselor for the entered last name
  counselorName = find_counselor(lastName)
  print("Your counselor is", counselorName)

if __name__ == "__main__":
  main()
