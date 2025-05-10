from repositories.author_repository import AuthorRepository
from models.author import Author
from sqlalchemy.exc import SQLAlchemyError

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
        try:
            return self.author_repository.get_all_authors()
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao listar autores: {str(e)}")

    def get_author(self, author_id):
        """Retorna um autor específico pelo seu ID."""
        try:
            author = self.author_repository.get_author_by_id(author_id)
            if not author:
                raise ValueError(f"Autor com ID {author_id} não encontrado.")
            return author
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao obter autor: {str(e)}")

    def add_author(self, author):
        """Adiciona um novo autor."""
        try:
            # Validação de dados (exemplo básico)
            if not author.name or not author.biography:
                raise ValueError("Nome e biografia são obrigatórios.")
            if len(author.biography) < 10:
                raise ValueError("A biografia deve ter pelo menos 10 caracteres.")
            
            self.author_repository.add_author(author)
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao adicionar autor: {str(e)}")

    def update_author(self, author):
        """Atualiza um autor existente."""
        try:
            # Validação de dados
            if not author.name or not author.biography:
                raise ValueError("Nome e biografia são obrigatórios.")
            if len(author.biography) < 10:
                raise ValueError("A biografia deve ter pelo menos 10 caracteres.")

            self.author_repository.update_author(author)
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao atualizar autor: {str(e)}")

    def delete_author(self, author_id):
        """Deleta um autor pelo seu ID."""
        try:
            # Verifica se o autor existe antes de tentar excluir
            author = self.author_repository.get_author_by_id(author_id)
            if not author:
                raise ValueError(f"Autor com ID {author_id} não encontrado.")
            self.author_repository.delete_author(author_id)
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao deletar autor: {str(e)}")
