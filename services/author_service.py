from repositories.author_repository import AuthorRepository

class AuthorService:
    """
    Serviço responsável pela lógica de negócios relacionada aos autores.
    """

    def __init__(self, db_session):
        """
        Inicializa o serviço de autores.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.author_repository = AuthorRepository(db_session)

    def list_authors(self):
        """Retorna todos os autores."""
        return self.author_repository.get_all_authors()

    def get_author(self, author_id):
        """Retorna um autor específico pelo seu ID."""
        return self.author_repository.get_author_by_id(author_id)

    def add_author(self, author):
        """Adiciona um novo autor."""
        self.author_repository.add_author(author)

    def update_author(self, author):
        """Atualiza um autor existente."""
        self.author_repository.update_author(author)

    def delete_author(self, author_id):
        """Deleta um autor pelo seu ID."""
        self.author_repository.delete_author(author_id)
