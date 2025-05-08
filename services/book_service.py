from repositories.book_repository import BookRepository

class BookService:
    """
    Serviço responsável pela lógica de negócios relacionada aos livros.
    """

    def __init__(self, db_session):
        """
        Inicializa o serviço de livros.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.book_repository = BookRepository(db_session)

    def list_books(self):
        """Retorna todos os livros."""
        return self.book_repository.get_all_books()

    def get_book(self, book_id):
        """Retorna um livro específico pelo seu ID."""
        return self.book_repository.get_book_by_id(book_id)

    def add_book(self, book):
        """Adiciona um novo livro."""
        self.book_repository.add_book(book)

    def update_book(self, book):
        """Atualiza um livro existente."""
        self.book_repository.update_book(book)

    def delete_book(self, book_id):
        """Deleta um livro pelo seu ID."""
        self.book_repository.delete_book(book_id)
