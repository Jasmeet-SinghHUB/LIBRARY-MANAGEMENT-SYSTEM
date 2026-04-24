from utils import books  #we did package 
    
def add_books():
    book_name = input("Enter the book name to be added: ")
    books.append(book_name)
    print(f"Book - {book_name} added successfully.")