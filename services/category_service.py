from repositories.category_repository import CategoryRepository
from models.category import Category
from sqlalchemy.exc import SQLAlchemyError

class CategoryService:
    """
    Serviço responsável pela lógica de negócios relacionada às categorias.
    """

    def __init__(self, db_session):
        """
        Inicializa o serviço de categorias.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.category_repository = CategoryRepository(db_session)

    def list_categories(self):
        """Retorna todas as categorias."""
        try:
            return self.category_repository.get_all_categories()
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao listar categorias: {str(e)}")

    def get_category(self, category_id):
        """Retorna uma categoria específica pelo seu ID."""
        try:
            category = self.category_repository.get_category_by_id(category_id)
            if not category:
                raise ValueError(f"Categoria com ID {category_id} não encontrada.")
            return category
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao obter categoria: {str(e)}")

    def add_category(self, category):
        """Adiciona uma nova categoria."""
        try:
            if not category.name or not category.description:
                raise ValueError("Nome e descrição são obrigatórios.")
            if len(category.description) < 10:
                raise ValueError("A descrição deve ter pelo menos 10 caracteres.")
            
            self.category_repository.add_category(category)
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao adicionar categoria: {str(e)}")

    def update_category(self, category):
        """Atualiza uma categoria existente."""
        try:
            if not category.name or not category.description:
                raise ValueError("Nome e descrição são obrigatórios.")
            if len(category.description) < 10:
                raise ValueError("A descrição deve ter pelo menos 10 caracteres.")

            self.category_repository.update_category(category)
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao atualizar categoria: {str(e)}")

    def delete_category(self, category_id):
        """Deleta uma categoria pelo seu ID."""
        try:
            category = self.category_repository.get_category_by_id(category_id)
            if not category:
                raise ValueError(f"Categoria com ID {category_id} não encontrada.")
            self.category_repository.delete_category(category_id)
        except ValueError as ve:
            raise ve
        except SQLAlchemyError as e:
            raise Exception(f"Erro ao deletar categoria: {str(e)}")
