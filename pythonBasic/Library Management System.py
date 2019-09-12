import sys
class Library:
    def __init__(self, books):
        self.books = books

    def displayBook(self):
        for book in self.books:
            print(book)
        print()
    def lendBook(self, a):
        lend =input("Enter the name of book which you want to borrow\n")
        if lend in self.books:
            self.books.remove(lend)
            print(lend, "has been successfully borrowed by", Name,"\n")
        else:
            print("Book not found\n")
    def addBook(self):
        add = input("Enter the book name you want to add:\n")
        self.books.append(add)
    def returnBook(self):
        return1 = input("Enter the book name you want to add:\n")
        self.books.append(return1)
        print("Hello", Name, "you have successfully return your book\n")
if __name__ == '__main__':
    print("----------Welcome to my Library")
    Books = Library(["Python Programming", "C Programming", "Java Programming", "Data Structure & Algorithm"])
    Name = input("Enter your name sir:\n")
    print("Welcome",Name, "What do you want to like\n")
    CustomerList = []
    CustomerList.append(Name)
    a = False
    while (a ==False):
        print("1.Display available books\n 2.lend a book\n 3.Add a book\n 4.Return a book\n 5.Exit")
        choose = int(input())

        if choose ==1:
            print("Available Books are:\n")
            Books.displayBook()
        elif choose==2:
            print("Available Books are:\n")
            Books.lendBook(Books.displayBook())
        elif choose==3:
            Books.addBook()
        elif choose==4:
            Books.returnBook()
        elif choose==5:
            print("Thank you for visiting")
            sys.exit()