from app import app, db
from app.models import Author, Book, Shelf
from flask import  json 

class Library:
    def get_books(self):
        return Book.query.all()

    def get_authors(self):
        return Author.query.all() 

    def get_shelf(self):
        return Shelf.query.all() 

    def add_book(self, title):
        book = Book(title=title)
        db.session.add(book)
        db.session.commit()
        return "OK"

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
    
    def delete(self, id):
        get = Book.query.get(id)
        # book_id = id - 1
        # book_to_delete = get[id]
        print(get)
        db.session.delete(get)
        db.session.commit()

library = Library()