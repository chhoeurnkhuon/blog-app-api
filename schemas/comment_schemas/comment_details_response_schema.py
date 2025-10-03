from marshmallow import fields, Schema
from schemas import AuthorResponseSchema

class CommentDetailsResponse(Schema):
    id = fields.Int()
    content = fields.Str()
    created_at = fields.DateTime()
    author = fields.Nested(AuthorResponseSchema)