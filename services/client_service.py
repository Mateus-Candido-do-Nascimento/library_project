from repositories.client_repository import ClientRepository

class ClientService:
    """
    Serviço responsável pela lógica de negócios relacionada aos clientes.
    """

    def __init__(self, db_session):
        """
        Inicializa o serviço de clientes.

        Args:
        db_session (SQLAlchemy session): A sessão do banco de dados.
        """
        self.client_repository = ClientRepository(db_session)

    def list_clients(self):
        """Retorna todos os clientes."""
        return self.client_repository.get_all_clients()

    def get_client(self, client_id):
        """Retorna um cliente específico pelo seu ID."""
        return self.client_repository.get_client_by_id(client_id)

    def add_client(self, client):
        """Adiciona um novo cliente."""
        self.client_repository.add_client(client)

    def update_client(self, client):
        """Atualiza um cliente existente."""
        self.client_repository.update_client(client)

    def delete_client(self, client_id):
        """Deleta um cliente pelo seu ID."""
        self.client_repository.delete_client(client_id)
