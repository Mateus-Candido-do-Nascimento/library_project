from models.loan import Loan
class LoanRepository:
    """
    Repositório responsável pela interação com os dados de empréstimos no banco de dados.
    """

    def __init__(self, db_session):
        """
        Inicializa o repositório de empréstimos com a sessão do banco de dados.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.db_session = db_session

    def get_all_loans(self):
        """Retorna todos os empréstimos do banco de dados."""
        return self.db_session.query(Loan).all()

    def get_loan_by_id(self, loan_id):
        """Retorna um empréstimo específico pelo seu ID."""
        return self.db_session.query(Loan).filter_by(id=loan_id).first()

    def add_loan(self, loan):
        """Adiciona um novo empréstimo ao banco de dados."""
        self.db_session.add(loan)
        self.db_session.commit()

    def update_loan(self, loan):
        """Atualiza os dados de um empréstimo no banco de dados."""
        self.db_session.merge(loan)
        self.db_session.commit()

    def delete_loan(self, loan_id):
        """Deleta um empréstimo do banco de dados pelo seu ID."""
        loan = self.db_session.query(Loan).get(loan_id)
        if loan:
            self.db_session.delete(loan)
            self.db_session.commit()
