# mikroblog.py

from app import app, db
from app.models import Author, Book, Shelf
# from app.routes import book

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Author": Author,
       "Book_status": Shelf

   }

def add_book():
    b = Book(title="Book1")
    db.session.add(b)
    db.session.commit()
    return

add_book()
