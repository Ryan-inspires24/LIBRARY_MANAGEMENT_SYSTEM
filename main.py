from Classes.librarian import Librarian
import json

with open("cathalogue/books.json", "r") as libraryFile:
    libraryInfo = libraryFile.read()
    books = json.loads(libraryInfo)
    print("Loaded books:", books)
    

with open("membersFile/members.json", "r") as file:
    memberData = json.load(file)

print(memberData)


library = Librarian(books,memberData)
