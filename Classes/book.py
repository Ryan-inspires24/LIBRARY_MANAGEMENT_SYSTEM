from tkinter import *
class Book:
    def __init__(self, title, author, genre, bookId, publisher, year, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.bookId = bookId
        self.publisher = publisher
        self.year = year
        self.copies = copies
        self.availableCopies = copies

    def addBook(self):
        self.bookWindow = Toplevel(self.root)
        self.bookWindow.title("Add New Book") 
        
        Label(self.bookWindow, text="Book ID:").pack(pady=5) 
        self.bookIdEntry = Entry(self.bookWindow)
        self.bookIdEntry.pack(pady=5)
        
        Label(self.bookWindow, text="Title:").pack(pady=5) 
        self.bookTitleEntry = Entry(self.bookWindow)
        self.bookTitleEntry.pack(pady=5)
        
        Label(self.bookWindow, text="Author:").pack(pady=5)
        self.bookAuthorEntry = Entry(self.bookWindow)
        self.bookAuthorEntry.pack(pady=5) 
        
        Label(self.bookWindow, text="Genre:").pack(pady=5) 
        self.bookGenreEntry = Entry(self.bookWindow) 
        self.bookGenreEntry.pack(pady=5)
        
        Label(self.bookWindow, text="Year:").pack(pady=5)
        self.bookYearEntry = Entry(self.bookWindow) 
        self.bookYearEntry.pack(pady=5) 
        
        Label(self.bookWindow, text="Copies:").pack(pady=5) 
        self.bookCopiesEntry = Entry(self.bookWindow)
        self.bookCopiesEntry.pack(pady=5) 
        
        
       
    def checkAvailability(self):
        return self.availableCopies > 0

    def issue_book(self):
        if self.checkAvailability():
            self.availableCopies -= 1
            return True
        else:
            return False

    def returnBook(self):
        if self.availableCopies < self.copies:
            self.availableCopies += 1
            return True
        else:
            return False
        
    def totalNumberOfBooks():
        pass
        

