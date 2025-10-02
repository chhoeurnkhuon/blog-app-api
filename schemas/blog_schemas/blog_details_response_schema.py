from marshmallow import Schema, validate, fields
from .author_response_schema import AuthorResponseSchema
from .comment_list_response_schema import CommentListResponseSchema

class BlogDetailsResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    created_date = fields.DateTime()
    
    ## blog author
    author = fields.Nested(AuthorResponseSchema)
    
    ## list comments
    comments = fields.Nested(CommentListResponseSchema, many=True)