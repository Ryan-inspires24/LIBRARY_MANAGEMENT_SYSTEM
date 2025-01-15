from tkinter import *
from tkinter import messagebox

class Login:

    def __init__(self, window):
        self.window = window
        self.window.title('Library Management System')
        self.window.minsize(700, 700)
        self.librarianCode = "0000"
        self.login_status = False
        self.register()
        self.center_window()
        
    def center_window(self):
        
        screen_width = self.window.winfo_screenwidth() 
        screen_height = self.window.winfo_screenheight()

        window_width = 700 
        window_height = 700
        position_x = int((screen_width - window_width) / 2) 
        position_y = int((screen_height - window_height) / 2) 
        
        self.window.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')
        
    def register(self):
        self.canvas = Canvas(self.window)
        self.scrollbar = Scrollbar(self.window, orient=VERTICAL, command=self.canvas.yview)
        self.scrollableframe = Frame(self.canvas)

        self.scrollableframe.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollableframe, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        pageTitle = Label(self.scrollableframe, text='Library Management System - Login', font=('Arial', 18, 'bold'))
        pageTitle.pack(side=TOP)

        self.img = PhotoImage(file="myLibrary.png")
        label = Label(self.scrollableframe, image=self.img)
        label.pack()

        frame2 = Frame(self.scrollableframe)
        label2 = Label(frame2, text='Please Enter the Librarian Code: ', font=20)
        self.entry2 = Entry(frame2, bd=4, bg='orange')

        label2.pack(side=LEFT)
        self.entry2.pack(side=LEFT)
        frame2.pack(pady=10, padx=40)

        submitBtn = Button(self.scrollableframe, text="Submit", command=self.check_credentials)
        submitBtn.pack(pady=20)

    def check_credentials(self):
        if self.librarianCode == self.entry2.get():
            messagebox.showinfo('Welcome', f'Welcome Back!')
            self.login_status = True
        else:
            messagebox.showerror('Error', 'Wrong code!')
            self.login_status = False

        self.window.destroy()
