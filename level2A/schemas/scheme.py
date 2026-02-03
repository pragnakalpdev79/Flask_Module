from flask_marshmallow import Marshmallow
from marshmallow import ValidationError
from models import User

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True  # Optional: deserialize to model instances
        exclude = ("password_hash",)  # Never expose password hashes

# Initialize schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)