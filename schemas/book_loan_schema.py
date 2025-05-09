from marshmallow import Schema, fields, validate

class BookLoanSchema(Schema):
    """
    Esquema de validação para a relação entre livros e empréstimos.

    Campos:
    - id: ID do relacionamento (somente leitura).
    - id_book: ID do livro (obrigatório).
    - id_loan: ID do empréstimo (obrigatório).
    - book_quantity: Quantidade de livros emprestados (obrigatório e deve ser maior que zero).
    - book_title: Título do livro (opcional para visualização).
    """
    id = fields.Int(dump_only=True)
    id_book = fields.Int(required=True, error_messages={"required": "O ID do livro é obrigatório."})
    id_loan = fields.Int(required=True, error_messages={"required": "O ID do empréstimo é obrigatório."})
    book_quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="A quantidade de livros deve ser maior que zero."),
        error_messages={"required": "A quantidade de livros é obrigatória."}
    )

    # Campo adicional para visualização
    book_title = fields.Str(attribute="book.name")
