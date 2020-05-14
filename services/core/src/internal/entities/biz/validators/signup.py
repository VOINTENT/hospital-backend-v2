from marshmallow import Schema, fields, ValidationError

from src.internal.errors.signup import *


def validate_last_name(value: str):
    if len(value) > 50:
        return ValidationError(LAST_NAME_TOO_LARGE)


def validate_first_name(value: str):
    if len(value) > 50:
        return ValidationError(FIRST_NAME_TOO_LARGE)


def validate_middle_name(value: str):
    if len(value) > 50:
        return ValidationError(MIDDLE_NAME_TOO_LARGE)


def validate_phone_number(value: str):
    if len(value) > 15:
        return ValidationError(PHONE_NUMBER_TOO_LARGE)


def validate_email(value: str):
    if len(value) > 50:
        return ValidationError(EMAIL_TOO_LARGE)


def validate_password(value: str):
    if len(value) > 200:
        return ValidationError(PASSWORD_TOO_LARGE)


class SignupSchema(Schema):
    last_name = fields.Str(required=True, error_messages={'required': NOT_LAST_NAME}, validate=validate_last_name)
    first_name = fields.Str(required=True, error_messages={'required': NOT_FIRST_NAME}, validate=validate_first_name)
    middle_name = fields.Str(required=True, error_messages={'required': NOT_MIDDLE_NAME}, validate=validate_middle_name)
    phone_number = fields.Str(required=True, error_messages={'required': NOT_PHONE_NUMBER}, validate=validate_phone_number)
    email = fields.Str(required=True, error_messages={'required': NOT_EMAIL}, validate=validate_email)
    password = fields.Str(required=True, error_messages={'required': NOT_PASSWORD}, validate=validate_password)
