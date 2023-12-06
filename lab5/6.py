class LibraryItem:
    def __init__(self, title, author_or_director, item_id, checked_out=False):
        self.title = title
        self.author_or_director = author_or_director
        self.item_id = item_id
        self.checked_out = checked_out

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already in the library.")

    def display_info(self):
        return f"ID: {self.item_id}, Title: {self.title}, Author/Director: {self.author_or_director}, Checked Out: {self.checked_out}"


class Book(LibraryItem):
    def __init__(self, title, author, item_id, checked_out=False, genre=''):
        super().__init__(title, author, item_id, checked_out)
        self.genre = genre

    def display_info(self):
        return f"Book - {super().display_info()}, Genre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, checked_out=False, duration=0):
        super().__init__(title, director, item_id, checked_out)
        self.duration = duration

    def display_info(self):
        return f"DVD - {super().display_info()}, Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, checked_out=False, issue_number=0):
        super().__init__(title, publisher, item_id, checked_out)
        self.issue_number = issue_number

    def display_info(self):
        return f"Magazine - {super().display_info()}, Issue Number: {self.issue_number}"


book_item = Book("The Great Gatsby", "F. Scott Fitzgerald", "B001", genre="Fiction")
dvd_item = DVD("Inception", "Christopher Nolan", "D001", duration=148)
magazine_item = Magazine("National Geographic", "National Geographic Society", "M001", issue_number=256)

print(book_item.display_info())
print(dvd_item.display_info())
print(magazine_item.display_info())

book_item.check_out()
dvd_item.check_out()
magazine_item.check_out()

book_item.check_out()

book_item.return_item()
dvd_item.return_item()

print(book_item.display_info())
print(dvd_item.display_info())
print(magazine_item.display_info())
