from models import Author,Book
from extensions import db
from sqlalchemy import update
import os 

class AuthorService:
#===============================================================================
#2.1 FUNCTION TO CREATE AN AUTHOR
    @staticmethod #2.1 adding a new author
    def add_author(name,bio):
        if Author.query.filter_by(name=name).first():
                #print(Author.query.filter_by(name=name).first()) not querying again.
            return None,"Author already in the list"
        new_author = Author(name=name,bio=bio)
        db.session.add(new_author)
        db.session.commit()
        return new_author,None
#===============================================================================
#2.3 FUNCTION TO GET AUTHOR WITH BOOK
    @staticmethod
    def get_author_books(id):
        found = Author.query.filter_by(id=id).first()
        if not found:
            return None,"No author found with given author id"
        if found.deleted:
            return None,"The author Does not exist"
        author = found
        print(author)
        return author,None
#===============================================================================
#2.5 FUNCTION TO DELETE THE AUTHORS
    @staticmethod
    def delete_auth(id):
        if not Author.query.filter_by(id=id).first():
            return None,"Author not in the list"
        try:
            with db.session() as dl:
                dl.execute(update(Author).where(Author.id==id).values(deleted=True))
                dl.execute(update(Book).where(Book.author_id==id).values(deleted=True))
                dl.commit()
                return id,None
        except Exception as e:
            return None,f"Something went wrong code: {e}"
        