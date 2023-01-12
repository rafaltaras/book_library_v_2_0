from app import app, db
from app.models import Author, Book, Shelf
import json

class Library:
    def get_library(self):
        get_books = Book.query.all()
        return get_books

    def add_book(self, title):
        book = Book(title=title)
        db.session.add(book)
        db.session.commit()
        return "ok"

    def add_author(self, first_name, second_name, birth_date):
        author = Author(first_name=first_name, second_name=second_name, birth_date=birth_date )
        db.session.add(author)
        db.session.commit()
        return "ok"

    def is_borrowed(self, is_borrowed, book_id):
        shelf = Shelf(is_borrowed=is_borrowed, book_id=book_id)
        db.session.add(shelf)
        db.session.commit()
        return "ok"

    def save_library(self):
        with open("library.json", "w") as f:
            json.dump(self.library, f)


library = Library()