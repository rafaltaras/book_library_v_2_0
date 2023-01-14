from app import app
from app.library_manager import library
from flask import request, jsonify, abort, make_response
from app.serializers import book_to_dict, author_to_dict, shelf_to_dict

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

@app.route("/api/v1/add/book/", methods=["POST"])
def add_book():
    data = request.json
    library.add_book(title=data.get("title"))
    return get_books()

@app.route("/api/v1/add/author/", methods=["POST"])
def add_author():
    data = request.json
    library.add_author(first_name=data.get("first_name"), second_name=data.get("second_name"), birth_date=data.get("birth_date"))
    return get_authors()

@app.route("/api/v1/shelf/", methods=["POST"])
def on_shelf():
    data = request.json
    library.is_borrowed(is_borrowed=data.get("is_borrowed"), book_id=data.get("book_id"))
    return get_shelf()


@app.route("/api/v1/update/title", methods=["PUT"])
def update_title():
    data = request.json
    library.update_title(id=data.get("id"), title=data.get("title"))
    return get_books()

@app.route("/api/v1/update/author", methods=["PUT"])
def update_author():
    data = request.json
    library.update_author(id=data.get("id"),first_name=data.get("first_name"), second_name=data.get("second_name"), birth_date=data.get("birth_date"))
    return get_authors()

@app.route("/api/v1/delete/book/<int:id>", methods=["DELETE"])
def delete_book(id):
    book_id = library.get_book_by_id(id)
    if not book_id:
        abort(404)
    else:
        library.delete_book(id)
    return get_books()

@app.route("/api/v1/delete/author/<int:id>", methods=["DELETE"])
def delete_author(id):
    author_id = library.get_author_by_id(id)
    if not author_id:
        abort(404)
    else:
        library.delete_author(id)
    return get_authors()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found this id', 'status_code': 404}), 404)