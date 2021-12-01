# Library Management System

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print("We've the following books in our Library:")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book-Lender DataBase has been updated. You can take the book now!")
        
        else:
            print(f"Sorry! You can't get the book now as the book had already been lent to {self.lendDict[book]}.")

    def addBook(self, book):
        self.booksList.append(book)
        print("The book had been added successfully!")

    def returnBook(self, book):
        self.lendDict.pop(book)



if __name__ == '__main__':
    library = Library(["Middlemarch ", "To the Lighthouse", "Mrs. Dalloway", "Great Expectations", "Jane Eyre", "Bleak House", "Wuthering Heights", "David Copperfield", "Frankenstein", "Vanity Fair"], "Library of Knowledge")


    while True:
        print(f"Welcome to the {library.name}! Enter your choice in numerical value to continue.")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()

        if user_choice == "1":
            library.displayBook()

        elif user_choice == "2":
            book = input("Enter the name of the book you want to lend: \n")
            user = input("Enter your name: \n")
            library.lendBook(user, book)

        elif user_choice == "3":
            book = input("Enter the name of the book you want to add: \n")
            library.addBook(book)

        elif user_choice == "4":
            book = input("Enter the name of the book you want to return: \n")
            library.returnBook(book)

        else:
            print("Please enter a valid option!")
            continue


        print("Enter 'c' to continue or 'q' to quit:")
        user_choice2 = input()

        if user_choice2 == "c":
            continue
        elif user_choice2 == "q":
            print("Thank you for visiting our Library!")
            exit()
