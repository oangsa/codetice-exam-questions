class Book:
    def __init__(self, title):
        self.title = title
        self.is_available = True
    
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
        
    def return_book(self):
        self.is_available = True

def main():
    title = input().strip()
    book = Book(title)
    
    n = int(input().strip())
    for _ in range(n):
        cmd = input().strip()
        if cmd == "borrow":
            if book.borrow_book():
                print(f"Borrowed {book.title}")
            else:
                print(f"{book.title} is not available")
        elif cmd == "return":
            book.return_book()
            print(f"Returned {book.title}")

if __name__ == '__main__':
    main()
