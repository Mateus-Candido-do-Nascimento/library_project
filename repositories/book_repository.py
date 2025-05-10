from models.book import Book
from config.database import db

class BookRepository:

    def get_all_books(self):
        return Book.query.all()

    def get_book_by_id(self, book_id):
        return Book.query.get(book_id)

    def add_book(self, book):
        db.session.add(book)
        db.session.commit()

    def update_book(self, book):
        db.session.merge(book)
        db.session.commit()

    def delete_book(self, book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
