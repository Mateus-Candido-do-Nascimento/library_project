class Category:
    """
    Representa uma categoria de livros no sistema da biblioteca.

    Atributos:
    id (int): Identificador único da categoria.
    name (str): Nome da categoria.
    """
    
    def __init__(self, id, name):
        """
        Inicializa uma categoria com os dados fornecidos, com validação.

        Args:
        id (int): Identificador único da categoria.
        name (str): Nome da categoria.

        Raises:
        ValueError: Se o ID ou o nome forem inválidos.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not name or not isinstance(name, str):
            raise ValueError("O nome da categoria deve ser uma string não vazia.")

        self._id = id
        self._name = name

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

    def __repr__(self):
        """
        Representação em string da categoria, com seu nome e ID.
        """
        return f'<Category {self.name} (ID: {self.id})>'
