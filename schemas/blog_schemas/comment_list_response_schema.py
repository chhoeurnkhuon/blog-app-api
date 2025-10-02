from marshmallow import Schema, fields
from .author_response_schema import AuthorResponseSchema

class CommentListResponseSchema(Schema):
    id = fields.Int()
    content = fields.Str()
    created_at = fields.DateTime()
    author = fields.Nested(AuthorResponseSchema)