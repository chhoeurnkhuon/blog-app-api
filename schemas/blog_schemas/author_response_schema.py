from marshmallow import Schema, fields

class AuthorResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
