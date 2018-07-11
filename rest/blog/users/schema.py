from marshmallow import Schema
from webargs import fields, validate


class UserSchema(Schema):

    id = fields.Int(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(3))
    email = fields.String(required=True, validate=validate.Length(10))
    password = fields.String(required=True, validate=validate.Length(8),
                             load_only=True)

    class Meta:
        strict = True
