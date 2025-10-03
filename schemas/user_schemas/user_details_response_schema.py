from marshmallow import Schema, fields, validate
from .role_response_schema import RoleReponseSchema

class UserDetailsResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    gender = fields.Str()
    created_at = fields.DateTime()
    
    roles = fields.Nested(RoleReponseSchema(many=True))