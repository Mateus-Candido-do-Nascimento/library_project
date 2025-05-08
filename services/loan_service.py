from repositories.loan_repository import LoanRepository

class LoanService:
    """
    Serviço responsável pela lógica de negócios relacionada aos empréstimos.
    """

    def __init__(self, db_session):
        """
        Inicializa o serviço de empréstimos.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.loan_repository = LoanRepository(db_session)

    def list_loans(self):
        """Retorna todos os empréstimos."""
        return self.loan_repository.get_all_loans()

    def get_loan(self, loan_id):
        """Retorna um empréstimo específico pelo seu ID."""
        return self.loan_repository.get_loan_by_id(loan_id)

    def add_loan(self, loan):
        """Adiciona um novo empréstimo."""
        self.loan_repository.add_loan(loan)

    def update_loan(self, loan):
        """Atualiza um empréstimo existente."""
        self.loan_repository.update_loan(loan)

    def delete_loan(self, loan_id):
        """Deleta um empréstimo pelo seu ID."""
        self.loan_repository.delete_loan(loan_id)
