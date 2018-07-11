from marshmallow import Schema
from webargs import fields, validate


class CategorySchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    description = fields.String(required=False)

    class Meta:
        strict = True


class ArticleSchema(Schema):
    
    id = fields.Int(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(3))
    content = fields.String(required=False)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    timestamp = fields.DateTime(dump_only=True)
    update_date = fields.DateTime(dump_only=True)

    class Meta:
        strict = True
