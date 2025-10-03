from marshmallow import validate, Schema, fields

class UpdateCommentSchema(Schema):
    content = fields.Str(required=True, validate=validate.Length(min=3, max=255))