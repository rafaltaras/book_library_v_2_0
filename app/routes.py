from app import db

class Book:
    
    def add_book(self,title):
        u = Book(title=title)
        db.session.add(u)
        db.session.commit()


book = Book()