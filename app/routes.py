from app import app, db
from app.models import Author, Book, Shelf

@app.route("/")
def test():
    book = Book(title="Test")
    db.session.add(book)
    db.session.commit(book)
    return "ok"