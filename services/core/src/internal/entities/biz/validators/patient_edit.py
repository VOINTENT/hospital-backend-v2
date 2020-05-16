from marshmallow import Schema, fields, ValidationError

from src.internal.errors.patient import WRONG_BIRTH_DATE_FORMAT, WRONG_GENDER_TYPE, WRONG_SNILS_FORMAT, \
    WRONG_POLICY_FORMAT
from src.internal.errors.signup import *


def validate_last_name(value: str):
    if len(value) > 50:
        raise ValidationError(LAST_NAME_TOO_LARGE)


def validate_first_name(value: str):
    if len(value) > 50:
        raise ValidationError(FIRST_NAME_TOO_LARGE)


def validate_middle_name(value: str):
    if len(value) > 50:
        raise ValidationError(MIDDLE_NAME_TOO_LARGE)


def validate_birth_date(value: str):
    if len(value) > 10 or len(value) < 8:
        raise ValidationError(WRONG_BIRTH_DATE_FORMAT)

    date = value.split('-')
    if len(date) != 3 or (len(date[0]) != 1 and len(date[0]) != 2) or (len(date[1]) != 1 and len(date[1]) != 2) or len(date[2]) != 4:
        raise ValidationError(WRONG_BIRTH_DATE_FORMAT)

    if not date[0].isdigit() or not date[1].isdigit() or not date[1].isdigit():
        raise ValidationError(WRONG_BIRTH_DATE_FORMAT)


def validate_gender(value: int):
    if value not in (1, 2, 3):
        raise ValidationError(WRONG_GENDER_TYPE)


def validate_snils(value: str):
    if len(value) != 14:
        raise ValidationError(WRONG_SNILS_FORMAT)

    snils = value.split('-')
    snils = snils[:2] + snils[2].split(' ')
    if len(snils) != 4 or len(snils[0]) != 3 or len(snils[1]) != 3 or len(snils[2]) != 3 or len(snils[3]) != 2:
        raise ValidationError(WRONG_SNILS_FORMAT)

    if not snils[0].isdigit() or not snils[1].isdigit() or not snils[2].isdigit() or not snils[3].isdigit():
        raise ValidationError(WRONG_SNILS_FORMAT)


def validate_policy(value: str):
    if len(value) != 16 or not value.isdigit():
        raise ValidationError(WRONG_POLICY_FORMAT)


class PatientEditSchema(Schema):
    last_name = fields.Str(validate=validate_last_name)
    first_name = fields.Str(validate=validate_first_name)
    middle_name = fields.Str(validate=validate_middle_name)
    birth_date = fields.Str(validate=validate_birth_date)
    gender = fields.Int(validate=validate_gender, error_messages={'invalid': WRONG_GENDER_TYPE})
    snils = fields.Str(validate=validate_snils)
    policy = fields.Str(validate=validate_policy)

