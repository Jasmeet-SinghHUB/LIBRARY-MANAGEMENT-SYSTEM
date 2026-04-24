from utils import books,issued_books
def issue_books():
    if len(books) == 0: print("no book found so u cant issue books")
    else:
        book_name = input("enter the book name to be issued: ").strip().upper()
        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f"Book - {book_name} issued successfully. ")
        else:
            print("No such book available!!!")    

