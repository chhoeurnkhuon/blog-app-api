from marshmallow import fields, Schema

class RoleReponseSchema(Schema):
    id = fields.Int()
    role_name = fields.Str()