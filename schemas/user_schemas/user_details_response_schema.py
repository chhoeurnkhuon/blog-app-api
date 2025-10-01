from marshmallow import Schema, fields, validate

class UserDetailsResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    gender = fields.Str()