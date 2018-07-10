from marshmallow import Schema
from webargs import fields, validate


class CategorySchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    description = fields.String(required=False)

    class Meta:
        strict = True
