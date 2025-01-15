from Classes.book import Book
from datetime import datetime, timedelta
from tkinter import *

class Member:
    def __init__(self, memberId, memberName, memberClass):
        self.memberClass = memberClass
        self.memberId = memberId
        self.memberName = memberName
        self.bookFine = 0
        self.borrowedBooks = {} 
        self.borrowLimit = 3 
        
    def borrowBook(self, book):
        if Book.checkAvailability():
            if len(self.borrowedBooks) < self.borrowLimit:
                dueDate = datetime.now() + timedelta(days=7)
                #if the number of books the user has borrowed is lessthan the borrowing limit, set the duedate to 7 days after and add to the list.
                self.borrowedBooks[book.bookId] = {
                    'book': book,
                    'dueDate': dueDate
                    }
            print(f"{self.memberName} borrowed {book.title}. It is due back on {dueDate.strftime('%Y-%m-%d')}.")
        else:
            print(f"{self.memberName} has reached the borrow limit of {self.borrowLimit} books.")

    def returnBook(self, bookId):
        if bookId in self.borrowedBooks:
            bookDetails = self.borrowedBooks.pop(bookId)
            returnDate = datetime.now()
            if returnDate > bookDetails['dueDate']:
                overdueDays = (returnDate - bookDetails['dueDate']).days
                self.bookFine += 1 * overdueDays  # Assuming fine is 1 unit per day
                print(f"{self.memberName} returned {bookDetails['book'].title} late. Fine accumulated: {self.bookFine} units.")
            else:
                print(f"{self.memberName} returned {bookDetails['book'].title} on time.")
        else:
            print(f"No record of {self.memberName} borrowing a book with ID {bookId}.")

    def payfine(self, amount):
        if amount <= self.bookFine:
            self.bookFine -= amount
            print(f"{self.memberName} paid {amount} units. Remaining fine: {self.bookFine} units.")
        else:
            print(f"Amount exceeds the owed fine. {self.memberName} currently owes {self.bookFine} units.")

# # Example usage
# book1 = Book(bookId='101', title='Python Programming', author='John Doe', genre='Technology', publisher='TechBooks', year='2023', copies=5, availableCopies=5)
# member1 = Member(memberId='M001', memberName='Alice', memberClass='A')

# member1.borrowBook(book1)
# # Simulate returning book late
# from time import sleep
# sleep(1)  # Just for simulation, you can remove this in real implementation
# member1.returnBook('101')
# member1.payfine(2)
