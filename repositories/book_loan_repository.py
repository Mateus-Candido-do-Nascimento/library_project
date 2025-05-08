class BookLoanRepository:
    """
    Repositório responsável pela interação com a associação entre livros e empréstimos no banco de dados.
    """

    def __init__(self, db_session):
        """
        Inicializa o repositório de associações de empréstimos de livros com a sessão do banco de dados.
        
        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.db_session = db_session

    def get_all_book_loans(self):
        """Retorna todas as associações de empréstimos de livros do banco de dados."""
        return self.db_session.query(BookLoan).all()

    def get_book_loan_by_id(self, book_loan_id):
        """Retorna uma associação de empréstimo de livro pelo seu ID."""
        return self.db_session.query(BookLoan).filter_by(id=book_loan_id).first()

    def add_book_loan(self, book_loan):
        """Adiciona uma nova associação de empréstimo de livro ao banco de dados."""
        self.db_session.add(book_loan)
        self.db_session.commit()

    def update_book_loan(self, book_loan):
        """Atualiza uma associação de empréstimo de livro no banco de dados."""
        self.db_session.merge(book_loan)
        self.db_session.commit()

    def delete_book_loan(self, book_loan_id):
        """Deleta uma associação de empréstimo de livro do banco de dados pelo seu ID."""
        book_loan = self.db_session.query(BookLoan).get(book_loan_id)
        if book_loan:
            self.db_session.delete(book_loan)
            self.db_session.commit()
