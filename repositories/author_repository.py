from models import author
from models.author import Author

class AuthorRepository:
    """
    Repositório responsável pela interação com os dados dos autores no banco de dados.
    """

    def __init__(self, db_session):
        """
        Inicializa o repositório de autores com a sessão do banco de dados.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.db_session = db_session

    def get_all_authors(self):
        """Retorna todos os autores do banco de dados."""
        return self.db_session.query(Author).all()

    def get_author_by_id(self, author_id):
        """Retorna um autor específico pelo seu ID."""
        return self.db_session.query(Author).filter_by(id=author_id).first()

    def add_author(self, author):
        """Adiciona um novo autor ao banco de dados."""
        try:
            self.db_session.add(author)
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()  # Reverte qualquer mudança em caso de erro
            raise ValueError(f"Erro ao adicionar autor: {str(e)}")

    def update_author(self, author):
        """Atualiza os dados de um autor no banco de dados."""
        try:
            # Em vez de merge, usamos flush() para garantir que a atualização seja feita
            self.db_session.flush()  
            self.db_session.merge(author)
            self.db_session.commit()
        except Exception as e:
            self.db_session.rollback()
            raise ValueError(f"Erro ao atualizar autor: {str(e)}")

    def delete_author(self, author_id):
        """Deleta um autor do banco de dados pelo seu ID."""
        try:
            author = self.db_session.query(Author).get(author_id)
            if author:
                self.db_session.delete(author)
                self.db_session.commit()
            else:
                raise ValueError("Autor não encontrado")
        except Exception as e:
            self.db_session.rollback()
            raise ValueError(f"Erro ao deletar autor: {str(e)}")
