from models import Author,Book
from extensions import db
from sqlalchemy import update

class UserService:
    @staticmethod
    def add_author(name,bio):
        if Author.query.filter_by(name=name).first():
            return None,"Author already in the list"
        new_author = Author(name=name,bio=bio)
        db.session.add(new_author)
        db.session.commit()

        return new_author,None
    @staticmethod
    def get_all_authors():
        return Author.query.all()
    
    @staticmethod
    def delete_auth(id):
        if not Author.query.filter_by(id=id).first():
            return None,"Author not in the list"
        db.session.execute(update(Author).where(Author.id==id).values(deleted=True))
        #db.session.execute(update(Book).where(Book.id==id).values(deleted=True))
        db.session.commit()
        return id,None