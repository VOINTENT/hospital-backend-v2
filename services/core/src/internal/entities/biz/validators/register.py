from marshmallow import Schema, fields

from src.internal.errors.register import NOT_RECEPTION_LINE_ID, WRONG_RECEPTION_LINE_ID


class RegisterSchema(Schema):
    reception_line_id = fields.Int(required=True, error_messages={
                                        'required': NOT_RECEPTION_LINE_ID,
                                        'invalid': WRONG_RECEPTION_LINE_ID}
                                   )
