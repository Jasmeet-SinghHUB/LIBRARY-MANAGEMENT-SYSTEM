#now in this we will connec this file as its acts as main file for overall project
from add_books import add_books
from issue_books import issue_books
from show_books import show_books
from return_books import return_books
def library():
    while True:
        print("\n1. Add Books")
        print("\n2. Show Books")
        print("\n3. Issue Books")
        print("\n4. Return Books")
        print("\n5. Exit")   

        choice = int(input("Enter your choice: "))
        if choice ==1: add_books()
        elif choice ==2: show_books()
        elif choice ==3: issue_books()
        elif choice ==4: return_books()
        elif choice ==5:
            print("Thank You")
            break
        else: print("Invalid Input!!!")
        
library()