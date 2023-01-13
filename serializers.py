

def book_to_dict(book):
    return {
        "id": book.id,
        "title": book.title
    }

def author_to_dict(author):
    return {
        "id": author.id,
        "first_name": author.first_name,
        "second_name": author.second_name,
        "birth_date": author.birth_date
    }

def is_borrowed_to_dict(borrowed):
    return {
        "id": borrowed.id,
        "is_borrowed": borrowed.is_borrowed,
        "book_id": borrowed.book_id
    }