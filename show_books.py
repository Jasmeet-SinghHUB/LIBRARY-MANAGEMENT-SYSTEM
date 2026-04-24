from utils import books
def show_books():
    if len(books) ==0: print("No books found")
    else:
        for _ in books:
            print(_)
            
