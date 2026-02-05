from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields,validates
from marshmallow.exceptions import ValidationError
import re

class Authorschema(Schema):
    name = fields.Str(required=True)
    bio = fields.Str(required=True)
    @validates('name','bio')
    def validate_string(self,value,**kwargs): #https://github.com/marshmallow-code/marshmallow/issues/1546 -- synatx requires kwargs to work
        if not value:
            raise ValidationError('name and bio can not be empty.')
        if bool(re.fullmatch(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$', value)):
            raise ValidationError('name and bio, can not be only numbers.')

