from Classes.login import Login
from Classes.book import Book
from tkinter import *

class Librarian:

    def __init__(self, library):
        self.library = library
        self.login_window = Tk()
        self.login = Login(self.login_window)
        self.login_window.mainloop()

        if self.login.login_status:
            self.access_library()
        else:
            print("Access Denied. Invalid Login Credentials.")

    def access_library(self):
        



