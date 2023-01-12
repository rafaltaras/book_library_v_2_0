from app import app
from library_manager import library
from flask import request

@app.route("/api/v1/get/books", methods=["GET"])
def get():
    library.get_library()
    return "Should be json"

@app.route("/api/v1/book/", methods=["POST"])
def add_book():
    data = request.json
    book = {
            "title" : data.get("title")
    }   
    title = book.get("title")  
    library.add_book(title)
    return "Book added"


@app.route("/api/v1/author/", methods=["POST"])
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
    return "Author added to DB"

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
    return "Is borrowed ?"