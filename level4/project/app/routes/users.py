import click 
from flask import Blueprint
from flask.cli import with_appcontext
from app.extensions import db
from app.models.author import Author
from app.models.book import Book


usersbp = Blueprint('seed', __name__)

@usersbp.cli.command('create') #for testing
@with_appcontext
@click.argument('username')
def create(username):
    """ Creates a user """
    print(f"Create user: {username}")

@usersbp.cli.command('db') #for testing
@with_appcontext
def seed():
    """ Creates a user """
    authors = ["Author1","Author2","Author3","Author4","Author5"]
    bios = ["Bio1","Bio2","Bio3","Bio4","Bio5"]
    book_titles = ["Book1","Book2","Book3","Book4","Book5"]
    price = [20,40,20,40,20]
    author_list_id = []
    for i,j in zip(authors,bios):
        if Author.query.filter_by(name=i).first():
            continue
        new_author = Author(name=i,bio=j)
        db.session.add(new_author)
        db.session.commit()
        author = Author.query.filter_by(name=i).first()
        #print("author:- ",author)
        #print("id:- ",author.id)
        author_list_id.append(author.id)
    #author_list_id = [i.id for i in Author.query.all()]
    if not author_list_id:
        print("DB Already contains data,seeding it again is not suggested")
        return 
    for a,b,c in zip(author_list_id,book_titles,price):
        if Book.query.filter_by(title=b).first():
            continue
        new_book = Book(title=b,price=c,author_id=a)
        db.session.add(new_book)
        db.session.commit()
    print("DB Seeded!!")

