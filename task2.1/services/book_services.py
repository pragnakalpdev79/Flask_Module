from models import Author,Book
from extensions import db
from sqlalchemy import update
import os 

class BookService:

#===============================================================================
#2.2 FUNCTION TO CREATE A BOOK
    @staticmethod #2.1 adding a new book
    def add_book(title,price,author_id):
        os.system('clear')
        print("author id",author_id,type(author_id))
        if Book.query.filter_by(title=title).first(): #first checking if book exists or not
            return None,"Book already in the list"
        #the book does not exists,so now checking if the author id is valid or not
        new_book = Book(title=title,price=price,author_id=author_id)
        if not Author.query.filter_by(id=author_id).first(): 
            return None,"Invalid Author Id"
        db.session.add(new_book)
        db.session.commit()
        return new_book,None
#===============================================================================
#2.3 FUNCTION TO GET AUTHOR WITH BOOK
    @staticmethod
    def get_books(id):
        books = Book.query.filter_by(author_id=id).all()
        if not books:
            return None,"No author found with given author id"
        #ids = [i.title for i in books]
        
        #print(ids)
        print("books here" ,books)
        return books,None
#===============================================================================
#2.4 FUNCTION TO UPDATE BOOK PRICE
    @staticmethod
    def update_book_price(id,new_price):
        books = Book.query.filter_by(id=id).first()
        if not books:
            return None,"No Book found with given book id"
        #ids = [i.title for i in books]
        with db.session() as up :
            up.execute(update(Book).where(Book.id==id).values(price=new_price))
            up.commit()
        #   print(ids)
            print("books here" ,books)
            return books.price,None
        return None,"Something went wrong,price not updated"
    

