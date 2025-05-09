from marshmallow import Schema, fields, validate

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, error="O nome do livro é obrigatório")
    )
    description = fields.Str()
    id_author = fields.Int(required=True)
    id_category = fields.Int(required=True)
    quantity = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="A quantidade deve ser maior que zero")
    )

    # Campos extras apenas para visualização
    author_name = fields.Str(attribute="author.name", dump_only=True)
    category_name = fields.Str(attribute="category.name", dump_only=True)
