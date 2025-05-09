class Client:
    """
    Representa um cliente do sistema da biblioteca.

    Atributos:
    id (int): Identificador único do cliente.
    name (str): Nome completo do cliente.
    email (str): Endereço de e-mail do cliente.
    """

    def __init__(self, id, name, email):
        """
        Inicializa um cliente com os dados fornecidos.

        Args:
            id (int): Identificador único do cliente.
            name (str): Nome do cliente.
            email (str): Endereço de e-mail do cliente.

        Raises:
            ValueError: Se algum dos campos for inválido.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not name or not isinstance(name, str):
            raise ValueError("O nome do cliente deve ser uma string não vazia.")
        if not email or not isinstance(email, str) or '@' not in email:
            raise ValueError("O e-mail do cliente deve ser válido.")

        self._id = id
        self._name = name
        self._email = email

    @property
    def id(self):
        """Retorna o ID do cliente."""
        return self._id

    @property
    def name(self):
        """Retorna o nome do cliente."""
        return self._name

    @name.setter
    def name(self, value):
        """Define o nome do cliente."""
        if not value or not isinstance(value, str):
            raise ValueError("O nome do cliente deve ser uma string não vazia.")
        self._name = value

    @property
    def email(self):
        """Retorna o e-mail do cliente."""
        return self._email

    @email.setter
    def email(self, value):
        """Define o e-mail do cliente."""
        if not value or not isinstance(value, str) or '@' not in value:
            raise ValueError("O e-mail do cliente deve ser válido.")
        self._email = value

    def __repr__(self):
        """Retorna a representação legível do cliente."""
        return f"<Client {self.name} (ID: {self.id})>"
