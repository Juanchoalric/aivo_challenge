from marshmallow import Schema, fields, ValidationError, validates

class LifeSatisfactionSchema(Schema):
    life_satisfaction_index = fields.Float(required=True, error_message={"required": "Life satisfaction index is required"})

    @validates("life_satisfaction_index")
    def validate_quantity(self, value):
        if type(value) == str:
            raise ValidationError("Life satisfaction index must be of float type")
        if value <= 0:
            raise ValidationError("Life satisfaction index must be greater than 0.")