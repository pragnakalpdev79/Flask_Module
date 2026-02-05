from errors import AppError
from extensions import db
from models import User

def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        raise AppError("User not found",404)
    return user