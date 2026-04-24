from utils import books,issued_books
def return_books():
    if len(issued_books) == 0: print("no book issued earlier")
    else:
        book_name = input("enter the book name to be returned: ").strip().upper()
        if book_name in issued_books:
            issued_books.remove(book_name)
            books.append(book_name)
            print(f"Book - {book_name} returned successfully. ")
        else:
            print("fuck off!!!")    
