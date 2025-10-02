from marshmallow import Schema, fields
from schemas import AuthorResponseSchema

class CommentResponseSchema(Schema):
    id = fields.Int()
    content = fields.Str()
    created_at = fields.DateTime()
    author = fields.Nested(AuthorResponseSchema)