from marshmallow import Schema, fields, validate

class ClientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(
        required=True,
        validate=validate.Length(min=1, error="O nome do cliente é obrigatório")
    )
    email = fields.Email(
        required=True,
        error_messages={
            "required": "O e-mail é obrigatório",
            "invalid": "E-mail inválido"
        }
    )
