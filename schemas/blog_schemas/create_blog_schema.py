from marshmallow import Schema, validate, fields

class CreateBlogSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=3, max=25))
    description = fields.Str(required=True, validate=validate.Length(min=3, max=255))