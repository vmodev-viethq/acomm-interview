from marshmallow import Schema, fields, validates, validates_schema, ValidationError


class FrogJumpRequestPayload(Schema):
    river_length = fields.Integer(required=True)
    leave_lists = fields.List(
        fields.Integer(),
        required=True
    )

    @validates_schema
    def validate_river_length(self, data, *args, **kwargs):
        river_length = data['river_length']
        if river_length < 0:
            raise ValidationError(
                "Value must be more than 0",
                "river_length")
        elif river_length > 100000:
            raise ValidationError(
                "Value must be less than 100000",
                "river_length")
        return data

    @validates_schema
    def validate_leave_lists(self, data, *args, **kwargs):
        river_length = data['river_length']
        leave_lists = data['leave_lists']
        for leave in leave_lists:
            if leave > river_length:
                raise ValidationError(
                    "Leave position cannot exceed river length",
                    'leave_lists'
                )

        return data


request_payload = FrogJumpRequestPayload()
