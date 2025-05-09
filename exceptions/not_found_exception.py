class NotFoundException(Exception):
    """Exceção para quando um recurso não é encontrado."""
    def __init__(self, message="Recurso não encontrado"):
        self.message = message
        super().__init__(self.message)
