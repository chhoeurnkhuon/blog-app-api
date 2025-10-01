from marshmallow import Schema, validate, fields
from .author_response_schema import AuthorResponseSchema

class BlogUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=3, max=25))
    description = fields.Str(required=True, validate=validate.Length(min=3, max=255))
    created_date = fields.DateTime(dump_only=True)
    author = fields.Nested(AuthorResponseSchema, dump_only=True)