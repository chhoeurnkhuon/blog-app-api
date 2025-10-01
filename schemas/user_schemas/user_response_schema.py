from marshmallow import Schema, fields, validate

class UserResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    gender = fields.Str()