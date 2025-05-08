from repositories.book_loan_repository import BookLoanRepository

class BookLoanService:
    """
    Serviço responsável pela lógica de negócios relacionada aos empréstimos de livros.
    """

    def __init__(self, db_session):
        """
        Inicializa o serviço de empréstimos de livros.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.book_loan_repository = BookLoanRepository(db_session)

    def list_book_loans(self):
        """Retorna todos os empréstimos de livros."""
        return self.book_loan_repository.get_all_book_loans()

    def get_book_loan(self, book_loan_id):
        """Retorna um empréstimo de livro específico pelo seu ID."""
        return self.book_loan_repository.get_book_loan_by_id(book_loan_id)

    def add_book_loan(self, book_loan):
        """Adiciona um novo empréstimo de livro."""
        self.book_loan_repository.add_book_loan(book_loan)

    def update_book_loan(self, book_loan):
        """Atualiza um empréstimo de livro existente."""
        self.book_loan_repository.update_book_loan(book_loan)

    def delete_book_loan(self, book_loan_id):
        """Deleta um empréstimo de livro pelo seu ID."""
        self.book_loan_repository.delete_book_loan(book_loan_id)
