from app import db

class Book:    
    def __init__(self,title):
        self.title = title

    def add_book(self):
        u = Book(title=self.title)
        db.session.add(u)
        db.session.commit()


book = Book()

