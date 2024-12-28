class Book:
    def __init__(self, title, author, genre, book_id, publisher, year, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.publisher = publisher
        self.year = year
        self.copies = copies
        self.available_copies = copies

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\nID: {self.book_id}\nPublisher: {self.publisher}\nYear: {self.year}\nCopies Available: {self.available_copies}"

    def check_availability(self):
        return self.available_copies > 0

    def issue_book(self):
        if self.check_availability():
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies += 1
            return True
        else:
            return False

