from app import app
from library_manager import library
from flask import request
from flask import jsonify, json 
from serializers import book_to_dict, author_to_dict, is_borrowed_to_dict

@app.route("/api/v1/get/books", methods=["GET"])
def get_books():
    books = library.get_library()
    return [book_to_dict(book) for book in books]

@app.route("/api/v1/get/authors", methods=["GET"])
def get_authors():
    authors = library.get_authors()
    return [author_to_dict(author) for author in authors]

@app.route("/api/v1/get/is_borrowed", methods=["GET"])
def borrowed():
    borrowed = library.borrowed()
    return [is_borrowed_to_dict(borrow) for borrow in borrowed]

@app.route("/api/v1/add_book/", methods=["POST"])
def add_book():
    data = request.json
    book = {
            "title" : data.get("title")
    }   
    title = book.get("title")  
    library.add_book(title)
    return get_books()

@app.route("/api/v1/add_author/", methods=["POST"])
def add_author():
    data = request.json
    author = {
        "first_name" : data.get("first_name"),
        "second_name" : data.get("second_name"),
        "birth_date" : data.get("birth_date")
    }
    first_name = author.get("first_name")
    second_name = author.get("second_name")
    birth_date = author.get("birth_date")
    library.add_author(first_name, second_name, birth_date)
    return get_authors()

@app.route("/api/v1/shelf/", methods=["POST"])
def is_borrowed():
    data = request.json
    isborrowed = {
        "is_borrowed" : data.get("is_borrowed"),
        "book_id" : data.get("book_id")
    }
    is_borrowed = isborrowed.get("is_borrowed")
    book_id = isborrowed.get("book_id")
    library.is_borrowed(is_borrowed,book_id)
    return borrowed()

@app.route("/api/v1/delete/<int:id>", methods=["DELETE"])
def delete(id):
    library.delete(id)
    return "Book deleted"