class BusinessException(Exception):
    """Exceção para erros de regra de negócio."""
    def __init__(self, message="Erro de regra de negócio"):
        self.message = message
        super().__init__(self.message)
