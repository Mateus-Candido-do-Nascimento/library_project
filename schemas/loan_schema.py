from marshmallow import Schema, fields, validate

class LoanSchema(Schema):
    """
    Esquema de validação para empréstimos.

    Campos:
    - id: ID do empréstimo (somente leitura).
    - id_client: ID do cliente que realizou o empréstimo (obrigatório).
    - start_date: Data de início do empréstimo (obrigatório).
    - end_date: Data de término do empréstimo (obrigatório).
    - client_name: Nome do cliente (opcional para visualização).
    """
    id = fields.Int(dump_only=True)
    id_client = fields.Int(required=True, error_messages={"required": "O ID do cliente é obrigatório."})
    start_date = fields.Date(required=True, error_messages={"required": "A data de início é obrigatória."})
    end_date = fields.Date(required=True, error_messages={"required": "A data de término é obrigatória."})

    # Campos opcionais para visualização no frontend
    client_name = fields.Str(attribute="client.name")
