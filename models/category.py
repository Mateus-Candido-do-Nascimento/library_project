class Category:
    """
    Representa uma categoria de livros no sistema da biblioteca.

    Atributos:
    id (int): Identificador único da categoria.
    name (str): Nome da categoria.
    description (str): Descrição da categoria.
    """

    def __init__(self, id, name, description):
        """
        Inicializa a categoria com os dados fornecidos, com validação.

        Args:
        id (int): Identificador único da categoria.
        name (str): Nome da categoria.
        description (str): Descrição da categoria.

        Raises:
        ValueError: Se o ID for inválido, ou se o nome ou descrição forem inválidos.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not name or not isinstance(name, str):
            raise ValueError("O nome da categoria deve ser uma string não vazia.")
        if not description or len(description) < 10:
            raise ValueError("A descrição deve ser uma string com pelo menos 10 caracteres.")

        self._id = id
        self._name = name
        self._description = description

    @property
    def id(self):
        """Retorna o identificador da categoria."""
        return self._id

    @property
    def name(self):
        """Retorna o nome da categoria."""
        return self._name

    @name.setter
    def name(self, value):
        """Define o nome da categoria, garantindo que não seja vazio."""
        if not value or not isinstance(value, str):
            raise ValueError("O nome da categoria deve ser uma string não vazia.")
        self._name = value

    @property
    def description(self):
        """Retorna a descrição da categoria."""
        return self._description

    @description.setter
    def description(self, value):
        """Define a descrição da categoria, garantindo que tenha pelo menos 10 caracteres."""
        if not value or len(value) < 10:
            raise ValueError("A descrição deve ser uma string com pelo menos 10 caracteres.")
        self._description = value

    def update_description(self, new_description):
        """
        Atualiza a descrição da categoria.

        Args:
        new_description (str): A nova descrição a ser atribuída.

        Raises:
        ValueError: Se a descrição fornecida for inválida.
        """
        self.description = new_description

    def __repr__(self):
        """
        Representação em string da categoria, com seu nome e ID.
        """
        return f'<Category {self.name} (ID: {self.id})>'
