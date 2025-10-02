from marshmallow import Schema, fields, validate

class CreateCommentSchema(Schema):
    content = fields.Str(required=True, validate=validate.Length(min=3, max=255))