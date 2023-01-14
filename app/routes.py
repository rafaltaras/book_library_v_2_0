from app import app
from library_manager import library
from flask import request
from flask import jsonify, json 
from serializers import book_to_dict, author_to_dict, shelf_to_dict

@app.route("/api/v1/get/books", methods=["GET"])
def get_books():
    books = library.get_books()
    return [book_to_dict(book) for book in books]

@app.route("/api/v1/get/authors", methods=["GET"])
def get_authors():
    authors = library.get_authors()
    return [author_to_dict(author) for author in authors]

@app.route("/api/v1/get/shelf", methods=["GET"])
def get_shelf():
    shelf = library.get_shelf()
    return [shelf_to_dict(borrow) for borrow in shelf]

@app.route("/api/v1/add_book/", methods=["POST"])
def add_book():
    data = request.json
    library.add_book(title=data.get("title"))
    return get_books()

@app.route("/api/v1/add_author/", methods=["POST"])
def add_author():
    data = request.json
    library.add_author(first_name=data.get("first_name"), second_name=data.get("second_name"), birth_date=data.get("birth_date"))
    return get_authors()

@app.route("/api/v1/shelf/", methods=["POST"])
def on_shelf():
    data = request.json
    library.is_borrowed(is_borrowed=data.get("is_borrowed"), book_id=data.get("book_id"))
    return get_shelf()

@app.route("/api/v1/delete/<int:id>", methods=["DELETE"])
def delete(id):
    library.delete(id)
    return "Book deleted"