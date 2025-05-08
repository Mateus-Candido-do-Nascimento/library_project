class CategoryRepository:
    """
    Repositório responsável pela interação com os dados das categorias no banco de dados.
    """

    def __init__(self, db_session):
        """
        Inicializa o repositório de categorias com a sessão do banco de dados.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.db_session = db_session

    def get_all_categories(self):
        """Retorna todas as categorias do banco de dados."""
        return self.db_session.query(Category).all()

    def get_category_by_id(self, category_id):
        """Retorna uma categoria específica pelo seu ID."""
        return self.db_session.query(Category).filter_by(id=category_id).first()

    def add_category(self, category):
        """Adiciona uma nova categoria ao banco de dados."""
        self.db_session.add(category)
        self.db_session.commit()

    def update_category(self, category):
        """Atualiza os dados de uma categoria no banco de dados."""
        self.db_session.merge(category)
        self.db_session.commit()

    def delete_category(self, category_id):
        """Deleta uma categoria do banco de dados pelo seu ID."""
        category = self.db_session.query(Category).get(category_id)
        if category:
            self.db_session.delete(category)
            self.db_session.commit()
