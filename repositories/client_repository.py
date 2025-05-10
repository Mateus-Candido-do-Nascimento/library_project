from models.client import Client
class ClientRepository:
    """
    Repositório responsável pela interação com os dados dos clientes no banco de dados.
    """

    def __init__(self, db_session):
        """
        Inicializa o repositório de clientes com a sessão do banco de dados.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.db_session = db_session
        
    def get_client_by_email(self, email):
        """Busca cliente pelo e-mail."""
        return self.db_session.query(Client).filter_by(email=email).first()


    def get_all_clients(self):
        """Retorna todos os clientes do banco de dados."""
        return self.db_session.query(Client).all()

    def get_client_by_id(self, client_id):
        """Retorna um cliente específico pelo seu ID."""
        return self.db_session.query(Client).filter_by(id=client_id).first()

    def add_client(self, client):
        """Adiciona um novo cliente ao banco de dados."""
        self.db_session.add(client)
        self.db_session.commit()

    def update_client(self, client):
        """Atualiza os dados de um cliente no banco de dados."""
        self.db_session.merge(client)
        self.db_session.commit()

    def delete_client(self, client_id):
        """Deleta um cliente do banco de dados pelo seu ID."""
        client = self.db_session.query(Client).get(client_id)
        if client:
            self.db_session.delete(client)
            self.db_session.commit()
