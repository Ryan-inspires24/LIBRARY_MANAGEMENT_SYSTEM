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

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nID: {self.book_id}\nPublisher: {self.publisher}\nYear: {self.year}\nCopies Available: {self.available_copies}"

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

