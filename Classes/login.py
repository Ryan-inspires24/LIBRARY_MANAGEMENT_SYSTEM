from tkinter import *
from tkinter import messagebox

class Login:

    def __init__(self, window):
        self.window = window
        self.window.title('Library Management System')
        self.librarianCode = "0000"
        self.login_status = False
        self.register()

    def register(self):
        frame1 = Frame(self.window) 
        label1 = Label(frame1, text='Enter Name: ')
        self.entry1 = Entry(frame1)

        frame2 = Frame(self.window) 
        label2 = Label(frame2, text='Enter the Librarian Code: ')
        self.entry2 = Entry(frame2)

        label1.pack(side=LEFT)
        self.entry1.pack(side=RIGHT)
        frame1.pack(pady=10, padx=40)

        label2.pack(side=LEFT)
        self.entry2.pack(side=RIGHT)
        frame2.pack(pady=10, padx=40)

        submitBtn = Button(self.window, text="Submit", command=self.check_credentials)
        submitBtn.pack(pady=20)

    def check_credentials(self):
        
        if self.librarianCode == self.entry2.get():
            messagebox.showinfo('Welcome', 'Welcome Back!')
            self.login_status = True
        else:
            messagebox.showerror('Error', 'Wrong code!')
            self.login_status = False
        
        # Close the login window after checking credentials
        self.window.destroy()
