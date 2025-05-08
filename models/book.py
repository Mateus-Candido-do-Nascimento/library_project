class Book:
    """
    Representa um livro no sistema da biblioteca.

    Atributos:
    id (int): Identificador único do livro.
    name (str): Nome do livro.
    description (str): Descrição do livro.
    id_author (int): Identificador do autor do livro.
    id_category (int): Identificador da categoria do livro.
    quantity (int): Quantidade disponível do livro.
    """
    
    def __init__(self, id, name, description, id_author, id_category, quantity):
        """
        Inicializa um livro com os dados fornecidos, com validação.

        Args:
        id (int): Identificador único do livro.
        name (str): Nome do livro.
        description (str): Descrição do livro.
        id_author (int): Identificador do autor.
        id_category (int): Identificador da categoria.
        quantity (int): Quantidade do livro disponível.

        Raises:
        ValueError: Se algum parâmetro for inválido.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not name or not isinstance(name, str):
            raise ValueError("O nome do livro deve ser uma string não vazia.")
        if not description or not isinstance(description, str):
            raise ValueError("A descrição do livro deve ser uma string não vazia.")
        if not isinstance(id_author, int) or id_author < 0:
            raise ValueError("ID do autor deve ser um inteiro não negativo.")
        if not isinstance(id_category, int) or id_category < 0:
            raise ValueError("ID da categoria deve ser um inteiro não negativo.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")

        self._id = id
        self._name = name
        self._description = description
        self._id_author = id_author
        self._id_category = id_category
        self._quantity = quantity

    @property
    def id(self):
        """Retorna o identificador do livro."""
        return self._id

    @property
    def name(self):
        """Retorna o nome do livro."""
        return self._name

    @name.setter
    def name(self, value):
        """Define o nome do livro, garantindo que não seja vazio."""
        if not value or not isinstance(value, str):
            raise ValueError("O nome do livro deve ser uma string não vazia.")
        self._name = value

    @property
    def description(self):
        """Retorna a descrição do livro."""
        return self._description

    @description.setter
    def description(self, value):
        """Define a descrição do livro, garantindo que não seja vazia."""
        if not value or not isinstance(value, str):
            raise ValueError("A descrição do livro deve ser uma string não vazia.")
        self._description = value

    @property
    def id_author(self):
        """Retorna o identificador do autor do livro."""
        return self._id_author

    @property
    def id_category(self):
        """Retorna o identificador da categoria do livro."""
        return self._id_category

    @property
    def quantity(self):
        """Retorna a quantidade disponível do livro."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Define a quantidade disponível do livro, garantindo que seja positiva."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("A quantidade deve ser um inteiro não negativo.")
        self._quantity = value

    def __repr__(self):
        """
        Representação em string do livro, com seu nome e ID.
        """
        return f'<Book {self.name} (ID: {self.id})>'
