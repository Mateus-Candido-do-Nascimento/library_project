from flask import Blueprint, render_template, request
from services.book_service import BookService

book_bp = Blueprint('book', __name__)

@book_bp.route('/')
def list_books():
    try:
        book_service = BookService()
        books = book_service.list_books()
        return render_template('books.html', books=books)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
