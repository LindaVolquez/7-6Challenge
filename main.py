# main.py
# Import the programs

import GuidanceCounselor
import NamePyramid

def main():
    while True:
        print("\nMenu:")
        print("1. Name Pyramid")
        print("2. Guidance Counselor")
        print("3. Mini Golf")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
          NamePyramid.main()
        elif choice == "2":
          GuidanceCounselor.main()
        elif choice == "3":
          print("Mini Golf has not been implemented yet.")  
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
