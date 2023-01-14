from app import app, db
from app.models import Author, Book, Shelf

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
        return book

    def add_author(self, first_name, second_name, birth_date):
        author = Author(first_name=first_name, second_name=second_name, birth_date=birth_date )
        db.session.add(author)
        db.session.commit()
        return author

    def is_borrowed(self, is_borrowed, book_id):
        shelf = Shelf(is_borrowed=is_borrowed, book_id=book_id)
        db.session.add(shelf)
        db.session.commit()
        return shelf
    
    def update_title(self, id, title):
        update_title = Book.query.get(id)
        update_title.title = title
        db.session.add(update_title)
        db.session.commit()

    def update_author(self, id, first_name, second_name, birth_date):
        update = Author.query.get(id)
        update.first_name = first_name
        db.session.add(update)
        update.second_name = second_name
        db.session.add(update)
        update.birth_date = birth_date
        db.session.add(update)
        db.session.commit()

    def delete_book(self, id):
        get = Book.query.get(id)
        db.session.delete(get)
        db.session.commit()

    def delete_author(self, id):
        get = Author.query.get(id)
        db.session.delete(get)
        db.session.commit()

    def get_book_id(self, id):
        get_book_id = Book.query.get(id)
        return get_book_id
    
    def get_author_id(self, id):
        get_author_id = Author.query.get(id)
        return get_author_id

library = Library()