class Person:
    """To implement"""
    def __init__(self,first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class Book:
    """To implement"""
    def __init__(self,title:str,author:Person):
        self.title = title
        self.author = author
    def __str__(self) -> str:
        return f'"{self.title}" by {self.author}'

class LibraryError(Exception):
    """Base class for Library errors"""


class Library:
    """To implement."""
    def __init__(self, name:str):
        self.name = name
        self.books: list[Book] = []
        self.members:set[Person] = set()
        self.borrowed_books:dict[Book,Person] = {}
    
    def is_book_available(self, book:Book):
        if book not in self.books:
            raise LibraryError("Book not in catalog")
        return book not in self.borrowed_books

    def borrow_book(self, book:Book, person:Person):
        if person not in self.members:
            raise LibraryError(f"{person} is not a member")
        if book not in self.books:
            raise LibraryError(f" {book} not in catalog")
        if book in self.borrowed_books:
            raise LibraryError(f"{book} already borrowed ")
        self.borrowed_books[book] = person
        if book not in self.borrowed_books:
            raise LibraryError(f"{book} is not part of the borrowed books")

    
    def return_book(self, book:Book):
        if book not in self.borrowed_books:
            raise LibraryError("Book was not borrowed")
        self.borrowed_books.pop(book)

    def add_new_book(self,book:Book):
        self.books.append(book)
    
    def add_new_member(self,member:Person):
        self.members.add(member)

    def print_status(self):
        print(f"=== Library Status ===")
        print(f"Name: {self.name}")
        print(f"Books in catalog: {len(self.books)}")
        available = len(self.books) - len(self.borrowed_books)
        print(f"Available books: {available}")
        print(f"Number of members: {len(self.members)}")
        print("Borrowed books:")
        if self.borrowed_books:
            for book, person in self.borrowed_books.items():
                print(f"  - {book} borrowed by {person}")
        else:
            print("  No books currently borrowed")
        

    



def main():
    """Test your code here"""
    """antoine = Person("Antoine","Dupont")
    print(f"First name: {antoine.first_name}")
    print(f"Last name: {antoine.last_name}")
    print(antoine)

    novel_book = Book("Vingt mille lieus sous les mers", Person("Antoine","Dupont"))
    print(f"title: {novel_book.title}")
    print(f"author: {novel_book.author}")
    print(novel_book)"""
    
    antoine = Person("Antoine", "Dupont")
    print(antoine)

    julia = Person("Julia", "Roberts")
    print(julia)

    rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
    print(rugby_book)

    novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
    print(novel_book)

    library = Library("Public library")
    library.print_status()

    library.add_new_book(rugby_book)
    library.add_new_book(novel_book)
    library.add_new_member(antoine)
    library.add_new_member(julia)
    library.print_status()

    print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
    library.borrow_book(rugby_book, antoine)
    library.print_status()

    try:
        library.borrow_book(rugby_book, julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
    except LibraryError as error:
        print(error)

    try:
        library.borrow_book(novel_book, Person("Simone", "Veil"))
    except LibraryError as error:
        print(error)

    try:
        library.return_book(novel_book)
    except LibraryError as error:
        print(error)

    library.return_book(rugby_book)
    library.borrow_book(novel_book, julia)
    library.print_status()

    library.borrow_book(rugby_book, julia)
    library.print_status()


if __name__ == "__main__":
    main()
