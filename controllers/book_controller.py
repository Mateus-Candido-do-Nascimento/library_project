from flask import Blueprint, render_template, request
from services.book_service import BookService
from database import db_session, SessionLocal


book_bp = Blueprint('book', __name__)

@book_bp.route('/')
def list_books():
    try:
        # Cria uma nova sessão para o serviço
        db_session = SessionLocal()
        book_service = BookService(db_session)
        
        # Chama o serviço para listar os livros
        books = book_service.list_books()

        # Fecha a sessão
        db_session.close()

        return render_template('books.html', books=books)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
