# app/models.py
from datetime import datetime
from app import db

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), index=True, unique=True)
   authors = db.relationship("Author", backref="author", lazy="dynamic")

   def __str__(self):
       return f"<Book {self.title}>"

class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.Text)
   second_name = db.Column(db.Text)
   birth_date = db.Column(db.Text)
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

   def __str__(self):
       return f"<Author {self.id} {self.first_name[:50]} {self.second_name[:50]} ...>"

class Shelf(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   is_borrowed = db.Column(db.Boolean, unique=False, default=True)
   book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
   books = db.relationship("Book", backref="shelf")
   
   def __str__(self):
       return f"<Book_status {self.id} {self.is_borrowed[:50]}  {self.book_id[:50]}...>"