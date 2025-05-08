class Author:
    """
    Representa um autor no sistema da biblioteca.

    Atributos:
    id (int): Identificador único do autor.
    name (str): Nome do autor.
    biography (str): Biografia do autor.
    """
    
    def __init__(self, id, name, biography):
        """
        Inicializa um autor com os dados fornecidos, com validação.

        Args:
        id (int): Identificador único do autor.
        name (str): Nome do autor.
        biography (str): Biografia do autor.

        Raises:
        ValueError: Se o ID for inválido, ou se o nome ou biografia forem inválidos.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not name or not isinstance(name, str):
            raise ValueError("O nome do autor deve ser uma string não vazia.")
        if not biography or len(biography) < 10:
            raise ValueError("A biografia deve ser uma string com pelo menos 10 caracteres.")

        self._id = id
        self._name = name
        self._biography = biography

    @property
    def id(self):
        """Retorna o identificador do autor."""
        return self._id

    @property
    def name(self):
        """Retorna o nome do autor."""
        return self._name

    @name.setter
    def name(self, value):
        """Define o nome do autor, garantindo que não seja vazio."""
        if not value or not isinstance(value, str):
            raise ValueError("O nome do autor deve ser uma string não vazia.")
        self._name = value

    @property
    def biography(self):
        """Retorna a biografia do autor."""
        return self._biography

    @biography.setter
    def biography(self, value):
        """Define a biografia do autor, garantindo que tenha pelo menos 10 caracteres."""
        if not value or len(value) < 10:
            raise ValueError("A biografia deve ser uma string com pelo menos 10 caracteres.")
        self._biography = value

    def update_biography(self, new_biography):
        """
        Atualiza a biografia do autor.

        Args:
        new_biography (str): A nova biografia a ser atribuída.

        Raises:
        ValueError: Se a biografia fornecida for inválida.
        """
        self.biography = new_biography

    def __repr__(self):
        """
        Representação em string do autor, com seu nome e ID.
        """
        return f'<Author {self.name} (ID: {self.id})>'
