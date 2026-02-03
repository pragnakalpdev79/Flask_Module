from models import Book
from extensions import db

class UserService:
    @staticmethod
    def create_author(name,bio):
        if Author.query.filter_by(name=name).first():
            return None,"Author already exists"
        
        new_author = Author(name=name,bio=bio)
        db.session.add(new_author)
        db.session.commit()

        return new_author,None
    
    @staticmethod
    def get_all_authors():
        return Author.query.all()

