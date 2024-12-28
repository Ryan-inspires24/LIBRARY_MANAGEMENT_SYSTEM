from Classes.librarian import Librarian
import json

with open("cathalogue/books.json", "r") as libraryFile:
    libraryInfo = libraryFile.read()
    books = json.loads(libraryInfo)
    print("Loaded books:", books)

library = Librarian(books)

