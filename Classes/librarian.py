from Classes.login import Login
from Classes.book import Book
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
class Librarian:

    def __init__(self, library):
        self.library = library
        self.loginWindow = Tk()
        self.login = Login(self.loginWindow)
        self.loginWindow.mainloop()

        if self.login.login_status:
            self.access_library()
        else:
            print("Access Denied. Invalid Login Credentials.")
            

    def access_library(self):
        self.libwindow = Tk()
        self.libwindow.title('Library information')
        
        self.books = []
        for bookId,bookInfo in self.library.items():
            book = Book(
                title=bookInfo['Title'],
                author=bookInfo['Author'],
                genre=bookInfo["Genre"],
                bookId=bookInfo['id'],
                publisher=bookInfo['publisher'],
                year=bookInfo['Year'],
                copies = bookInfo['availableCopies']
                
            )
            self.books.append(book)
            
        tree = ttk.Treeview(self.libwindow) 
            
            # Define the columns 
        tree["columns"] = ("Book ID", "Title", "Author", "Copies", "Available Copies") 
           
            # Format columns 
        tree.column("#0", width=0, stretch=NO)
        tree.column("Book ID", anchor=CENTER, width=80)
        tree.column("Title", anchor=W, width=200) 
        tree.column("Author", anchor=W, width=200)
        tree.column("Copies", anchor=CENTER, width=80) 
        tree.column("Available Copies", anchor=CENTER, width=120)
            
            # Create column headings 
        tree.heading("#0", text="", anchor=W) 
        tree.heading("Book ID", text="Book ID", anchor=CENTER) 
        tree.heading("Title", text="Title", anchor=W) 
        tree.heading("Author", text="Author", anchor=W) 
        tree.heading("Copies", text="Copies", anchor=CENTER) 
        tree.heading("Available Copies", text="Available Copies", anchor=CENTER)
            
            # Load the data and insert it into the tree 
        for book in self.books: 
            tree.insert(parent="", index="end", iid=book.bookId, text="", values=(book.bookId, book.title, book.author, book.copies, book.availableCopies))
                
                # Pack the Treeview
            tree.pack(pady=20, padx=20)
                
                # Run the main loop for the new window 
        self.libwindow.mainloop()
        availableBooksBtn = Button(self.libwindow, text='View Available Books', command=book.)
        borrowedBooksBtn = Button(self.libwindow, text='View Borrowed Books', command='')
        libraryMembersBtn = Button(self.libwindow, text='View Members of the Library', command='')

        availableBooksBtn.pack(padx=30, pady=50)
        borrowedBooksBtn.pack(padx=30, pady=50)
        libraryMembersBtn.pack(padx=30, pady=50)

        
        
        
        
        



