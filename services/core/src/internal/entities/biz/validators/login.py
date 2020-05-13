from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Length

from src.internal.errors.login import NOT_EMAIL_OR_PHONE_NUMBER, NOT_PASSWORD


class LoginSchema(Schema):
    email_or_phone = fields.Str(required=True,
                                error_messages={'required': NOT_EMAIL_OR_PHONE_NUMBER})

    password = fields.Str(required=True,
                          error_messages={'required': NOT_PASSWORD})
