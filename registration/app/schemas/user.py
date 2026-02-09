from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields,validates
from marshmallow.exceptions import ValidationError
import re

class UserSchema(Schema):
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)
    email = fields.Email(required=True)
    passwrod = fields.Str(required=True)
    repass = fields.Str()
    address = fields.Str()
    hobbies = fields.Str()
    gender = fields.Bool(required=True)