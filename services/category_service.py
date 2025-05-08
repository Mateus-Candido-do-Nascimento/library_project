from repositories.category_repository import CategoryRepository

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
        return self.category_repository.get_all_categories()

    def get_category(self, category_id):
        """Retorna uma categoria específica pelo seu ID."""
        return self.category_repository.get_category_by_id(category_id)

    def add_category(self, category):
        """Adiciona uma nova categoria."""
        self.category_repository.add_category(category)

    def update_category(self, category):
        """Atualiza uma categoria existente."""
        self.category_repository.update_category(category)

    def delete_category(self, category_id):
        """Deleta uma categoria pelo seu ID."""
        self.category_repository.delete_category(category_id)
