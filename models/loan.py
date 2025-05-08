class Loan:
    """
    Representa um empréstimo de livro no sistema da biblioteca.

    Atributos:
    id (int): Identificador único do empréstimo.
    id_client (int): Identificador do cliente que realizou o empréstimo.
    start (str): Data de início do empréstimo.
    end (str): Data de fim do empréstimo.
    """

    def __init__(self, id, id_client, start, end):
        """
        Inicializa um empréstimo com os dados fornecidos, com validação.

        Args:
        id (int): Identificador único do empréstimo.
        id_client (int): Identificador do cliente.
        start (str): Data de início do empréstimo.
        end (str): Data de fim do empréstimo.

        Raises:
        ValueError: Se algum parâmetro for inválido.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um inteiro não negativo.")
        if not isinstance(id_client, int) or id_client < 0:
            raise ValueError("ID do cliente deve ser um inteiro não negativo.")
        if not start or not isinstance(start, str):
            raise ValueError("A data de início deve ser uma string não vazia.")
        if not end or not isinstance(end, str):
            raise ValueError("A data de fim deve ser uma string não vazia.")
        
        self._id = id
        self._id_client = id_client
        self._start = start
        self._end = end

    @property
    def id(self):
        """Retorna o identificador do empréstimo."""
        return self._id

    @property
    def id_client(self):
        """Retorna o identificador do cliente."""
        return self._id_client

    @property
    def start(self):
        """Retorna a data de início do empréstimo."""
        return self._start

    @property
    def end(self):
        """Retorna a data de fim do empréstimo."""
        return self._end

    def __repr__(self):
        """
        Representação em string do empréstimo, com ID do empréstimo e ID do cliente.
        """
        return f'<Loan ID: {self.id} (Client ID: {self.id_client})>'
