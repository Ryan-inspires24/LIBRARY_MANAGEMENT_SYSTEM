from tkinter import *
from tkinter import ttk
from Classes.member import Member
from tkinter import messagebox

class LibraryGui:
    def __init__(self, root, library, members):
        self.root = root
        self.library = library
        self.members = members
        self.centerWindow()

        self.root.title("Library Management System")
        
        self.dashboard = Frame(root)
        self.dashboard.pack(fill=BOTH, expand=5)
        
        self.title = Label(self.dashboard, text='Choose your view', border=20, font=15)
        self.title.pack(side=TOP)
        
        handleBooksBtn = Button(self.dashboard, text="Handle Books", command=self.handleBooks)
        handleMembersBtn = Button(self.dashboard, text="Handle Members", command=self.handleMembers)

        handleBooksBtn.pack(padx=20, pady=20)
        handleMembersBtn.pack(padx=20, pady=20)
        
    def centerWindow(self):
        
            screenWidth = self.root.winfo_screenwidth() 
            screenHeight = self.root.winfo_screenheight()

            windowWidth = 400 
            windowHeight = 400
            positionx = int((screenWidth - windowWidth) / 2) 
            positiony = int((screenHeight - windowHeight) / 2) 
        
            self.root.geometry(f'{windowWidth}x{windowHeight}+{positionx}+{positiony}')
        

    def handleBooks(self):
        
        self.clearFrame()
        self.root.minsize=(1000,700)
        self.bookFrame = Frame(self.root)
        self.bookFrame.pack(fill=BOTH, expand=5)

        self.bookTree = ttk.Treeview(self.bookFrame, columns=("bookId", "title", "author", "genre", "year", "copies"), show='headings')
        self.bookTree.heading("bookId", text="Book ID")
        self.bookTree.heading("title", text="Title")
        self.bookTree.heading("author", text="Author")
        self.bookTree.heading("genre", text="Genre")
        self.bookTree.heading("year", text="Year")
        self.bookTree.heading("copies", text="Copies")
        self.bookTree.pack(fill=BOTH, expand=5)

        for bookId, bookInfo in self.library.items():
            self.bookTree.insert("", END, values=(bookId, bookInfo['Title'], bookInfo['Author'], bookInfo['Genre'], bookInfo['Year'], bookInfo['availableCopies']))

        addBookBtn = Button(self.bookFrame, text="Add Book", command=self.addBook)
        addBookBtn.pack(side=LEFT, padx=10, pady=10)
        handleMembersBtn = Button(self.bookFrame, text='Go to Handle Members', command=self.handleMembers)
        handleMembersBtn.pack(side=LEFT, padx=10, pady=10)

    def handleMembers(self):
        self.clearFrame()
        self.memberFrame = Frame(self.root)
        self.memberFrame.pack(fill=BOTH, expand=1)

        self.memberTree = ttk.Treeview(self.memberFrame, columns=("id", "name", "dateOfEntry", "class", "fine"), show='headings')
        self.memberTree.heading("id", text="ID")
        self.memberTree.heading("name", text="Name")
        self.memberTree.heading("dateOfEntry", text="Date of Entry")
        self.memberTree.heading("class", text="Class")
        self.memberTree.heading("fine", text="Fine")
        self.memberTree.pack(fill=BOTH, expand=1)

        for memberId, memberInfo in self.members.items():
            self.memberTree.insert("", END, values=(memberId, memberInfo['memberName'], memberInfo['dateOfEntry'], memberInfo['memberClass'], memberInfo['fine']))

        self.memberTree.bind('<Double-1>', self.onMemberSelect)

        addMemberBtn = Button(self.memberFrame, text="Add Member", command=self.addMember)
        addMemberBtn.pack(side=LEFT, padx=10, pady=10)
        handlebooksBtn = Button(self.memberFrame, text='Go to Books Page', command=self.handleBooks)
        handlebooksBtn.pack(side=RIGHT, padx=10, pady=10)
        
    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def onMemberSelect(self, event):
        item = self.memberTree.selection()[0]
        memberId = self.memberTree.item(item, "values")[0]
        self.manageMember(memberId)

    def addMember(self):
        self.memberWindow = Toplevel(self.root)
        self.memberWindow.title("Add New Member")

        Label(self.memberWindow, text="Member ID:").pack(pady=5)
        self.memberIdEntry = Entry(self.memberWindow)
        self.memberIdEntry.pack(pady=5)

        Label(self.memberWindow, text="Member Name:").pack(pady=5)
        self.memberNameEntry = Entry(self.memberWindow)
        self.memberNameEntry.pack(pady=5)

        Label(self.memberWindow, text="Date of Entry:").pack(pady=5)
        self.dateOfEntryEntry = Entry(self.memberWindow)
        self.dateOfEntryEntry.pack(pady=5)

        Label(self.memberWindow, text="Class:").pack(pady=5)
        self.memberClassEntry = Entry(self.memberWindow)
        self.memberClassEntry.pack(pady=5)

        Label(self.memberWindow, text="Fine:").pack(pady=5)
        self.memberFineEntry = Entry(self.memberWindow)
        self.memberFineEntry.pack(pady=5)

        saveMemberBtn = Button(self.memberWindow, text="Save Member", command=self.saveMember)
        saveMemberBtn.pack(pady=10)

    def saveMember(self):
        newMember = {
            'memberName': self.memberNameEntry.get(),
            'dateOfEntry': self.dateOfEntryEntry.get(),
            'memberClass': self.memberClassEntry.get(),
            'fine': self.memberFineEntry.get()
        }
        self.members[self.memberIdEntry.get()] = newMember
        self.memberTree.insert("", END, values=(self.memberIdEntry.get(), newMember['memberName'], newMember['dateOfEntry'], newMember['memberClass'], newMember['fine']))
        self.memberWindow.destroy()

    def manageMember(self, memberId):
        memberInfo = self.members[memberId]
        self.memberWindow = Toplevel(self.root)
        self.memberWindow.title("Manage Member")

        Label(self.memberWindow, text=f"Member ID: {memberId}").pack(pady=5)
        Label(self.memberWindow, text=f"Name: {memberInfo['memberName']}").pack(pady=5)
        Label(self.memberWindow, text=f"Date of Entry: {memberInfo['dateOfEntry']}").pack(pady=5)
        Label(self.memberWindow, text=f"Class: {memberInfo['memberClass']}").pack(pady=5)
        Label(self.memberWindow, text=f"Fine: {memberInfo['fine']}").pack(pady=5)

        borrowBookBtn = Button(self.memberWindow, text="Borrow Book", command=lambda: self.borrowBook(memberId))
        returnBookBtn = Button(self.memberWindow, text="Return Book", command=lambda: self.returnBook(memberId))
        payFineBtn = Button(self.memberWindow, text="Pay Fine", command=lambda: self.payFine(memberId))

        borrowBookBtn.pack(pady=20, padx=20)
        returnBookBtn.pack(pady=20, padx=20)
        payFineBtn.pack(pady=20, padx=20)

    def borrowBook(self, memberId):
        self.bookWindow = Toplevel(self.root)
        self.bookWindow.title("Borrow Book")
    
        Label(self.bookWindow, text="Select Book ID:").pack(pady=5,padx=5) 
        self.bookIdEntry = Entry(self.bookWindow) 
        self.bookIdEntry.pack(pady=5, padx=5)
    
        borrowBtn = Button(self.bookWindow, text="Borrow", command=lambda: self.confirmBorrow(memberId))
        borrowBtn.pack(pady=20, padx=20) 
    
    def confirmBorrow(self, memberId):
        bookId = self.bookIdEntry.get()
        if bookId in self.library: 
            bookInfo = self.library[bookId]
            if int(bookInfo['availableCopies']) > 0:
                bookInfo['availableCopies'] = str(int(bookInfo['availableCopies']) - 1)
                self.library[bookId] = bookInfo
                # Member.borrowBook(memberId, bookId)
                
                
            else:
                print("Book ID not found")
                messagebox.showerror('Sorry,', 'There are no more available copies of this book.') 
                
        else:
            messagebox.showerror('Error!', 'This book ID does not exist in this Library.') 
               
        self.bookWindow.destroy() 
                
    def returnBook(self, memberId):
        self.returnWindow = Toplevel(self.root)
        self.returnWindow.title("Return Book") 
        
        Label(self.returnWindow, text="Select Book ID:").pack(pady=5, padx=5) 
        
        self.returnBookIdEntry = Entry(self.returnWindow) 
        self.returnBookIdEntry.pack(pady=5, padx=5)
        
        returnBtn = Button(self.returnWindow, text="Return", command=lambda: self.confirmReturn(memberId)) 
        returnBtn.pack(pady=10) 
        
    def confirmReturn(self, memberId):
        bookId = self.returnBookIdEntry.get() 
        if bookId in self.library: 
            bookInfo = self.library[bookId] 
            bookInfo['availableCopies'] = str(int(bookInfo['availableCopies']) + 1) 
            self.library[bookId] = bookInfo 
            # Member.returnBook(memberId, bookId) 
     
            self.updateBookTree() 
            self.updateMemberTree() 
        else: print("Book ID not found")
        self.returnWindow.destroy() 
   

    def payFine(self, memberId):
        Member.payfine(memberId)

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
        self.bookCopiesEntry.pack(pady=5)

        saveBookBtn = Button(self.bookWindow, text="Save Book", command=self.saveBook)
        saveBookBtn.pack(pady=10)

    def saveBook(self):
        newBook = {
            'Title': self.bookTitleEntry.get(),
            'Author': self.bookAuthorEntry.get(),
            'Genre': self.bookGenreEntry.get(),
            'Year': self.bookYearEntry.get(),
            'availableCopies': self.bookCopiesEntry.get()
        }
        self.library[self.bookIdEntry.get()] = newBook
        self.bookTree.insert("", END, values=(self.bookIdEntry.get(), newBook['Title'], newBook['Author'], newBook['Genre'], newBook['Year'], newBook['availableCopies']))
        self.bookWindow.destroy()
