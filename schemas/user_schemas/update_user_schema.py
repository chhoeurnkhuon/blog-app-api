from marshmallow import Schema, fields, validate

class UpdateUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=6, max=12))
    gender = fields.Str(required=True, validate=validate.Length(max=10))