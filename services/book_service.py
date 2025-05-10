from repositories.book_repository import BookRepository

class BookService:
    """
    Serviço responsável pela lógica de negócios relacionada aos livros.
    """

    def __init__(self):
        """Inicializa o serviço de livros com a instância padrão do repositório."""
        self.book_repository = BookRepository()

    def list_books(self):
        return self.book_repository.get_all_books()

    def get_book(self, book_id):
        return self.book_repository.get_book_by_id(book_id)

    def add_book(self, book):
        self.book_repository.add_book(book)

    def update_book(self, book):
        self.book_repository.update_book(book)

    def delete_book(self, book_id):
        self.book_repository.delete_book(book_id)
