def render_book_list(books):
    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "edition": book.edition,
            "availability": book.availability,
        }
        for book in books
    ]


def render_book_detail(book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "edition": book.edition,
        "availability": book.availability,
    }