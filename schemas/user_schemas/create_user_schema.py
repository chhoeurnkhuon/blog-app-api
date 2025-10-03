from marshmallow import Schema, fields, validate

class CreateUserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=6, max=12))
    comfirm_password = fields.Str(required=True, validate=validate.Length(min=6, max=12))
    gender = fields.Str(required=True, validate=validate.OneOf(["MALE", "FEMALE"]))
    role_name = fields.Str(required=True, validate=validate.OneOf(["ADMIN", "USER"]))