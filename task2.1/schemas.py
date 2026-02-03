from marshmallow import Schema,fields

class Authorschema(Schema):
    name = fields.Str()
    bio = fields.Str()

