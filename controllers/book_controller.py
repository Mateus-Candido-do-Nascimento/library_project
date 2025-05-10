from flask import Blueprint, render_template
from models.book import Book
from config.database import db

book_bp = Blueprint('book', __name__)

@book_bp.route('/')
def list_books():
    try:
        # Consulta todos os livros
        books = Book.query.all()
        return render_template('books.html', books=books)
    except Exception as e:
        db.session.rollback()  # Boa prática em caso de erro
        return render_template('error.html', message=str(e)), 500
