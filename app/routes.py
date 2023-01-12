from app import db
from app.models import Author, Book, Shelf

class Book:    
    def add_book(self):
        book = Book(title="BookTest")
        db.session.add(book)
        db.session.commit(book)


book = Book()
