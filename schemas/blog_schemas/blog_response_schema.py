from marshmallow import Schema, validate, fields
from .author_response_schema import AuthorResponseSchema

class BlogResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    created_date = fields.DateTime()
    author = fields.Nested(AuthorResponseSchema)