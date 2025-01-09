from Classes.login import Login
from Classes.libraryGui import LibraryGui
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Librarian:
    def __init__(self, library, members):
        self.library = library
        self.members = members
        self.loginWindow = Tk()
        self.login = Login(self.loginWindow)
        self.loginWindow.mainloop()

        if self.login.login_status:
            self.accessLibrary()
        else:
            print("Access Denied. Invalid Login Credentials.")

    def accessLibrary(self):
        root = Tk()
        LibraryGui(root, self.library, self.members)
        root.mainloop()