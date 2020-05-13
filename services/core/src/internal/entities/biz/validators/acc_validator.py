from marshmallow import Schema, fields
from marshmallow.validate import Length


class AccSchema(Schema):
    username = fields.Str(required=True, validate=Length(min=3, max=50))
