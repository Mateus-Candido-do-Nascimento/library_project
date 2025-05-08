class BookLoan:
    """
    Representa a associação entre um livro e um empréstimo no sistema da biblioteca.

    Atributos:
    id (int): Identificador único do registro de empréstimo de livro.
    id_book (int): Identificador do livro emprestado.
    id_loan (int): Identificador do empréstimo associado.
    book_quantity (int): Quantidade de cópias do livro emprestadas.
    """

    def __init__(self, id, id_book, id_loan, book_quantity):
        """
        Inicializa um registro de empréstimo de livro com os dados fornecidos, com validação.

        Args:
        id (int): Identificador único do registro de empréstimo de livro.
        id_book (int): Identificador do livro emprestado.
        id_loan (int): Identificador do empréstimo associado.
        book_quantity (int): Quantidade de cópias do livro emprestadas.

        Raises:
        ValueError: Se algum parâmetro for inválido.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not isinstance(id_book, int) or id_book < 0:
            raise ValueError("ID do livro deve ser um inteiro não negativo.")
        if not isinstance(id_loan, int) or id_loan < 0:
            raise ValueError("ID do empréstimo deve ser um inteiro não negativo.")
        if not isinstance(book_quantity, int) or book_quantity < 1:
            raise ValueError("A quantidade de livros emprestados deve ser um inteiro positivo.")
        
        self._id = id
        self._id_book = id_book
        self._id_loan = id_loan
        self._book_quantity = book_quantity

    @property
    def id(self):
        """Retorna o identificador do empréstimo de livro."""
        return self._id

    @property
    def id_book(self):
        """Retorna o identificador do livro emprestado."""
        return self._id_book

    @property
    def id_loan(self):
        """Retorna o identificador do empréstimo associado."""
        return self._id_loan

    @property
    def book_quantity(self):
        """Retorna a quantidade de livros emprestados."""
        return self._book_quantity

    @book_quantity.setter
    def book_quantity(self, value):
        """Define a quantidade de livros emprestados, garantindo que seja positiva."""
        if not isinstance(value, int) or value < 1:
            raise ValueError("A quantidade de livros emprestados deve ser um inteiro positivo.")
        self._book_quantity = value

    def __repr__(self):
        """
        Representação em string do empréstimo de livro, com ID do empréstimo e quantidade de livros.
        """
        return f'<BookLoan ID: {self.id} (Book ID: {self.id_book}, Loan ID: {self.id_loan})>'
