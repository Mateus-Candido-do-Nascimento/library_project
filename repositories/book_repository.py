class BookRepository:
    """
    Repositório responsável pela interação com os dados de livros no banco de dados.
    """

    def __init__(self, db_session):
        """
        Inicializa o repositório de livros com a sessão do banco de dados.
        
        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.db_session = db_session

    def get_all_books(self):
        """Retorna todos os livros do banco de dados."""
        return self.db_session.query(Book).all()

    def get_book_by_id(self, book_id):
        """Retorna um livro específico pelo seu ID."""
        return self.db_session.query(Book).filter_by(id=book_id).first()

    def add_book(self, book):
        """Adiciona um novo livro ao banco de dados."""
        self.db_session.add(book)
        self.db_session.commit()

    def update_book(self, book):
        """Atualiza os dados de um livro no banco de dados."""
        self.db_session.merge(book)
        self.db_session.commit()

    def delete_book(self, book_id):
        """Deleta um livro do banco de dados pelo seu ID."""
        book = self.db_session.query(Book).get(book_id)
        if book:
            self.db_session.delete(book)
            self.db_session.commit()
