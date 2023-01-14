from app import app, db
from app.models import Author, Book, Shelf
from flask import  json 

class Library:
    def get_library(self):
        get_books = Book.query.all() 
        return get_books

    def get_authors(self):
        get_authors = Author.query.all() 
        return get_authors

    def borrowed(self):
        is_borrowed = Shelf.query.all() 
        return is_borrowed

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