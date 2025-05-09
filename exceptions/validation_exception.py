class ValidationException(Exception):
    """Exceção para erros de validação de dados."""
    def __init__(self, message="Erro de validação de dados"):
        self.message = message
        super().__init__(self.message)
